from flask import Flask, request
from urllib.request import urlopen
from urllib.parse import urlparse

DEFENCE_MODE = True

app = Flask(__name__)

# ALLOWED LIST
ALLOWED_HOSTS = {
    "example.com",
}

def validate_url(url:str):
    '''url 검사'''
    
    parsed = urlparse(url)
    
    if parsed.hostname not in ALLOWED_HOSTS:
        print(parsed.hostname)
        return False


@app.get("/")
def index():
    return 'Vulnerable Server Index'


@app.get("/fetch")
def fetch():
    '''url을 전달받아 대신 요청하는 API'''
    
    url = request.args.get("url")
    
    # url 검사. 허용 목록에 없으면 Block
    if (not validate_url(url)) and (DEFENCE_MODE) :
        return "Blocked", 403
    
    with urlopen(url, timeout=3) as response:
        result = response.read()
        print(result)
    
    return result

app.run(host="0.0.0.0", port=8000)
    