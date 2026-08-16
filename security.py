# ==========================================
# SECURITY CONFIGURATION
# ==========================================


# Actions that FRIDAY is allowed to execute
ALLOWED_ACTIONS = {

    # ======================================
    # Calculator
    # ======================================

    "add",
    "subtract",
    "multiply",
    "divide",

    # ======================================
    # PDF
    # ======================================

    "search_pdf",

    # ======================================
    # Computer
    # ======================================

    "open_application",
    "open_website",

    "move_mouse",
    "click_mouse",
    "type_text",
    "press_key",
    "scroll",

    # ======================================
    # Files
    # ======================================

    "create_folder",
    "create_file",
    "read_file",
    "rename_path",
    "move_path",

    # ======================================
    # Web
    # ======================================

    "search_web",

}


# ==========================================
# CHECK WHETHER ACTION IS ALLOWED
# ==========================================

def is_action_allowed(action):

    return action in ALLOWED_ACTIONS


# ==========================================
# ACTIONS REQUIRING USER CONFIRMATION
# ==========================================

CONFIRMATION_REQUIRED_ACTIONS = {

    # File operations that can modify data
    "create_folder",
    "create_file",
    "rename_path",
    "move_path",

}


# ==========================================
# CHECK WHETHER CONFIRMATION IS REQUIRED
# ==========================================

def needs_confirmation(action):

    return action in CONFIRMATION_REQUIRED_ACTIONS