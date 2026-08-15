import pyautogui

pyautogui.FAILSAFE = True
# ==========================================
# Move Mouse
# ==========================================

def move_mouse(x, y):

    try:

        pyautogui.moveTo(x, y, duration=0.2)

        return {
            "success": True,
            "message": f"Mouse moved to ({x}, {y})"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# Click
# ==========================================

def click_mouse(x, y):

    try:

        pyautogui.click(x, y)

        return {
            "success": True,
            "message": f"Clicked at ({x}, {y})"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# Type Text
# ==========================================

def type_text(text):

    try:

        pyautogui.write(
            text,
            interval=0.03
        )

        return {
            "success": True,
            "message": "Text typed successfully"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# Press Key
# ==========================================

def press_key(key):

    try:

        pyautogui.press(key)

        return {
            "success": True,
            "message": f"Pressed {key}"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# Scroll
# ==========================================

def scroll(amount):

    try:

        pyautogui.scroll(amount)

        return {
            "success": True,
            "message": f"Scrolled {amount}"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }