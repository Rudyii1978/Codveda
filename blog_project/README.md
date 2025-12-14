# Django Blog Application

A fully functional Django web application featuring user authentication and blog functionality. Users can register, login, reset passwords, and manage blog posts.

## Features

### User Authentication
- User registration with validation
- Login/Logout functionality
- Password reset via email (console backend for development)
- User-specific permissions

### Blog Functionality
- Create, read, update, and delete blog posts
- User can only edit/delete their own posts
- Rich text content support
- Automatic slug generation from post titles
- Draft and published post status
- Pagination for post listing
- Timestamp tracking (created and updated dates)

### Admin Interface
- Django admin panel for site management
- Post management with filtering and search
- User management

## Requirements

- Python 3.6 or higher
- Django 6.0

## Installation

1. Navigate to the blog_project directory:
   ```bash
   cd blog_project
   ```

2. Install Django (if not already installed):
   ```bash
   pip install django
   ```

3. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your web browser and navigate to:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### For Regular Users

1. **Register**: Click "Register" in the navigation menu to create a new account
2. **Login**: Use your credentials to log in
3. **Create Posts**: Once logged in, click "New Post" to create a blog post
4. **View Posts**: Browse all posts on the "All Posts" page
5. **Edit/Delete Posts**: You can edit or delete your own posts from the post detail page
6. **Password Reset**: Click "Forgot your password?" on the login page to reset your password

### For Administrators

1. Log in to the admin panel at http://127.0.0.1:8000/admin/
2. Manage users, posts, and site settings
3. View and moderate all content

## Project Structure

```
blog_project/
├── blog/                      # Blog application
│   ├── migrations/           # Database migrations
│   ├── models.py            # Post model
│   ├── views.py             # Blog views
│   ├── urls.py              # Blog URLs
│   └── admin.py             # Admin configuration
├── accounts/                 # Authentication application
│   ├── views.py             # Authentication views
│   └── urls.py              # Authentication URLs
├── blog_project/            # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── home.html           # Home page
│   ├── blog/               # Blog templates
│   └── accounts/           # Authentication templates
└── manage.py               # Django management script
```

## Default Credentials

A superuser has been created for testing:
- Username: `admin`
- Password: `admin123`

**Note**: Change these credentials in production!

## Development Settings

The project is configured for development with:
- SQLite database
- DEBUG mode enabled
- Console email backend (password reset emails appear in terminal)
- Secret key for development (change for production)

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in settings.py
2. Generate a new `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Set up a production database (PostgreSQL, MySQL, etc.)
5. Configure a proper email backend for password reset
6. Collect static files: `python manage.py collectstatic`
7. Use a production-ready web server (Gunicorn, uWSGI)
8. Set up HTTPS

## Testing the Application

1. Start the development server
2. Navigate to http://127.0.0.1:8000/
3. Register a new user account
4. Create a blog post
5. View and edit your posts
6. Test the password reset functionality
7. Log in to the admin panel to see the admin interface

## Troubleshooting

**Issue**: "no such table" error
- **Solution**: Run `python manage.py migrate`

**Issue**: Static files not loading
- **Solution**: Ensure `DEBUG = True` for development, or run `collectstatic` for production

**Issue**: Cannot access admin panel
- **Solution**: Create a superuser with `python manage.py createsuperuser`

## License

This project is created for educational purposes as part of the Codveda internship tasks.
