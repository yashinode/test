def hello():
    """Print a greeting message.

    Raises:
        Exception: If an error occurs during message printing.
    """
    try:
        print("Hello, world!")
    except Exception as e:
        raise Exception(f"Failed to print greeting message: {e}")

if __name__ == "__main__":
    try:
        hello()
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
