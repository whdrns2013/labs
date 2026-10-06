from typing import TypedDict, Annotated
from enum import Enum

class Intent(str, Enum):
    cafe:str = "cafe"
    other:str = "other"

class CafeState(TypedDict):
    query: Annotated[str, "사용자의 질문 텍스트"]
    intent: Annotated[Intent, "사용자의 질문 의도"]
    intent_reason: Annotated[str, "질문 의도 분류 이유"]
    document : Annotated[str, "질문에 답변하기 위한 참고자료 텍스트"]
    response : Annotated[str, "질문에 대한 답변 텍스트"]