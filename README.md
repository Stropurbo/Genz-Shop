# 🧩 GenzShop Backend

This is the **backend** of **GenzShop**, a full-featured e-commerce platform powered by **Django** and **Django REST Framework**. It provides all the necessary APIs and admin functionality to support the frontend of the platform.

## 🚀 Key Features

- User registration, login, logout, and JWT authentication
- Product management with categories, price, and stock tracking
- Cart and wishlist functionality
- Order processing with status tracking
- Payment gateway integration (SSLCOMMERZ)
- Product search and filtering API
- Review and rating system
- Admin dashboard with Django admin
- RESTful API structure with proper permissions
- Media and static file handling via Cloudinary
- Swagger API documentation

## 🛠️ Tech Stack

- **Backend Framework:** Django
- **API:** Django REST Framework (DRF)
- **Authentication:** Djoser + JWT (Simple JWT)
- **Database:** PostgreSQL
- **Payments:** SSLCOMMERZ
- **Media Storage:** Cloudinary 
- **Documentation:** Swagger / Redoc via drf-yasg


## ⚙️ Setup & Installation

### Clone the repository

```bash
git clone https://github.com/Stropurbo/Genz-Shop.git
cd Genz-Shop

python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

