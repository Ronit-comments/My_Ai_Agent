# ==========================================
# SECURITY
# ==========================================

from security import (
    is_action_allowed,
    needs_confirmation
)


# ==========================================
# COMPUTER TOOLS
# ==========================================

from computer_tools import (
    open_application
)


# ==========================================
# FILE TOOLS
# ==========================================

from file_tools import (
    create_folder,
    create_file,
    read_file,
    rename_path,
    move_path
)


# ==========================================
# PDF TOOLS
# ==========================================

from pdf_tool import (
    search_pdf
)


# ==========================================
# WEB TOOLS
# ==========================================

from web_tools import (
    open_website,
    search_web
)


# ==========================================
# CALCULATOR TOOLS
# ==========================================

from tools import (
    add,
    subtract,
    multiply,
    divide
)


# ==========================================
# INPUT TOOLS
# ==========================================

from input_tools import (
    move_mouse,
    click_mouse,
    type_text,
    press_key,
    scroll
)


# ==========================================
# RESULT RESOLVER
# ==========================================

from result_resolver import (
    resolve_arguments
)


# ==========================================
# TOOL REGISTRY
# ==========================================

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

    # Mouse / Keyboard
    "move_mouse": move_mouse,
    "click_mouse": click_mouse,
    "type_text": type_text,
    "press_key": press_key,
    "scroll": scroll,
}


# ==========================================
# USER CONFIRMATION
# ==========================================

def request_confirmation(action, arguments):

    print("\n⚠️ ACTION REQUIRES CONFIRMATION")

    print(f"Action: {action}")

    print(f"Arguments: {arguments}")

    answer = input(
        "\nAllow this action? (yes/no): "
    )

    return answer.lower().strip() == "yes"


# ==========================================
# NORMALIZE ARGUMENTS
# ==========================================

def normalize_arguments(action, arguments):

    if not isinstance(arguments, dict):

        return {
            "success": False,
            "error": "Arguments must be a dictionary."
        }


    # --------------------------------------
    # open_application
    # --------------------------------------

    if action == "open_application":

        if "application" not in arguments:

            if "name" in arguments:

                arguments["application"] = arguments.pop(
                "name"
            )

        elif "app" in arguments:

            arguments["application"] = arguments.pop(
                "app"
            )

        elif "application_name" in arguments:

            arguments["application"] = arguments.pop(
                "application_name"
            )


    # --------------------------------------
    # open_website
    # --------------------------------------

    elif action == "open_website":

        if (
            "url" not in arguments
            and "website" in arguments
        ):

            arguments["url"] = arguments.pop(
                "website"
            )

        elif (
            "url" not in arguments
            and "link" in arguments
        ):

            arguments["url"] = arguments.pop(
                "link"
            )


    # --------------------------------------
    # type_text
    # --------------------------------------

    elif action == "type_text":

        if (
            "text" not in arguments
            and "content" in arguments
        ):

            arguments["text"] = arguments.pop(
                "content"
            )

        elif (
            "text" not in arguments
            and "message" in arguments
        ):

            arguments["text"] = arguments.pop(
                "message"
            )


    return {
        "success": True,
        "arguments": arguments
    }


# ==========================================
# EXECUTE TASK
# ==========================================

def execute_task(task, state=None):

    # --------------------------------------
    # Validate task
    # --------------------------------------

    if not isinstance(task, dict):

        return {
            "success": False,
            "error": "Task must be a dictionary."
        }


    # --------------------------------------
    # Get action
    # --------------------------------------

    action = task.get("action")

    arguments = task.get(
        "arguments",
        {}
    )


    # --------------------------------------
    # Check action exists
    # --------------------------------------

    if not action:

        return {
            "success": False,
            "error": "No action was provided."
        }


    # --------------------------------------
    # DONE
    # --------------------------------------

    if action == "done":

        return {
            "success": True,
            "message": "Task completed."
        }


    # --------------------------------------
    # Check action exists in registry
    # --------------------------------------

    if action not in TOOL_REGISTRY:

        return {
            "success": False,
            "error": f"Unknown action: {action}"
        }


    # --------------------------------------
    # Normalize arguments
    # --------------------------------------

    normalized = normalize_arguments(
        action,
        arguments
    )


    if not normalized["success"]:

        return normalized


    arguments = normalized["arguments"]


    # --------------------------------------
    # SECURITY CHECK
    # --------------------------------------

    if needs_confirmation(action):

        approved = request_confirmation(
            action,
            arguments
        )

        if not approved:

            return {
                "success": False,
                "error": "User denied the action."
            }

    elif not is_action_allowed(action):

        return {
            "success": False,
            "error": (
                f"Action '{action}' "
                "is not allowed."
            )
        }


    # --------------------------------------
    # EXECUTE TOOL
    # --------------------------------------

    try:

        tool = TOOL_REGISTRY[action]

        result = tool(**arguments)


        # ----------------------------------
        # Normalize tool result
        # ----------------------------------

        if isinstance(result, bool):

            return {
                "success": result,
                "message": (
                    "Action executed successfully."
                    if result
                    else "Action failed."
                )
            }


        if isinstance(result, dict):

            return result


        return {
            "success": True,
            "result": result
        }


    # --------------------------------------
    # Invalid arguments
    # --------------------------------------

    except TypeError as e:

        return {
            "success": False,
            "error": (
                f"Invalid arguments for "
                f"{action}: {str(e)}"
            )
        }


    # --------------------------------------
    # Other errors
    # --------------------------------------

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }