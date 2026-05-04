# Product Management API

A small Django REST Framework project for managing products with a simple API.

## Overview

This project provides a `Product` model with:

- `name` (string)
- `price` (integer)

The API supports listing products and creating new products via the `/drf/products/` endpoint.

## Features

- Django 6.0.1
- Django REST Framework 3.17.1
- `ListCreateAPIView` for product listing and creation
- Validation ensures `price` is positive
- Product names are converted to uppercase on creation
- SQLite database included by default (`db.sqlite3`)

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

## Running locally

```bash
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` and use the API endpoints below.

## API Endpoints

- `GET /drf/products/` - list all products
- `POST /drf/products/` - create a new product

### Sample request body for creating a product

```json
{
  "name": "Keyboard",
  "price": 150
}
```

### Validation

- `price` must be greater than zero
- `name` is stored as uppercase when created

## Optional endpoints

- `POST /drf/token/` - obtain auth token (DRF token authentication endpoint included)

## Project structure

- `config/` - Django project settings and URL configuration
- `drf/` - main application with models, views, serializers, and URLs
- `db.sqlite3` - SQLite database file
- `requirements.txt` - project dependencies

## Notes

- The current API implementation uses `ListCreateAPIView` for product listing and creation.
- Additional functionality such as detail, update, and delete endpoints are present in commented code within `drf/views.py` for future expansion.
