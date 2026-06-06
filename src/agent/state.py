from typing import Optional, TypedDict, Annotated
import operator

class AgentState(TypedDict):
    prompt: str
    generated_code: str
    test_cases: str
    repl_output: Optional[str]
    iterations: Annotated[int, operator.add]
    # human_feedback: str (For Future Use)