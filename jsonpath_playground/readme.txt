
## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/jsonpath_playground.git
   cd jsonpath_playground

2.Create and activate a virtual environment (optional but recommended):

    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

    pip install -r requirements.txt

* Local run:
    python manage.py migrate
    python manage.py runserver

**Docker Setup
    This project includes a Dockerfile.

    docker build -t jsonpath_playground .

    docker run -d -p 8000:8000 jsonpath_playground

    Now, the application will be accessible at http://localhost:8000.

    -------------------------------------------
    In the Dockerfile, Gunicorn is used as the WSGI server to serve the Django application:

    CMD ["gunicorn", "jsonpath_playground.wsgi:application", "--bind", "0.0.0.0:8000"]