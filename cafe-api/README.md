# ☕ Café API – RESTful Flask + SQLAlchemy Project

> 📘 RESTful Flask API with SQLAlchemy, SQLite, and Postman Documentation

---

## 1️⃣ Overview
A **RESTful API** built with **Flask** and **SQLAlchemy (ORM)** that manages a database of cafés.  
It demonstrates complete **CRUD functionality** — including **Create (POST)**, **Read (GET)**, **Update (PATCH)**, and **Delete (DELETE)** —  
plus **API key authentication** and **Postman documentation** for all endpoints.

🔗 **Live API Documentation:**  
👉 [View on Postman](https://documenter.getpostman.com/view/49384606/2sB3QQKo88)

---

## 2️⃣ Tech Stack
| Category | Technology |
|-----------|-------------|
| Language | Python 3.11+ |
| Framework | Flask |
| ORM / DB | SQLAlchemy + SQLite |
| API Testing | Postman |
| Security | dotenv (Environment Variables) |
| Serialization | JSON (Custom `to_dict()` method) |

---

## 3️⃣ Features

| Method | Endpoint | Description |
|--------|-----------|-------------|
| `GET` | `/random` | Fetch a random café |
| `GET` | `/all` | Get all cafés from the database |
| `GET` | `/search?loc=LOCATION` | Search cafés by location |
| `POST` | `/add` | Add a new café (form data) |
| `PATCH` | `/update-price/<id>?new_price=PRICE` | Update a café’s coffee price |
| `DELETE` | `/report-closed/<id>?api_key=SECRET_KEY` | Delete a café (requires API key) |

---

## 4️⃣ Database Schema

| Column | Type | Description |
|---------|------|-------------|
| `id` | Integer (PK) | Unique café ID |
| `name` | String | Café name |
| `map_url` | String | Google Maps URL |
| `img_url` | String | Image URL |
| `location` | String | City or area |
| `seats` | String | Seating info |
| `has_toilet` | Boolean | Whether café has a toilet |
| `has_wifi` | Boolean | Whether café has Wi-Fi |
| `has_sockets` | Boolean | Whether café has plug sockets |
| `can_take_calls` | Boolean | Whether phone calls are allowed |
| `coffee_price` | String | Price string (e.g. "£3.50") |

---

## 5️⃣ Authentication
Certain routes (like DELETE) are protected by an **API key** stored in the `.env` file.

**Example `.env`:**
API_KEY=TopSecretAPIKey


You can send the API key:
- As a **query parameter** → `?api_key=TopSecretAPIKey`  
- Or via **header** → `X-API-KEY: TopSecretAPIKey`

---

## 6️⃣ Example Requests

### 🟢 PATCH (Update price)
PATCH /update-price/3?new_price=€4.50

css

**Response:**
```json
{
  "response": {
    "success": "Successfully updated the cafe."
  }
}
🔴 DELETE (Protected)

DELETE /report-closed/3?api_key=TopSecretAPIKey
Response:

json

{
  "response": {
    "success": "Successfully removed the cafe."
  }
}
7️⃣ Setup Instructions
Clone the repository and install dependencies:


git  https://github.com/Miss-Layla/Cafe-Wifi
cd cafe-api
pip install -r requirements_3.13.txt
Run the app locally:


python main.py
Access in your browser:


http://127.0.0.1:5000/
8️⃣ Project Structure

📦 cafe-api
├── 📂 instance/
│   └── cafes.db                # SQLite database (auto-created by Flask)
├── 📂 templates/
│   └── index.html              # Basic homepage for Flask route "/"
├── 📄 .env                     # Stores API_KEY (excluded via .gitignore)
├── 📄 main.py                  # Main Flask application
├── 📄 README.md                # Project documentation (this file)
├── 📄 requirements_3.13.txt    # Python dependencies
└── 📂 External Libraries       # Managed by PyCharm virtual environment
9️⃣ Postman Documentation
All endpoints are documented, parameterized, and testable via Postman.

🔗 View Documentation:
https://documenter.getpostman.com/view/49384606/2sB3QQKo88

🔟 Learning Goals
Building RESTful APIs with Flask

Managing relational data using SQLAlchemy ORM

Implementing full CRUD functionality (POST, GET, PATCH, DELETE)

Securing routes with environment variables (dotenv)

Testing endpoints using Postman

Writing clean and modular backend code

🏷️ Tags
#flask #sqlalchemy #sqlite #python #restfulapi #sql #crud #postman

👩‍💻 Created by Lea

Passionate about Python, automation, and smart APIs.







