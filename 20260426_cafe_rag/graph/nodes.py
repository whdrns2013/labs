from llm.chat_model import load_model
from graph.state import CafeState
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import retrieval

def intent_classify_node(state:CafeState):
    prompt_file_path = "prompts/intent_classify_v1.0.txt"
    with open(prompt_file_path, "r", encoding="utf-8") as f:
        prompt = PromptTemplate.from_template(f.read())
    chain = prompt | load_model() | JsonOutputParser()
    response = chain.invoke({"query":state["query"]})
    return {"intent":response["intent"], "intent_reason":response["reason"]}

def retrieve_node(state:CafeState):
    document = retrieval.retrieve(query = state["query"])
    return {"document":document}

def llm_node(state:CafeState):
    prompt_file_path = "prompts/llm_response_v1.0.txt"
    with open(prompt_file_path, "r", encoding="utf-8") as f:
        prompt = PromptTemplate.from_template(f.read())
    chain = prompt | load_model() | JsonOutputParser()
    response = chain.invoke({"query":state["query"], "reference":state["document"]})
    # response = chain.stream({"query":state["query"], "reference":state["document"]})
    return {"response":response["response"]}

def fallback_node(state:CafeState):
    return {"response":"카페 이용 및 브랜드 관련 문의만 가능합니다. 다시 질문해주시기 바랍니다."}

def output_node(state:CafeState):
    return {"response" : state["response"]}