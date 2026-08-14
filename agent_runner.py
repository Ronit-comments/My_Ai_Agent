from executor import execute_task
from retry import should_retry


def run_task(
    task,
    state,
    max_retries=2
):

    attempts = 0


    while attempts <= max_retries:

        result = execute_task(
            task,
            state
        )


        # -----------------------------
        # Successful
        # -----------------------------

        if result["success"]:

            return result


        # -----------------------------
        # Failed
        # -----------------------------

        error = result["error"]

        print(
            f"Tool failed: {error}"
        )


        # -----------------------------
        # Check retry
        # -----------------------------

        if not should_retry(error):

            return result


        attempts += 1

        print(
            f"🔄 Retrying... "
            f"Attempt {attempts}"
        )


    return result