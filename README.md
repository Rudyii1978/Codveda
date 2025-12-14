# Codveda Internship Tasks

This repository contains three separate projects developed as part of the Codveda internship program.

## Projects

### 1. Simple Calculator
A basic calculator that can perform four primary arithmetic operations.

**Location**: `simple_calculator/`

**Features**:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Interactive command-line interface
- Error handling for invalid inputs and division by zero

**Usage**:
```bash
cd simple_calculator
python calculator.py
```

See [simple_calculator/README.md](simple_calculator/README.md) for detailed instructions.

---

### 2. API Integration
A Python script that interacts with an external API to fetch and display data.

**Location**: `api_integration/`

**Features**:
- Fetch posts from JSONPlaceholder API
- View post details
- Display user information
- View comments for posts
- Interactive command-line interface
- Error handling for network issues

**Usage**:
```bash
cd api_integration
python api_client.py
```

See [api_integration/README.md](api_integration/README.md) for detailed instructions.

---

### 3. Django Blog Application
A fully functional web application using Django that includes user authentication and blog functionality.

**Location**: `blog_project/`

**Features**:
- User registration, login, and logout
- Password reset functionality
- Create, read, update, and delete blog posts
- User-specific post management
- Admin interface
- Responsive design

**Setup**:
```bash
cd blog_project
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

See [blog_project/README.md](blog_project/README.md) for detailed instructions.

---

## Requirements

- Python 3.6 or higher
- For the Django project: Django 6.0 (install via `pip install -r blog_project/requirements.txt`)

## Project Structure

```
Codveda/
├── simple_calculator/          # Project 1: Basic Calculator
│   ├── calculator.py
│   └── README.md
├── api_integration/           # Project 2: API Integration
│   ├── api_client.py
│   └── README.md
├── blog_project/              # Project 3: Django Blog
│   ├── blog/                  # Blog app
│   ├── accounts/              # Authentication app
│   ├── templates/             # HTML templates
│   ├── manage.py
│   ├── requirements.txt
│   └── README.md
└── README.md                  # This file
```

## Getting Started

Each project is self-contained in its own directory with its own README file containing specific setup and usage instructions. Navigate to the project directory you want to explore and follow the instructions in its README.

## License

This project is created for educational purposes as part of the Codveda internship program.

