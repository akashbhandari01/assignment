# Django User App

A simple Django application that connects to a MySQL database and provides routes to view, add, and view details of users.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/assignment.git
```
```bash
cd assignment
```

### 2. Environment Setup

```bash
    python -m venv myvenv
```
```bash
    venv\Scripts\activate       # Windows
```
```bash
    source venv/bin/activate    # Linux/macOS
```

### 2. Install pip

```bash
    pip install -r requirements.txt
```
### 4. Go To Project Folder

```bash
    cd Proj
```
### 5. Apply Migrations
```bash
    python manage.py makemigrations
    python manage.py migrate
```
### 6. Run The Project 
```bash
    python manage.py runserver
```