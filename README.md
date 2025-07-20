# 🍽️ Restaurant Management System – Django Project

This is a simple restaurant management website built using Django (Python) and SQLite. The project includes features such as a homepage, menu, order form, and static content pages like About and Feast.

---

## 📌 Features

- Menu page to display food items
- Order page with form submission
- About and Feast info pages
- Static HTML templates with routing
- Admin panel with authentication
- SQLite database (default Django DB)
- Ready for deployment on Render

---

## 🔧 Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Django (Python)
- **Database:** SQLite (Django default)
- **Deployment:** GitHub + Render

---

## 🛠️ How to Run the Project Locally

```bash
git clone https://github.com/cj7-code-journey/Restaurant-Management-System.git
cd Restaurant-Management-System

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env

# Run migrations and start server
python manage.py migrate
python manage.py runserver
