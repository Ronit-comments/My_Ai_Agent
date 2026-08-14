from json import tool

from pdf_tool import search_pdf

from tools import (
    add,
    subtract,
    multiply,
    divide
)

def resolve_input(value, state):

    if isinstance(value, str):

        if value.startswith("$step"):

            step_number = int(
                value.replace("$step", "")
            )

            for result in state.get_results():

                if result["step"] == step_number:

                    return result["result"]


    return value
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

def execute_task(task, state):

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

        state.add_result(
            step=task["step"],
            action=action,
            result=result
        )
        return result

    except Exception as e:

        return f"Tool execution failed: {e}"