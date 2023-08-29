# python-code-challenge1

Challenge 1: Converting 12-hour Time to 24-hour Time

Description:
In this coding challenge, you'll be crafting a Python function that handles the conversion of time from the 12-hour format to the 24-hour format. Given an input time consisting of an hour, a minute, and a period (either "am" or "pm"), your task is to develop a function that seamlessly transforms this input into a four-digit string representation in the 24-hour format.

Functionality:

def convert_to_24_hour(hour: int, minute: int, period: str) -> str:
    """
    Converts a 12-hour time to 24-hour time.

    Args:
        hour (int): The hour in the range of 1 to 12.
        minute (int): The minute in the range of 0 to 59.
        period (str): The period, either "am" or "pm".

    Returns:
        str: The time in 24-hour format as a four-digit string.
    """
    # Your implementation here
    # Convert hour to 24-hour format considering the period
    # Format the time as a four-digit string (HHMM)
    # Return the formatted time
Challenge 2: Exactly Two Positive Integers

Description:
This challenge revolves around crafting a Python function that evaluates whether exactly two out of three given integers are positive. Your objective is to inspect each integer and ascertain if the count of positive integers among the three is precisely two.

Functionality:
def exactly_two_positive(a: int, b: int, c: int) -> bool:
    """
    Checks if exactly two out of three integers are positive.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        bool: True if exactly two integers are positive, False otherwise.
    """
    # Your implementation here
    # Count the number of positive integers among a, b, and c
    # Return True if the count is exactly 2, otherwise False
Challenge 3: Highest Value of Consonant Substrings

Description:
This intriguing challenge demands the creation of a Python function that calculates the highest value of substrings formed exclusively from consonant characters within a given lowercase string. To achieve this, you'll be provided with a predefined mapping of consonant characters to their corresponding values.

Functionality:
def highest_consonant_value(s: str) -> int:
    """
    Calculates the highest value of consonant substrings.

    Args:
        s (str): The input lowercase string with alphabetic characters only.

    Returns:
        int: The highest value of consonant substrings.
    """
    # Your implementation here
    # Define a mapping of consonant characters to their values
    # Iterate through the string and identify consonant substrings
    # Calculate the value of each consonant substring and track the highest value
    # Return the highest cumulative value among the identified substrings

