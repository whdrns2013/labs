# SSRF 실습

로컬 전용 내부 서비스와, 사용자가 전달한 URL을 대신 요청하는 서비스로 구성된 SSRF(Server-Side Request Forgery) 실습입니다. 취약 서버를 경유하면 외부에서 직접 접근할 수 없는 내부 서비스의 응답을 가져올 수 있는 상황을 재현합니다.

## 구성

| 서비스 | 바인딩 주소 | 역할 |
| --- | --- | --- |
| `internal_server/main.py` | `127.0.0.1:9000` | 내부망에서만 접근 가능한 API. `/secret_key?user_id=...`로 가상 API 키를 반환합니다. |
| `vulnerable_server/main.py` | `0.0.0.0:8000` | `/fetch?url=...`로 전달받은 URL을 서버 측에서 `urlopen`으로 요청합니다. |

내부 API는 요청 출발지가 `127.0.0.1`일 때만 응답하므로, 같은 컴퓨터에서 실행 중인 취약 서버가 요청하면 허용됩니다.

## 준비 및 실행

Python과 uv, Flask가 필요합니다. 터미널 두 개를 열고 uv로 각 프로젝트를 실행해줍니다.  

```powershell
# 터미널 1: 내부 서비스
cd internal_server
uv run main.py
```

```powershell
# 터미널 2: URL 요청 서비스
cd vulnerable_server
uv run main.py
```

정상 기동 여부는 각각 `http://127.0.0.1:9000/`, `http://127.0.0.1:8000/`에서 확인할 수 있습니다.

## 실습

현재 소스의 `DEFENCE_MODE`는 `True`라서 `/fetch` 요청은 차단됩니다. 취약 동작을 재현하려면 학습용 로컬 환경에서만 `vulnerable_server/main.py`의 `DEFENCE_MODE`를 `False`로 바꾼 뒤 취약 서버를 다시 시작합니다.

그 상태에서 아래 요청을 보내면, 클라이언트가 아니라 **8000번 포트의 서버**가 `127.0.0.1:9000`에 요청하고 그 응답을 그대로 돌려줍니다.

```powershell
curl.exe "http://127.0.0.1:8000/fetch?url=http%3A%2F%2F127.0.0.1%3A9000%2Fsecret_key%3Fuser_id%3DSAM"
```

예상 응답은 `INTERNAL-1234567`입니다. `SAM` 대신 `TOM`, `ANN`을 지정해 다른 가상 사용자 값을 확인할 수 있습니다.

## 방어 모드에서의 동작과 개선점

`DEFENCE_MODE=True`일 때는 허용 호스트 목록(`example.com`) 밖의 요청을 막으려 합니다. 다만 `validate_url()`이 허용된 호스트에 대해 `True`를 반환하지 않으므로, 현재 구현에서는 허용 목록 URL도 차단됩니다.

실제 환경에서는 안전한 구현에서는 다음을 함께 적용해야 합니다.

- 검증 함수가 명시적으로 `True`/`False`를 반환하도록 수정합니다.
- 호스트명뿐 아니라 DNS 해석 결과의 IP가 loopback, 사설망, link-local, 메타데이터 주소인지 차단합니다.
- 리다이렉트 이후의 목적지도 다시 검증하고, 허용할 스킴을 `http`/`https`로 제한합니다.
- URL 요청 기능 자체를 최소 권한 네트워크 환경에서 실행합니다.

이 프로젝트는 로컬 학습 목적으로만 실행하고, 임의의 외부 URL이나 실제 자격 증명 서비스에는 사용하지 마세요.
