# ==========================================
# Allowed computer actions
# ==========================================

ALLOWED_ACTIONS = {
    "open_application",
    "open_website",
    "type_text",
    "press_key",
    "click_mouse",
    "scroll",
}


# ==========================================
# Actions requiring confirmation
# ==========================================

CONFIRMATION_REQUIRED = {
    "delete_file",
    "delete_folder",
    "install_program",
    "run_command",
}


# ==========================================
# Check whether action is allowed
# ==========================================

def is_action_allowed(action):

    return action in ALLOWED_ACTIONS


# ==========================================
# Check whether action needs confirmation
# ==========================================

def needs_confirmation(action):

    return action in CONFIRMATION_REQUIRED