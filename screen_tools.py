from PIL import ImageGrab


def take_screenshot():

    try:

        screenshot = ImageGrab.grab()

        screenshot.save("screen.png")

        return {
            "success": True,
            "message": "Screenshot saved as screen.png"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
    