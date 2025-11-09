import os
import django
import pandas as pd
from decimal import Decimal, InvalidOperation
import math

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "provider_search.settings")
django.setup()

from catalog_app.models import NASPOItem  # noqa

FILES = [
    "/srv/mita4/NASPO_Price_Catalog_A-E_10.15.2025.xlsx",
    "/srv/mita4/NASPO_Price_Catalog_F-H_10.15.2025.xlsx",
    "/srv/mita4/NASPO_Price_Catalog_I-P_10.15.2025.xlsx",
    "/srv/mita4/NASPO_Price_Catalog_Q-Z_10.15.2025.xlsx",
]

SHEET_NAME = "NASPO October 2025"


def to_decimal(x):
    # 1) pandas 的 NaN
    if x is None:
        return None
    if isinstance(x, float) and math.isnan(x):
        return None

    if isinstance(x, (int, Decimal)):
        return Decimal(str(x))
    if isinstance(x, float):
        return Decimal(str(x))

    s = str(x).strip()
    if s == "" or s.lower() == "nan":
        return None

    s = s.replace(",", "")
    try:
        return Decimal(s)
    except InvalidOperation:
        return None


def load_file(path):
    print(f"Loading {path} ...")
    df = pd.read_excel(path, sheet_name=SHEET_NAME)
    df = df.rename(
        columns={
            "Vendor": "vendor",
            "Description": "description",
            "Manufacturer Part Number": "manufacturer_part_number",
            "List Price": "list_price",
            "NASPO Price": "naspo_price",
        }
    )

    objs = []
    created_total = 0

    for _, row in df.iterrows():
        vendor = str(row.get("vendor") or "").replace("\xa0", " ").strip()
        if not vendor:
            continue

        obj = NASPOItem(
            vendor=vendor,
            description=row.get("description"),
            manufacturer_part_number=row.get("manufacturer_part_number"),
            list_price=to_decimal(row.get("list_price")),
            naspo_price=to_decimal(row.get("naspo_price")),
        )
        objs.append(obj)

        if len(objs) >= 2000:
            NASPOItem.objects.bulk_create(objs)
            created_total += len(objs)
            print(f"  inserted {created_total} rows so far...")
            objs = []

    if objs:
        NASPOItem.objects.bulk_create(objs)
        created_total += len(objs)

    print(f"Finished {path}, inserted {created_total} rows.")


def main():
    for f in FILES:
        if os.path.exists(f):
            load_file(f)
        else:
            print(f"WARNING: file not found: {f}")


if __name__ == "__main__":
    main()
