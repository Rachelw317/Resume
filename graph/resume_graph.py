from langgraph.graph import StateGraph, START, END
from schemas.state import ResumeState

from nodes.load_resume_node import load_resume_node
from nodes.parse_resume_node import parse_resume_node

from nodes.load_jd_node import load_jd_node
from nodes.parse_jd_node import parse_jd_node

from nodes.match_analysis_node import match_analysis_node

from nodes.opimize_node import optimize_resume_node

from nodes.write_node import write_node

def build_resume_graph() -> StateGraph:
   
   # 告诉LangGraph我们使用的状态类型是ResumeState
   # 以后所有Node的输入输出都会是ResumeState类型
   graph = StateGraph(ResumeState)
   
   # 节点名字：执行函数
   graph.add_node("load_resume", load_resume_node)
   graph.add_node("parse_resume", parse_resume_node)
   
   graph.add_node("load_jd", load_jd_node)
   graph.add_node("parse_jd", parse_jd_node)
   
   graph.add_node("match_analysis", match_analysis_node)
   
   graph.add_node("optimize_resume", optimize_resume_node)
   
   graph.add_node("write", write_node)
   
   graph.add_edge(
        START,
        "load_resume"
   )

   graph.add_edge(
        START,
        "load_jd"
   )


   graph.add_edge(
        "load_resume",
        "parse_resume"
   )


   graph.add_edge(
        "load_jd",
        "parse_jd"
   )
   
   graph.add_edge(
            "parse_resume",
            "match_analysis"
     )
   
   graph.add_edge(
            "parse_jd",
            "match_analysis"
     )
   
   graph.add_edge(
            "match_analysis",
            "optimize_resume"
     )
   
   graph.add_edge(
            "optimize_resume",
            "write"
     )    
   
   graph.add_edge(
        "write",
        END
     )



   return graph.compile()
   
