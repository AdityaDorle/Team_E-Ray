
# Project Setup Guide

This guide will walk you through setting up and running the Interactive Water Quality Dashboard for Lakes in Germany.

## Prerequisites

- Python 3.x
- PostgreSQL database

## Steps

1. **Clone the repository:**

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```
4. **Set up the database:**

   - Install PostgreSQL if not already installed.
   - Create a new database and user with the necessary permissions.
   - Update the database connection settings in `serve.py` if needed.
5. **Populate the database with lake data:**

   - Add your lake data to the PostgreSQL database.
6. **Run the Flask server:**

   ```sh
   python serve.py
   ```
7. **Access the application:**

   - Open your browser and navigate to `http://localhost:5000/`.

## Folder Structure

- `static/`: Contains all static files like HTML, CSS, and JavaScript.
- `serve.py`: The main Flask application file.
- `requirements.txt`: Lists all dependencies.
- `README.md`: The main project readme file.
- `SETUP.md`: This setup guide.
- `CODE_DESCRIPTION.md`: Description of the code and its components.

## Troubleshooting

If you encounter any issues, check the following:

- Ensure the database is running and accessible.
- Verify the database connection settings in `serve.py`.
- Check the browser console for any errors.
