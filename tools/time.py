import datetime

def get_current_datetime(**kwargs) -> str:
    """
        Returns current date and time.

        Returns:
            A string with the current local date and time in ISO 8601 format.
    """
    return datetime.datetime.now().isoformat()


print(get_current_datetime())