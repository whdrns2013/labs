from config.config import config
from models.dummy_data import DummyData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

def generate_dummy_data(data_size:int = int(config["setting"]["dummy_data_size"])):
    countries = ["KR", "US", "JP", "CN", "DE", "FR", "GB", "IN"]
    rows = []
    for i in range(1, data_size + 1):
        rows.append((
            i,
            f"user_{i}",
            f"user_{i}@example.com",
            20 + (i % 50),
            countries[i % len(countries)],
            round((i % 10000) / 100, 2),
            f"2026-01-{(i % 28) + 1:02d} 12:00:00"
        ))
    return rows

def get_engine(baseurl:str=config["db"]["baseurl"],
               user:str=config["db"]["user"],
               password:str=config["db"]["password"],
               host:str=config["db"]["host"],
               port:str=config["db"]["port"],
               db:str=config["db"]["db"]):
    url = f"{baseurl}{user}:{quote_plus(password)}@{host}:{port}/{db}"
    connect_args = {
        "connect_timeout": 30,
        "read_timeout": 600,
        "write_timeout": 600,
        "charset": "utf8mb4",
        }
    engine = create_engine(url, echo=False, connect_args=connect_args)
    return engine

def create_db(engine = get_engine()):
    DummyData.__table__.create(bind=engine)

def insert_dummy_data(data:list[tuple], engine=get_engine()):
    Session = sessionmaker(bind=engine)
    with Session() as s:
        for id, name, email, age, country, score, created_at in data:
            dummy = DummyData(
                id = id, name = name, email = email, age = age,
                country = country, score = score, created_at = created_at
            )
            s.add(dummy)
        s.commit()
    return