#instantiate the PythonREPLTool from langchain_experimental.tools. Wrap it in a code block string and explicity returns the output or the caught error string so my state can read easily
from langchain_experimental.tools import PythonREPLTool
def execute_code(code: str) -> str:
    tool = PythonREPLTool()
    try:
        output = tool.run(code)
        return f"Output: {output}"
    except Exception as e:
        return f"Error: {str(e)}"