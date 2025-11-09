#🧾 Django NASPO Price Search

A web-based application built with Django and PostgreSQL, designed for efficient searching, filtering, and management of NASPO contract pricing data.
This project demonstrates structured database design, reusable Django app components, and a responsive, user-friendly front-end interface for procurement data exploration.

##🌟 Features

Advanced Search — Filter NASPO items by product name, supplier, contract number, or price range.

Pagination — Seamless navigation across large contract datasets.

PostgreSQL Integration — Structured schema supporting efficient queries.

Responsive UI — Optimized for both desktop and mobile views.

Modular Architecture — Easily extendable for new data sources or visualization modules.

##🧩 Project Structure

```text
Django_NASPO_price_search/
│
├── provider_search/                   → Main project configuration (settings, urls, wsgi)
│
├── catalog_app/                       → Core app handling NASPO contract search
│   ├── models.py                      → Defines NASPO contract and item models
│   ├── views.py                       → Query handling, pagination, and rendering logic
│   ├── urls.py                        → URL routing for catalog endpoints
│   └── templates/catalog_app/         → HTML templates (base.html, search.html)
│
├── catalog/                           → Optional secondary app for legacy references
│   ├── admin.py, views.py, models.py
│
├── templates/                         → Shared templates for UI rendering
│   └── catalog_app/search.html
│
├── scripts/                           → Utility scripts for data ingestion
│   └── load_naspo.py
│
├── static/                            → Static assets (CSS, JS, images)
├── manage.py                          → Django management entry point
└── requirements.txt                   → Python dependencies
```

##⚙️ Installation Guide
1️⃣ Clone the repository
git clone https://github.com/yvonnehan777/Django_NASPO_price_search.git  
cd Django_NASPO_price_search

2️⃣ Create a virtual environment
python3 -m venv venv  
source venv/bin/activate   # macOS/Linux  
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure the database

In your settings.py, update the DATABASES section:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'naspo_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5️⃣ Run migrations
python manage.py migrate

6️⃣ Start the development server
python manage.py runserver

Then visit 👉 http://127.0.0.1:8000/ in your browser 🚀

Notes:

Data can be loaded via the script in scripts/load_naspo.py.

Pagination, search filters, and database optimization are defined in views.py.

.gitignore excludes venv/, db.sqlite3, cache, and build files for cleaner version control.
