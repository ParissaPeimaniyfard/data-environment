# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    # FFLASK_ENV=development python flask_option.py

    environment_variable = os.getenv("FLASK_ENV", "empty")
    return f"Starting in {environment_variable} mode..."



if __name__ == "__main__":
    print(start())
