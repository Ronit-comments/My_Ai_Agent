from planner import create_plan


request = (
    "Open Notepad, "
    "type Hello FRIDAY, "
    "and then press Enter"
)


plan = create_plan(request)


print("\n📋 PLAN:\n")

for task in plan["tasks"]:

    print(
        f"Step {task['step']}: "
        f"{task['action']} "
        f"{task.get('arguments', {})}"
    )