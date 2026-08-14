from agent_state import AgentState

from executor import execute_task


state = AgentState()


# =================================
# STEP 1
# =================================

task1 = {

    "step": 1,

    "action": "multiply",

    "arguments": {

        "a": 25,

        "b": 4

    }

}


result1 = execute_task(
    task1,
    state
)

print(
    "Step 1:",
    result1
)


# =================================
# STEP 2
# =================================

task2 = {

    "step": 2,

    "action": "add",

    "arguments": {

        "a": "$step1",

        "b": 50

    }

}


result2 = execute_task(
    task2,
    state
)

print(
    "Step 2:",
    result2
)


# =================================
# STEP 3
# =================================

task3 = {

    "step": 3,

    "action": "multiply",

    "arguments": {

        "a": "$step2",

        "b": 2

    }

}


result3 = execute_task(
    task3,
    state
)

print(
    "Step 3:",
    result3
)


# =================================
# SHOW STATE
# =================================

print("\nSTATE:")

print(
    state.get_results()
)