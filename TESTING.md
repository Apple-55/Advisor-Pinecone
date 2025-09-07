# Testing Guide

This document describes how to test the FastAPI project locally.

## 1. Activate the virtual environment

```powershell
cd C:\Projects\Advisor-Pinecone
.\.venv\Scripts\activate
```

## 2. Install dependencies

Make sure you have the latest requirements (including `requests`):

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements_clean.txt
```

## 3. Run the FastAPI server

In one PowerShell window:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## 4. Test endpoints manually

Open these in your browser:

- Root: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Health: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)
- Config: [http://127.0.0.1:8000/config](http://127.0.0.1:8000/config)
- Settings: [http://127.0.0.1:8000/settings](http://127.0.0.1:8000/settings)
- Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 5. Test endpoints with the script

In a second PowerShell window:

```powershell
cd C:\Projects\Advisor-Pinecone
.\.venv\Scripts\python.exe test_endpoints.py
```

Optional: specify a custom base URL:

```powershell
.\.venv\Scripts\python.exe test_endpoints.py --base http://127.0.0.1:8000
```

If all endpoints return valid responses, your environment is working correctly.
