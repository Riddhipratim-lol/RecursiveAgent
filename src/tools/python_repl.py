from langchain_experimental.tools import PythonREPLTool
def execute_code(code: str) -> str:
    tool = PythonREPLTool()
    try:
        output = tool.run(code)
        return f"Output: {output}"
    except Exception as e:
        return f"Error: {str(e)}"