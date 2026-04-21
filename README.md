# Code Review Dashboard

A Flask-based web application for submitting and tracking code review issues, severity levels, and suggested fixes. Built as part of an IT Support & Cybersecurity portfolio.

---

## Features

- Submit code snippets for peer review
- Log issues with severity levels (Low / Medium / High)
- Suggest fixes for identified issues
- View all submitted reviews on a live dashboard

---

## Tech Stack

| Layer    | Technology     |
|----------|---------------|
| Backend  | Python, Flask  |
| Frontend | HTML, CSS      |
| Server   | Gunicorn       |

---

## Project Structure

```
code-review-dashboard/
├── app.py               # Flask application logic
├── requirements.txt     # Project dependencies
└── templates/
    └── index.html       # Dashboard UI
```

---

## Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Bwalkzz31/code-review-dashboard.git

# Navigate into the project folder
cd code-review-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000
```

---

## Author

**Britany Walker**
IT Support & Cybersecurity Professional
- GitHub: [@Bwalkzz31](https://github.com/Bwalkzz31)
- Email: b.walker.itm@gmail.com

---

*Built to demonstrate backend logic, form handling, and dynamic data display using Python and Flask.*
