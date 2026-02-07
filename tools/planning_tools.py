import datetime

def get_current_datetime(**kwargs) -> str:
    """
        Retrieves the current date and time.

        Returns:
            A dictionary with 'status' ("success" or "error") and 'details' (a string with current local date and time in ISO 8601 format (if success) or an error message (if error).
    """

    try:
        current_datetime = datetime.datetime.now().isoformat

        return {
            "status": "success",
            "details": current_datetime
        }

    except Exception as e:
        return {
            "status": "error",
            "details": str(e)
        }