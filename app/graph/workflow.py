from langgraph.graph import StateGraph, END
from app.graph.state import RecruitState
from app.graph.nodes import extract_skills_node, scoring_node, decision_node

workflow = StateGraph(RecruitState)

# nodes
workflow.add_node("extract_skills", extract_skills_node)
workflow.add_node("score", scoring_node)
workflow.add_node("decision", decision_node)

# entry point
workflow.set_entry_point("extract_skills")

# flow
workflow.add_edge("extract_skills", "score")
workflow.add_edge("score", "decision")
workflow.add_edge("decision", END)

app = workflow.compile()