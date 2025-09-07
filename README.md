# Advisor-Pinecone

![CI](https://github.com/<your-username>/Advisor-Pinecone/actions/workflows/ci.yml/badge.svg)

A FastAPI project for experimentation and development.

## Setup

Create and activate a virtual environment:

```powershell
cd C:\Projects\Advisor-Pinecone
python -m venv .venv
.\.venv\Scripts\activate
```

Install dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
.\.venv\Scripts\pip.exe install -r requirements_clean.txt
```

## Running the App

Start the FastAPI app with:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) for the root response.

Interactive API docs are at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Testing Endpoints

### Manual Testing
Open in browser:
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
- [http://127.0.0.1:8000/config](http://127.0.0.1:8000/config)
- [http://127.0.0.1:8000/settings](http://127.0.0.1:8000/settings)
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Automated Testing

With server started in one terminal:

```powershell
.\.venv\Scripts\python.exe test_endpoints.py
```

Or run autorun test (spins server, checks endpoints, shuts down):

```powershell
.\.venv\Scripts\python.exe test_endpoints.py
```

## Endpoints

- `GET /` – Root message
- `GET /health` – Health check
- `GET /config` – Displays environment info
- `GET /settings` – Reads settings from `.env`
