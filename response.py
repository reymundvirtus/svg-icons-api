from fastapi import HTTPException
from fastapi.responses import FileResponse
import os

class Response:
    def __init__(self):
        self.NEUTRAL_ICON_FOLDER = "assets/icons/neutral"
        self.LIGHT_ICON_FOLDER = "assets/icons/light"
        self.DARK_ICON_FOLDER = "assets/icons/dark"
        self.WORDMARK_ICON_FOLDER = "assets/wordmark"

    def return_index_html(self):
        return FileResponse("index.html", media_type="text/html")

    def return_icon(self, icon_type, icon_name):
        if icon_type == "neutral":
            icon_path = os.path.join(self.NEUTRAL_ICON_FOLDER, f"{icon_name}.svg")
            return self.check_if_isfile(icon_path)
        elif icon_type == "light":
            icon_path = os.path.join(self.LIGHT_ICON_FOLDER, f"{icon_name}.svg")
            return self.check_if_isfile(icon_path)
        elif icon_type == "dark":
            icon_path = os.path.join(self.DARK_ICON_FOLDER, f"{icon_name}.svg")
            return self.check_if_isfile(icon_path)

        raise self.return_not_found()

    def check_if_isfile(self, icon_path):
        if os.path.isfile(icon_path):
            return FileResponse(icon_path, media_type="image/svg+xml")

        raise self.return_not_found()

    def return_not_found(self):
        return HTTPException(status_code=404, detail="Icon not found")