# Django CSV Upload API

This project provides an API endpoint to upload a CSV file and save valid user data to the database. The data is validated for age range and duplicate emails before saving.

---

## 🔧 Features

- Upload `.csv` file containing `name`, `email`, and `age`.
- Automatically skips:
  - Duplicate emails (already existing in the database).
  - Invalid age entries (not between 0 and 120 or non-integer).
- Valid records are saved to the database.
- Skipped and error records are returned as response metadata.

---

📦 Installation

Clone the repository:

git clone https://github.com/yourusername/csv-upload-api.git
cd csv-upload-api

    Set up a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

    Run migrations:

python manage.py migrate

    Start the server:

python manage.py runserver
