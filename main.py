from fastapi import FastAPI, Request
from urllib3 import request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models import User

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request=request, name='index.html', context={"id": id}
    )


