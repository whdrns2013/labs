import os
from retrieval import ingest
from config.config import config
from graph.builder import CafeLanggraphBuilder
from graph.state import CafeState

def main():
    while True:
        query = input("사용자 입력 : ")
        graph, app = CafeLanggraphBuilder.build()
        state = CafeState({"query" : query})
        response = app.invoke(state)
        print(f'AI : {response["response"]}\n')

if __name__ == "__main__":
    if not os.path.exists(config["path"]["vector_store"]):
        ingest.init()
    main()
