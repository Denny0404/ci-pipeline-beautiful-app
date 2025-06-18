
# 📘 Mid-Term Practical Assignment: CI/CD Pipeline with GitHub Actions

## 🎯 Assignment Objective

This project is developed as part of the **Mid-Term Practical** to demonstrate a full implementation of a **CI/CD pipeline** using **GitHub Actions**, along with **Docker containerization** and **multi-environment deployment support**. It includes stages for **build, linting, testing, artifact/image upload**, and supports both **dev** and **prod** environments.

---

## 🧩 Project Overview

This is a **Flask web application** that serves a styled landing page using **Bootstrap** and custom CSS. It includes:
- Flask app with a root route `/`
- Beautiful UI rendered via Jinja2 template (`index.html`)
- Custom styling through `style.css`
- Docker support
- GitHub Actions workflow

---

## 📁 Folder Structure

```
ci-pipeline-beautiful-app/
├── app.py                     # Main Flask app
├── test_app.py                # Unit tests (4)
├── Dockerfile                 # Docker container config
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignore Python/IDE files
├── README.md                  # Assignment report and documentation
├── templates/
│   └── index.html             # Frontend HTML (Bootstrap UI)
├── static/
│   └── style.css              # Custom CSS styling
└── .github/
    └── workflows/
        └── ci.yml             # GitHub Actions CI config
```

---

## 🛠️ Setup & Running (Offline)

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

---

## ✅ Unit Testing

### Run Tests

```bash
pytest
```

### Included Tests (4 Total)
- `test_home_status`: Check `/` returns HTTP 200
- `test_home_content`: Checks if homepage contains expected message
- `test_home_route_exists`: Confirms route is reachable
- `test_home_returns_string`: Ensures response type is correct

---

## 🐳 Docker Integration

### Build Docker Image

```bash
docker build -t flask-ci-app .
```

### Run Locally

```bash
docker run -p 5050:5000 flask-ci-app
```

Visit: `http://localhost:5050`

---

## 📦 GitHub Container Registry (GHCR)

### Push Image to GHCR

```bash
docker build -t ghcr.io/denny0404/flask-ci-app:latest .
echo ghp_YOUR_TOKEN | docker login ghcr.io -u denny0404 --password-stdin
docker push ghcr.io/denny0404/flask-ci-app:latest
```

### Pull and Run Anywhere

```bash
docker pull ghcr.io/denny0404/flask-ci-app:latest
docker run -p 5050:5000 ghcr.io/denny0404/flask-ci-app:latest
```

---

## ⚙️ GitHub Actions CI Pipeline

### File: `.github/workflows/ci.yml`

#### Triggers:
- `develop`: automatic on push (dev environment)
- `main`: manual or merge trigger (prod environment)

#### Stages Implemented:
1. **Build**: install dependencies
2. **Lint**: use flake8
3. **Test**: run pytest for 4 test cases
4. **Docker Build**: tagged image with `dev` or `latest`
5. **Multi-environment Deploy**: branch-based logic

---

## 📸 Required Screenshots for Submission

- CI workflow passing (green check in GitHub Actions)
- Unit test success via terminal (`pytest`)
- Docker build success in terminal
- Running app via browser (`localhost:5050`)
- GHCR listing: [https://github.com/denny0404?tab=packages](https://github.com/denny0404?tab=packages)

---

## ✅ Submission Confirmation

- [x] Created a new GitHub repository (not reused from Labs/Assignments)
- [x] Implemented feature and develop branches
- [x] GitHub Actions CI pipeline with build, lint, test, Docker upload
- [x] At least 4 unit tests included and passed
- [x] Docker image pushed to GHCR
- [x] Multi-environment deployment setup (dev/prod)
- [x] README.md completed and submitted
- [x] Screenshots saved for grading

---

## 👨‍💻 Author
**Denish Akbari**  
PROG8860 – CI/CD Mid-Term Practical – June 2025
