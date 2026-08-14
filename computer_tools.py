import subprocess


def open_application(application):

    applications = {

        "chrome": "chrome",

        "vscode": "code",

        "notepad": "notepad",

        "calculator": "calc",

        "explorer": "explorer"

    }

    app = applications.get(
        application.lower()
    )

    if app is None:

        return {
            "success": False,
            "error": f"Unknown application: {application}"
        }

    try:

        subprocess.Popen(app)

        return {
            "success": True,
            "message": f"Opened {application}"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }