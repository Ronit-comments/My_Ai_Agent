from pathlib import Path
import shutil


# ==========================================
# Create Folder
# ==========================================

def create_folder(path):

    try:

        folder = Path(path)

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return {
            "success": True,
            "message": f"Folder created: {folder}"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# Create File
# ==========================================

def create_file(path, content=""):

    try:

        file = Path(path)

        file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file.write_text(
            content,
            encoding="utf-8"
        )

        return {
            "success": True,
            "message": f"File created: {file}"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# Read File
# ==========================================

def read_file(path):

    try:

        file = Path(path)

        if not file.exists():

            return {
                "success": False,
                "error": f"File does not exist: {file}"
            }

        if not file.is_file():

            return {
                "success": False,
                "error": f"Path is not a file: {file}"
            }

        content = file.read_text(
            encoding="utf-8"
        )

        return {
            "success": True,
            "content": content
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# Rename File / Folder
# ==========================================

def rename_path(old_path, new_path):

    try:

        old = Path(old_path)
        new = Path(new_path)

        if not old.exists():

            return {
                "success": False,
                "error": f"Path does not exist: {old}"
            }

        old.rename(new)

        return {
            "success": True,
            "message": f"Renamed to: {new}"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# Move File / Folder
# ==========================================

def move_path(source, destination):

    try:

        source_path = Path(source)
        destination_path = Path(destination)

        if not source_path.exists():

            return {
                "success": False,
                "error": f"Source does not exist: {source_path}"
            }

        shutil.move(
            str(source_path),
            str(destination_path)
        )

        return {
            "success": True,
            "message": (
                f"Moved {source_path} "
                f"to {destination_path}"
            )
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }