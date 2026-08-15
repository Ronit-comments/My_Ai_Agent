from file_tools import create_folder
from file_tools import move_path


create_folder(
    "agent_test/archive"
)


result = move_path(
    "agent_test/study_notes.txt",
    "agent_test/archive/study_notes.txt"
)

print(result)