
from graph import state, nodes
from langgraph.graph import StateGraph, START, END

class CafeLanggraphBuilder:
    
    @staticmethod    
    def build():
        graph = StateGraph(state.CafeState)
        
        graph.add_node("intent", nodes.intent_classify_node)
        graph.add_node("retrieve", nodes.retrieve_node)
        graph.add_node("llm", nodes.llm_node)
        graph.add_node("fallback", nodes.fallback_node)
        graph.add_node("output", nodes.output_node)

        graph.add_edge(START, "intent")
        graph.add_conditional_edges("intent", lambda x:x["intent"], {"cafe":"retrieve", "other":"fallback"})
        graph.add_edge("retrieve", "llm")
        graph.add_edge("llm", "output")
        graph.add_edge("fallback", "output")
        graph.add_edge("output", END)

        app = graph.compile()
        return graph, app