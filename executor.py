from ast import arguments

from computer_tools import open_application

from pdf_tool import search_pdf

from tools import (
    add,
    subtract,
    multiply,
    divide
)

from result_resolver import (
    resolve_arguments
)


TOOL_REGISTRY = {
    "search_pdf": search_pdf,

    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,

    "open_application": open_application
}


def execute_task(task, state):

    action = task["action"]

    arguments = task.get(
        "arguments",
        {}
    )


    # --------------------------------
    # Final answer
    # --------------------------------

    if action == "answer":

        return None


    # --------------------------------
    # Resolve references
    # --------------------------------

    arguments = resolve_arguments(
        arguments,
        state
    )


    # --------------------------------
    # Find tool
    # --------------------------------

    tool = TOOL_REGISTRY.get(action)


    if tool is None:

        return {
        "success": False,
        "error": f"Unknown action: {action}"
    }


    # --------------------------------
    # Execute
    # --------------------------------

    try:

        result = tool(**arguments)

        state.add_result(
        step=task["step"],
        action=action,
        result=result
    )

        return {
        "success": True,
        "result": result
    }

    except Exception as e:

        return {
        "success": False,
        "error": str(e)
    }