from flask import Flask, request

app = Flask(__name__)

# 가상의 DB 테이블  
VIRTUAL_API_KEY_TABLE = {
    "SAM" : "INTERNAL-1234567",
    "TOM" : "INTERNAL-3334567",
    "ANN" : "INTERNAL-2684578",
}

# 가상의 방화벽
VIRTUAL_FIREWALL = { "127.0.0.1" }

@app.get("/")
def index():
    '''인덱스 페이지'''
    return "Internal Server"

@app.get("/secret_key")
def get_secret_key() -> str:
    '''내부 직원들 대상으로 API KEY를 조회하는 API'''
    
    user_id = request.args.get("user_id", '')
    
    if request.remote_addr in VIRTUAL_FIREWALL:
        return VIRTUAL_API_KEY_TABLE.get(user_id, 'None')
    else:
        raise PermissionError("허가받지 않은 요청자입니다.")

app.run(host="127.0.0.1", port=9000)
