from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from api_factorial import router as factorial_router

app = FastAPI(title='Recursion Visualizer API')

# ---Paths---
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

# --- check before mount ---
if (not FRONTEND_DIR.exists()):
    raise RuntimeError(f"Front End directory not found: {FRONTEND_DIR}")

# ---Static Files---
app.mount("/static",StaticFiles(directory=str(FRONTEND_DIR)), name="static")

# --- Factorial ---
app.include_router(factorial_router, prefix='/api')

# ---Serve Static---
@app.get("/", response_class=HTMLResponse)
def serveLandingPage():
    htmlPage = FRONTEND_DIR / "landing-page.html"
    return htmlPage.read_text()


    