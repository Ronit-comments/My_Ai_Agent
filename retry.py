def should_retry(error):

    retryable_errors = [

        "timeout",
        "temporarily unavailable",
        "connection",
        "network"
    ]

    error = error.lower()

    for keyword in retryable_errors:

        if keyword in error:

            return True

    return False