# Technology Stack Used in This Project

## Backend Framework
- **Django 5.2.7** - Python web framework
  - Django ORM for database operations
  - Django Templates for server-side rendering
  - Django Admin (available at /admin/)
  - Django Authentication system (django.contrib.auth)

## Database
- **SQLite3** - Default Django database (db.sqlite3)
  - Used for storing user registrations and dish items

## Frontend Technologies
- **HTML5** - Markup language
- **CSS3** - Styling
  - Bootstrap CSS (via static files and CDN)
  - Custom CSS files (style.css, responsive.css)
  - Font Awesome icons
- **JavaScript**
  - jQuery 3.4.1
  - Bootstrap JavaScript
  - Custom JavaScript (custom.js)
  - Isotope.js (for menu filtering)
  - Owl Carousel 2 (for sliders)
  - Google Maps API (for map integration)

## Python Libraries/Dependencies
- **Django** - Main web framework
- **Pillow** (implicit) - For handling image uploads (ImageField)

## Static Files Management
- Django Static Files Framework
- Media files handling (for uploaded images)
  - MEDIA_URL: /media/
  - MEDIA_ROOT: media/ directory

## Key Django Components Used

### Models
- `User_registration` - Custom user registration model
- `Dish` - Menu items model (name, description, image)

### Views
- Function-based views
- HTTP methods: GET, POST
- File upload handling (multipart/form-data)
- Redirects and messages framework

### URL Routing
- URL patterns with named routes
- Dynamic URL parameters (item_id)
- URL namespacing

### Templates
- Django Template Language (DTL)
- Template inheritance
- Static file loading (`{% load static %}`)
- CSRF protection

## Additional Features
- **Form Handling** - HTML forms with CSRF tokens
- **File Uploads** - Image uploads for dishes
- **Messages Framework** - Success/error messages
- **Authentication** - Custom login/registration system
- **CRUD Operations** - Create, Read, Update, Delete for dishes

## External Services/APIs
- **Google Maps API** - For location/map display
- **CDN Resources**:
  - Bootstrap 5.3.0 (CSS/JS)
  - jQuery Nice Select
  - Owl Carousel 2
  - Isotope Layout

## Development Tools
- **Python 3.13.3** - Programming language
- **Virtual Environment** (myenv) - Python environment isolation
- **Django Development Server** - Built-in server for development

## File Structure
```
myproject/
├── myapp/
│   ├── models.py (Database models)
│   ├── views.py (View functions)
│   ├── urls.py (URL routing)
│   ├── templates/ (HTML templates)
│   └── static/ (CSS, JS, images)
├── myproject/
│   ├── settings.py (Django settings)
│   └── urls.py (Main URL configuration)
└── db.sqlite3 (Database file)
```

## Security Features
- CSRF protection (built-in Django)
- SQL injection protection (Django ORM)
- XSS protection (template escaping)
- File upload validation

