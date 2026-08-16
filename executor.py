from ast import arguments

from computer_tools import open_application

from computer_tools import (
    open_application,
)
from file_tools import (
    create_folder,
    create_file,
    read_file,
    rename_path,
    move_path
)
from pdf_tool import search_pdf

from web_tools import (
    open_website,
    search_web
)

from tools import (
    add,
    subtract,
    multiply,
    divide
)

from result_resolver import (
    resolve_arguments
)
from input_tools import (
    move_mouse,
    click_mouse,
    type_text,
    press_key,
    scroll
)

TOOL_REGISTRY = {

    # Calculator
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,

    # PDF
    "search_pdf": search_pdf,

    # Computer
    "open_application": open_application,

    # Files
    "create_folder": create_folder,
    "create_file": create_file,
    "read_file": read_file,
    "rename_path": rename_path,
    "move_path": move_path,

    # Web
    "search_web": search_web,
    "open_website": open_website,

    "move_mouse": move_mouse,
    "click_mouse": click_mouse,
    "type_text": type_text,
    "press_key": press_key,
    "scroll": scroll,
}


def execute_task(task, state=None):

    action = task.get("action")
    arguments = task.get("arguments", {})

    # ------------------------------------------
    # Normalize arguments
    # ------------------------------------------

    if not isinstance(arguments, dict):
        return {
            "success": False,
            "error": "Arguments must be a dictionary."
        }

    # Gemini sometimes uses "name" instead of
    # the expected parameter name "application"
    if action == "open_application":

        if "application" not in arguments and "name" in arguments:
            arguments["application"] = arguments.pop("name")

    # ------------------------------------------
    # Check action
    # ------------------------------------------

    if action not in TOOL_REGISTRY:

        return {
            "success": False,
            "error": f"Unknown action: {action}"
        }

    # ------------------------------------------
    # Execute tool
    # ------------------------------------------

    try:

        tool = TOOL_REGISTRY[action]

        result = tool(**arguments)

        return result

    except TypeError as e:

        return {
            "success": False,
            "error": f"Invalid arguments for {action}: {str(e)}"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }