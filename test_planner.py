from planner import create_plan

request = "search my ml pdf for decision trees"

plan = create_plan(request)

print("\nPLAN:\n")

for task in plan["tasks"]:
    print(
        f"Step {task['step']}: "
        f"{task['action']} "
        f"{task.get('arguments', {})}"
    )