from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from response import Response

app = FastAPI()
res = Response()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return res.return_index_html()

@app.get("/icons/{icon_type}/{icon_name}")
def get_icon(icon_type: str, icon_name: str):
    try:
        return res.return_icon(icon_type=icon_type, icon_name=icon_name)
    except:
        raise res.return_not_found()