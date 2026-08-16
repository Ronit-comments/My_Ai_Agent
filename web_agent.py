from web_tools import (
    search_web,
    open_website
)


def run_web_task(user_request):

    print("\n🌐 Web agent started.")

    # --------------------------------------
    # Search web
    # --------------------------------------

    result = search_web(
        user_request
    )

    print("\n🔎 Search result:")
    print(result)

    # --------------------------------------
    # Handle failure
    # --------------------------------------

    if not isinstance(result, dict):

        return {
            "success": False,
            "error": "Invalid web tool result."
        }

    if not result.get("success", False):

        return result

    return result