# scripts/benchmark.py
import time
import pandas as pd
from config.config import config
from scripts.data_generator import get_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from models.dummy_data import DummyData
import pymysql
from urllib.parse import quote_plus
import connectorx as cx

# =========================
# 벤치마크 1: pandas
# =========================

def benchmark_pandas(engine=None):
    if engine is None:
        engine = get_engine()
    
    query = f"SELECT * FROM {config['db']['table']}"
    start = time.perf_counter()
    df = pd.read_sql(query, engine)
    elapsed = time.perf_counter() - start

    print("\n[pandas.read_sql + pymysql connection]")
    print(f"rows: {len(df):,}")
    print(f"columns: {len(df.columns)}")
    print(f"time: {elapsed:.4f}초")

    return f"{elapsed:.4f}"


# =========================
# 벤치마크 2: sqlalchemy
# =========================

def benchmark_sqlalchemy(engine=None):
    if engine is None:
        engine = get_engine()
    
    Session = sessionmaker(bind=engine)
    start = time.perf_counter()
    with Session() as s:
        smtm = select(DummyData)
        datas = s.scalars(smtm).all()
    elapsed = time.perf_counter() - start
    
    print("\n[sqlalchemy]")
    print(f"rows: {len(datas):,}")
    print(f"time: {elapsed:.4f}초")
    
    return f"{elapsed:.4f}"


# =========================
# 벤치마크 3: pymysql
# =========================

def benchmark_pymysql():
    
    query = f"SELECT * FROM {config['db']['table']}"
    conn = pymysql.connect(
        host=config["db"]["host"],
        port=int(config["db"]["port"]),
        user=config["db"]["user"],
        password=config["db"]["password"],
        database=config["db"]["db"],
    )
    cur = conn.cursor()
    
    start = time.perf_counter()
    cur.execute(query)
    datas = cur.fetchall()
    elapsed = time.perf_counter() - start
    cur.close()
    conn.close()
    
    print("\n[pymysql]")
    print(f"rows: {len(datas):,}")
    print(f"time: {elapsed:.4f}초")
    
    return f"{elapsed:.4f}"


# =========================
# 벤치마크 4: connectorx.read_sql
# =========================

def benchmark_connectorx():
    
    user = config["db"]["user"]
    password = quote_plus(config["db"]["password"])
    host = config["db"]["host"]
    port = config["db"]["port"]
    db = config["db"]["db"]
    url = f"mysql://{user}:{password}@{host}:{port}/{db}"
    
    query = f"SELECT * FROM {config['db']['table']}"
    
    start = time.perf_counter()
    df = cx.read_sql(url, query)
    elapsed = time.perf_counter() - start

    print("\n[connectorx.read_sql]")
    print(f"rows: {len(df):,}")
    print(f"columns: {len(df.columns)}")
    print(f"time: {elapsed:.4f}초")

    return f"{elapsed:.4f}"


# =========================
# 벤치마크 5: connectorx.read_sql + 
# =========================

def benchmark_connectorx_with_partition():
    
    user = config["db"]["user"]
    password = quote_plus(config["db"]["password"])
    host = config["db"]["host"]
    port = config["db"]["port"]
    db = config["db"]["db"]
    url = f"mysql://{user}:{password}@{host}:{port}/{db}"
    
    query = f"SELECT * FROM {config['db']['table']}"
    
    start = time.perf_counter()
    df = cx.read_sql(url, query, partition_on="id", partition_num=4, partition_range=(1,2_000_000))
    elapsed = time.perf_counter() - start

    print("\n[connectorx.read_sql with partition]")
    print(f"rows: {len(df):,}")
    print(f"columns: {len(df.columns)}")
    print(f"time: {elapsed:.4f}초")

    return f"{elapsed:.4f}"