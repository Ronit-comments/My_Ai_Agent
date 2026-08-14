from agent_state import AgentState


def resolve_value(value, state):

    if isinstance(value, str):

        if value.startswith("$step"):

            try:

                step_number = int(
                    value.replace("$step", "")
                )

                result = state.get_step_result(
                    step_number
                )

                return result

            except ValueError:

                return value


    return value


def resolve_arguments(arguments, state):

    resolved = {}

    for key, value in arguments.items():

        resolved[key] = resolve_value(
            value,
            state
        )

    return resolved