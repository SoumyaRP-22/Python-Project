# *****************************************************************************************************************************
#                                                📘 Silicon Campus Hub – Documentation
# *****************************************************************************************************************************

**Project Name**:Silicon Campus Hub\
**Main Modules**: User + Announcements System + Lost & Found System

---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------

## 👤 1. Author

| Name                   | College ID | Email                        |
|------------------------|------------|------------------------------|
| Soumya Ranjan Pradhan  | 24BCSG84   | cse.24bcsg84@silicon.ac.in   |

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

## 📌 2. Project Overview

**Silicon Campus Hub** is a modular web application built using **FastAPI**. It provides:

- 👥 **User Management** – Secure registration and login via JWT.
- 📢 **Announcements** – Admins can post and delete updates; students can read them.
- 🧳 **Lost & Found** – A portal for students to report or claim lost items.

## What Has Been Done and How It Was Done

I built a backend web application using **FastAPI**. This system allows users to log in, view/post announcements, and create or search lost & found items. The project was divided into separate modules, all of which I implemented.

Below is the breakdown of the features that I built and how they were done:

### 🔍 Lost & Found Module

This module allows users to:

    📌Post a lost/found item (admin only)
    📌Get the list of all lost/found items
    📌View a specific lost/found item by its ID
    📌Delete an item (admin only)

#### 💡 How It Was Implemented:

🟡 Created a SQLAlchemy model `LostFoundItem` with fields like `id`, `title`, `description`, `is_found`, `created_by`.  
🟡 Created corresponding Pydantic schemas to handle API input/output.  
🟡 Used FastAPI's `APIRouter` to define routes like:  

  * `GET /lost-found`
  * `GET /lost-found/{id}`
  * `POST /admin/lost_found`
  * `DELETE /admin/{item_id}/delete`  

🟡 Used JWT token and `require_admin` function to restrict access for admin-only routes.  
🟡 Database session managed with dependency injection using `Depends(get_db)`.  

### 📢 Announcement Module

 This module allows:

    📌Students to view all announcements.  
    📌Admins to create new announcements.  
    📌Admins to delete any announcement.    
    📌View a specific announcement by ID.  

#### 💡 How It Was Implemented:

🟡 Created a SQLAlchemy model `Announcement` with fields like `id`, `title`, `content`, `created_by`, and `created_at`.  
🟡 Used schemas `announcementCreate` and `announcementOut` for data validation.  
🟡 Built routes using FastAPI decorators for:  

  * Listing all announcements
  * Posting new ones
  * Viewing one by ID
  * Deleting by ID

### 👥 User Authentication

🟡 Register and login using `/register` and `/login`  
🟡 Passwords are hashed using `passlib` and `bcrypt`  
🟡 JWT tokens are created and returned to users on login  
🟡 Admin vs reader roles are checked using custom logic (`require_admin`)  

## ⚙️ Technologies Used

✅**FastAPI**
✅**Python 3.11**
✅**SQLAlchemy**
✅**Pydantic**
✅**SQLite**
✅**VS Code**
✅**GitHub**

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

## 🚀 How to Run the Project

bash
# Clone the repository
git clone <project-url>
cd <file-name>

# Create virtual environment
python -m venv venv
venv\Scripts\activate       # On Linux/Mac: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload

Then go to: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** to use Swagger UI and test the APIs.

