from scripts.data_generator import generate_dummy_data, create_db, insert_dummy_data, get_engine
from scripts.benchmark import benchmark_pandas, benchmark_sqlalchemy, benchmark_pymysql, benchmark_connectorx, benchmark_connectorx_with_partition
import pandas as pd

def init_data():
    try:
        create_db()
        datas = generate_dummy_data()
        insert_dummy_data(datas)
    except:
        datas = generate_dummy_data()
        try:
            insert_dummy_data(datas)
        except:
            print("data insert failed")

def benchmarks(engine):
    times = {
        "pandas":list(),
        "sqlalchemy":list(),
        "pymysql":list(),
        "connectorx":list(),
        "connectorx_with_partition":list()
             }
    # 10회 반복
    for i in range(10):
        times["pandas"].append(benchmark_pandas())
        times["sqlalchemy"].append(benchmark_sqlalchemy())
        times["pymysql"].append(benchmark_pymysql())
        times["connectorx"].append(benchmark_connectorx())
        times["connectorx_with_partition"].append(benchmark_connectorx_with_partition())
    return times
    
def main():
    init_data()
    engine = get_engine()
    times = benchmarks(engine)
    pd.DataFrame(times).to_csv("time_check_result.csv")
    

if __name__ == "__main__":
    main()
