# This script automates the retrieval of input data for the Advent of Code challenges.
# It is designed to be executed once per day to download the input for the current day's challenge.
# The script requires the AOC_SESSION environment variable to be set with the session cookie.
# To download the input for a specific day or to re-download the input for the current day,
# a day can be specified as a command-line argument. If no argument is provided, the script
# will default to downloading the input for the current day.
#
# Usage:
#   python3 get_aoc_input.py [day]
#
# Example (default usage):
#   python3 get_aoc_input.py
#
# Example (force download for day 1):
#   python3 get_aoc_input.py 1


import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import sys
import logging

YEAR = 2024

def get_input(day, forced_day=False):
    """
    Downloads the input for the given day from the Advent of Code website.

    Args:
        day (int): The day for which to download the input.
        forced_day (bool): If True, forces the download even if the input already exists.
    """
    input_path = os.path.join(str(YEAR), "Input", f"Day{day}.txt")
    
    # Check if the input has already been downloaded
    if os.path.exists(input_path) and not forced_day:
        logging.error(f"Error: Input for day {day} already downloaded")
        return

    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    session = os.environ.get("AOC_SESSION")
    if not session:
        raise EnvironmentError("Error: AOC_SESSION environment variable not set")

    cookies = {"session": session}
    headers = {"User-Agent": "github.com/swarleyman1/Advent_of_Code"}

    response = requests.get(url, cookies=cookies, headers=headers)
    response.raise_for_status()

    # Ensure the directory exists
    os.makedirs(os.path.dirname(input_path), exist_ok=True)
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    
    logging.info(f"Input for day {day} {'re-' if forced_day else ''}downloaded to {input_path}")

if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    # Check month and warn if not December
    current_month = datetime.now().strftime("%B")
    if datetime.now().month != 12:
        logging.warning(f"Warning: Code is only intended to be used in December. Current month is {current_month}.")
    forced_day = False

    # Check if a day is provided as a command-line argument
    try:
        day = int(sys.argv[1])
        if day < 1 or day > 25:
            logging.error("Error: Day must be between 1 and 25")
            sys.exit(1)
        forced_day = True
    except ValueError:
        day = datetime.now().day
    
    try:
        get_input(day, forced_day)
        logging.info("Input downloaded successfully")
    except (requests.exceptions.RequestException, EnvironmentError) as e:
        logging.error(e)
        logging.error("Failed to download input")
        sys.exit(1)

