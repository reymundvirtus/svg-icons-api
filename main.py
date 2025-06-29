from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI()

NEUTRAL_ICON_FOLDER = "assets/icons/neutral"
LIGHT_ICON_FOLDER = "assets/icons/light"
DARK_ICON_FOLDER = "assets/icons/dark"

WORDMARK_ICON_FOLDER = "assets/wordmark"

@app.get("/")
def read_root():
    return { "Hello": "World!" }

@app.get("/icons/neutral/{icon_name}")
def get_neutral_icon(icon_name: str):
    icon_path = os.path.join(NEUTRAL_ICON_FOLDER, f"{icon_name}.svg")

    if os.path.isfile(icon_path):
        return FileResponse(icon_path, media_type="image/svg+xml")

    raise HTTPException(status_code=404, detail="Icon not found")
