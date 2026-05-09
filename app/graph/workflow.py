from langgraph.graph import StateGraph, END

from app.graph.state import RecruitmentState

from app.graph.nodes import (
    parse_resume_node,
    matching_node,
    decision_node
)

# =========================
# GRAPH
# =========================
workflow = StateGraph(RecruitmentState)

# =========================
# NODES
# =========================
workflow.add_node(
    "parse_resume",
    parse_resume_node
)

workflow.add_node(
    "match_candidate",
    matching_node
)

workflow.add_node(
    "decision",
    decision_node
)

# =========================
# EDGES
# =========================
workflow.set_entry_point("parse_resume")

workflow.add_edge(
    "parse_resume",
    "match_candidate"
)

workflow.add_edge(
    "match_candidate",
    "decision"
)

workflow.add_edge(
    "decision",
    END
)

# =========================
# COMPILE
# =========================
app_graph = workflow.compile()