# Resource Portal 📚

A **Django-based Resource Portal** designed for students and educators to manage, upload, and access academic resources in a clean and structured way.

This project focuses on **core backend fundamentals, authentication, role-based access, and real-world workflows**, rather than flashy features — making it highly suitable for **placements and interviews**.

---

## 🚀 Features

* 🔐 User Authentication (Register / Login / Logout)
* 👨‍🎓 Student & 👨‍🏫 Admin (Teacher) role separation
* 🧑‍🏫 Admin-only upload access
* 📂 Organized resource management
* 🖼️ Static & media file handling
* 🗄️ SQLite database for development
* 🧼 Clean project structure following Django best practices

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Django Templates
* **Database:** SQLite
* **Version Control:** Git & GitHub

---

## 📁 Project Structure

```
resourcePortal/
│── manage.py
│── db.sqlite3
│
├── resourcePortal/   # Main project settings
├── users/            # Authentication & user logic
├── templates/        # HTML templates
├── static/           # Static files (CSS, JS)
├── media/            # Uploaded resources
```

---

## 🔑 Role-Based Access Logic

* Students can:

  * Register and log in
  * View available resources

* Admins (Teachers) can:

  * Log in with admin privileges
  * Upload and manage resources
  * Access admin-specific UI elements

*(Future-ready logic for `is_admin` session-based access control)*

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/TarushBajpai/resource-portal.git

# Move into the project directory
cd resource-portal

# Run the server
python manage.py runserver
```

Open browser at:

```
http://127.0.0.1:8000/
```

---

## 🎯 Learning Outcomes

* Hands-on Django project structure understanding
* Authentication and authorization workflow
* Static & media file configuration
* Git & GitHub real-world usage
* Backend-first project thinking

---

## 🔮 Future Improvements

* Admin dashboard UI
* Search & filter resources
* File type restrictions
* Deployment (Render / Railway)
* REST API integration

---

## 👤 Author

**Tarush Bajpai**
3rd Year Computer Science Student
Actively learning Django, Python, and Backend Development

GitHub: [https://github.com/TarushBajpai](https://github.com/TarushBajpai)

---

⭐ If you find this project helpful, consider giving it a star!
