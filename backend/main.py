from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title='Recursion Visualizer API')

# ---Paths---
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

# ---Static Files---
app.mount("/static",StaticFiles(directory=FRONTEND_DIR), name="static")

# ---Serve Static---
@app.get("/", response_class=HTMLResponse)
def serveLandingPage():
    htmlPage = FRONTEND_DIR / "landing-page.html"
    return htmlPage.read_text()
    