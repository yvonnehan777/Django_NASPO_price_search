from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from .models import NASPOItem

def search(request):
    # read and normalize inputs
    q_vendor = (request.GET.get("vendor") or "").strip()
    q_part = (request.GET.get("mpn") or "").strip()
    q_desc = (request.GET.get("desc") or "").strip()
    q_min = (request.GET.get("min_price") or "").strip()
    q_max = (request.GET.get("max_price") or "").strip()

    has_query = any([q_vendor, q_part, q_desc, q_min, q_max])

    queryset = NASPOItem.objects.none()  # default: no results until a search happens

    if has_query:
        qs = NASPOItem.objects.all()

        if q_vendor:
            qs = qs.filter(vendor__icontains=q_vendor)

        if q_part:
            qs = qs.filter(manufacturer_part_number__icontains=q_part)

        if q_desc:
            qs = qs.filter(description__icontains=q_desc)

        # numeric filters are safe because model fields are Decimal; empty strings are skipped
        if q_min:
            try:
                qs = qs.filter(naspo_price__gte=q_min)
            except ValueError:
                pass

        if q_max:
            try:
                qs = qs.filter(naspo_price__lte=q_max)
            except ValueError:
                pass

        queryset = qs.order_by("vendor", "manufacturer_part_number")

    paginator = Paginator(queryset, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "catalog_app/search.html",
        {
            "page_obj": page_obj,
            "has_query": has_query,
            "vendor": q_vendor,
            "mpn": q_part,
            "desc": q_desc,
            "min_price": q_min,
            "max_price": q_max,
        },
    )

def health(request):
    return render(request, "catalog_app/health.html", {"status": "ok"})
