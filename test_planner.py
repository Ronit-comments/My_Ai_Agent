from planner import create_plan

request = "add 5 and 10, then multiply the result by 2, and finally subtract 3"

plan = create_plan(request)

print("\nPLAN:\n")

for task in plan["tasks"]:
    print(
        f"Step {task['step']}: "
        f"{task['action']} "
        f"{task.get('arguments', {})}"
    )