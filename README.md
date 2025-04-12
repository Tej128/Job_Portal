# 💼 Job Portal Web Application

A full-featured Job Portal built using **Flask** and **SQLite**, designed with role-based access for Job Seekers and Employers. This web app allows users to post, apply, and manage job listings with a clean, responsive UI powered by Bootstrap.

---

## 🌟 Features

- 👤 **User Roles**  
  - Job Seekers: Register, browse jobs, apply to postings  
  - Employers: Register, post jobs, manage listings  
  - (Optional) Admin: Extendable for admin management of users/posts

- 🔐 **Secure Authentication**  
  - Role-based login system using **Flask-Login**  
  - Session handling and access protection

- 🧭 **Core Functionalities**
  - User registration and login
  - Job listing with filters (title, location, company)
  - Application tracking
  - Dashboards for different user roles

---

## 🧰 Tech Stack

| Layer     | Tools                            |
|-----------|----------------------------------|
| Backend   | Python, Flask, Flask-Login       |
| Frontend  | HTML, CSS, Bootstrap             |
| Database  | SQLite with SQLAlchemy ORM       |
| Auth      | Flask-Login                      |

---

## 🚀 Getting Started

### 🔧 Prerequisites
- Python 3.8+
- Virtualenv (recommended)

### ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/Tej128/Job_Portal.git
cd Job_Portal

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
