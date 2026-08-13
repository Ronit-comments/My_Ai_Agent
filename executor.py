from pdf_tool import search_pdf

from tools import (
    add,
    subtract,
    multiply,
    divide
)


# ==========================================
# TOOL REGISTRY
# ==========================================

TOOL_REGISTRY = {

    "search_pdf": search_pdf,

    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}


# ==========================================
# EXECUTE TASK
# ==========================================

def execute_task(task):

    action = task["action"]

    task_input = task.get(
        "input",
        ""
    )


    # --------------------------------------
    # Final answer task
    # --------------------------------------

    if action == "answer":

        return None


    # --------------------------------------
    # Find tool
    # --------------------------------------

    tool = TOOL_REGISTRY.get(action)


    if tool is None:

        return (
            f"Unknown action: {action}"
        )


    # --------------------------------------
    # Execute tool
    # --------------------------------------

    try:

        result = tool(task_input)

        return result

    except Exception as e:

        return (
            f"Tool execution failed: {str(e)}"
        )