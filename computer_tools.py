import subprocess


def open_application(application):

    application = application.lower().strip()

    applications = {
        "chrome": "chrome",
        "vscode": "code",
        "notepad": "notepad",
        "calculator": "calc",
        "explorer": "explorer"
    }

    target = applications.get(application)

    if target is None:

        return {
            "success": False,
            "error": f"Unknown application: {application}"
        }

    try:

        subprocess.Popen(
            ["cmd", "/c", "start", "", target],
            shell=False
        )

        return {
            "success": True,
            "message": f"Opened {application}"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }