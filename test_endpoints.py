
# Single-terminal FastAPI integration test.
# - Starts Uvicorn in the background via sys.executable
# - Waits for readiness on /health
# - Checks /, /health, /config, /settings
# - Prints a summary and exits 0 on success, 1 on failure
# - Shuts the server down cleanly
#
# Usage (PowerShell):
#   .\.venv\Scripts\python.exe test_endpoints.py
#   .\.venv\Scripts\python.exe test_endpoints.py --host 127.0.0.1 --port 8000 --module main:app

import argparse
import json
import subprocess
import sys
import time
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

def get_json(url: str):
    req = Request(url, headers={"Accept": "application/json"})
    with urlopen(req, timeout=5) as resp:
        return json.loads(resp.read().decode("utf-8"))

def wait_for_ready(base: str, timeout: float = 25.0) -> bool:
    url = f"{base}/health"
    start = time.time()
    while time.time() - start < timeout:
        try:
            _ = get_json(url)
            return True
        except Exception:
            time.sleep(0.5)
    return False

def run_checks(base: str):
    failures = []
    cases = [
        ("/", lambda d: "message" in d, "missing 'message'"),
        ("/health", lambda d: d.get("status") == "ok", "status != 'ok'"),
        ("/config", lambda d: all(k in d for k in ("env", "api_key_set")), "missing keys"),
        ("/settings", lambda d: all(k in d for k in ("env", "api_key_present")), "missing keys"),
    ]

    for path, predicate, desc in cases:
        url = f"{base}{path}"
        try:
            data = get_json(url)
            ok = predicate(data)
            print(f"[OK ] {path}: {data}" if ok else f"[FAIL] {path}: {data} -- {desc}")
            if not ok:
                failures.append(path)
        except HTTPError as e:
            print(f"[FAIL] {path}: HTTP {e.code}")
            failures.append(path)
        except URLError as e:
            print(f"[FAIL] {path}: {e.reason}")
            failures.append(path)
        except Exception as e:
            print(f"[FAIL] {path}: {e}")
            failures.append(path)
    return failures

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", default="8000")
    p.add_argument("--module", default="main:app", help="ASGI module, e.g. main:app")
    args = p.parse_args()

    base = f"http://{args.host}:{args.port}"
    cmd = [sys.executable, "-m", "uvicorn", args.module, "--host", args.host, "--port", str(args.port)]
    print("Starting:", " ".join(cmd))
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    try:
        if not wait_for_ready(base):
            # show a bit of server output for debugging
            try:
                out = proc.stdout.read(2000)
                if out:
                    print(out)
            except Exception:
                pass
            print("Server did not become ready in time.")
            proc.terminate()
            proc.wait(timeout=10)
            sys.exit(1)

        failures = run_checks(base)
        code = 0 if not failures else 1
        print("Summary:", "ALL PASS" if code == 0 else f"FAIL: {', '.join(failures)}")
        sys.exit(code)
    finally:
        try:
            proc.terminate()
            proc.wait(timeout=10)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass

if __name__ == "__main__":
    main()
