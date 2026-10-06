
## 1. 기본 환경  

- 패키지 매니저인 uv 가 설치되어있어야 합니다.  
- 명령어들은 터미널에서 실행합니다.  

## 2. 의존성 설치  

- (터미널)본 프로젝트의 루트 경로에서 아래 명령어를 실행합니다.  
- 이 명령어는 본 프로젝트에 명세된 의존성 라이브러리들을 설치합니다.  

```bash
uv sync
```

## 4. 프로그램 실행  

- (터미널)본 프로젝트의 루트 경로에서 아래 명령어를 실행합니다.  

```bash
uv run main.py
```

- (터미널)study 디렉터리에 위치한 파일들도 실행 가능합니다.    

```bash
uv run study/01_BaseSettings_declare.py
```

## 5. 프로그램 실행의 결과  

- 터미널에서 아래와 같은 출력을 볼 수 있습니다.  

```bash
ervice=ServiceSettings(timeout=30, multiprocessor_num='36') dirpath=DirPathSettings(data_path='dataaa', artifact_path='artifactssss', log_path='logssss') logging=LoggingSettings(expire_day='10000', log_level='ERROR') dummy_secret='dummy_secret_key_is_1234567'
35
dummy_secret_key_is_1234567
```