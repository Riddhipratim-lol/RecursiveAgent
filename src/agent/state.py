from typing import Optional, TypedDict, Annotated
import operator

class AgentState(TypedDict):
    prompt: str
    generated_code: str
    error_message: Optional[str]
    iterations: Annotated[int, operator.add]