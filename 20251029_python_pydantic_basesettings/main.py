from core.settings import settings # 이렇게 인스턴스 자체를 import

def main():
    print(settings)
    print(settings.service.TIMEOUT + 5)
    print(settings.logging.LOG_LEVEL)

if __name__ == "__main__":
    main()
