

## 더미 데이터 제작   

- 사용자 지정(디폴트 50만개) 개만큼 데이터를 만들고, 지정된 DB 에 넣는다.  
- DB 설정은 config.ini 파일에서 수행  

```plaintext
[db]
baseurl=mysql+pymysql://
host=
port=
user=
password=
db=
table=dummy_data

[setting]
dummy_data_size=500000
```


## 실행 방법  

- 최초 실행인 경우 : main.py 에서 main 함수 안의 "init_data()" 주석을 풀어주세요.  

```python
def main():
    # init_data() # <----- this
    times = benchmarks()
    pd.DataFrame(times).to_csv("time_check_result.csv")
```

- 프로젝트 루트 디렉터리에서 아래 명령어 실행  

```bash
uv run main.py
```


## 벤치마크 결과

- 프로젝트 루트 디렉터리에 "time_check_result.csv" 라는 파일이 생성됩니다.  