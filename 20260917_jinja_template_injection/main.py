from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from jinja2 import Template

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class User:
    def __init__(self):
        self.name   : str = "Alice"
        self.secret : str = "Alice's Secret"

user = User()

# @app.get("/")
# def home(name: str):
#     global user
#     template = Template(f"""
#     <html>
#       <body>
#         Hello {name}
#       </body>
#     </html>                    
#     """)
#     return HTMLResponse(template.render())

@app.get("/")
def home(name: str):
    template = Template(name)
    return HTMLResponse(template.render(user=user))
