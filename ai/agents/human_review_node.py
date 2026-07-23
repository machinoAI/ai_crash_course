"""
How do you add a human review node in LangGraph ?
"""

from langgraph.types import interrupt

def human_review(state: AgentState):

    approval = interrupt(
        {
            "message": "Approve this action?",
            "action": state["action"],
            "risk_score": state["risk_score"],
            "query": state["query"]
        }
    )

    state["approval"] = approval

    return state