from fastapi import FastAPI
from fastapi.responses import FileResponse
from response import Response
import os

app = FastAPI()
res = Response()

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

    raise res.return_not_found()

@app.get("/icons/light-variant/{icon_name}")
def get_light_icon(icon_name: str):
    icon_path = os.path.join(LIGHT_ICON_FOLDER, f"{icon_name}.svg")

    if os.path.isfile(icon_path):
        return FileResponse(icon_path, media_type="image/svg+xml")

    raise res.return_not_found()

@app.get("/icons/dark-variant/{icon_name}")
def get_dark_icon(icon_name: str):
    icon_path = os.path.join(DARK_ICON_FOLDER, f"{icon_name}.svg")

    if os.path.isfile(icon_path):
        return FileResponse(icon_path, media_type="image/svg+xml")

    raise res.return_not_found()