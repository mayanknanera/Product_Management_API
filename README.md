# 🛒 Product Management API

> A REST API built with **Django** & **Django REST Framework** for managing products with full CRUD and token-based authentication.

---

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| Framework | ![Django](https://img.shields.io/badge/Django-6.0.1-green) |
| API | ![DRF](https://img.shields.io/badge/DRF-3.17.1-red) |
| Auth | Token Authentication |
| Database | SQLite |

---

## 🔐 Authentication

All endpoints require a token in the request header.

```
Authorization: Token <your_token>
```

### Obtain Token

**`POST`** `/drf/token/`

```json
{ "username": "your_username", "password": "your_password" }
```

---

## 📦 API Endpoints

### Base URL

```
http://127.0.0.1:8000/drf/
```

| Method | URL | Description |
|---|---|---|
| `GET` | `/products/` | List all products |
| `POST` | `/products/` | Create a new product |
| `PUT` | `/products/<id>/` | Full update a product |
| `PATCH` | `/products/<id>/` | Partial update a product |
| `DELETE` | `/products/<id>/` | Delete a product |

> Paginated — default page size is **5**. Use `?page=2` to navigate.

---

## ✅ Validation Rules

| Field | Rule |
|---|---|
| `price` | Must be **greater than 0** |
| `stock` | Cannot be **negative** |
| `name` | Auto-converted to **UPPERCASE** on create |
