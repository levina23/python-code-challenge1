# python-code-challenge1

Challenge 1: Converting 12-hour Time to 24-hour Time
Description
In this challenge, you're tasked with creating a Python function that handles the conversion of 12-hour time representation to the 24-hour format. Given an hour, minute, and period (either "am" or "pm"), your function should return a four-digit string representing the time in the 24-hour format.
 
 # functionality
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
# python-code-challenge2
Description
This challenge revolves around creating a Python function that assesses whether exactly two out of three given integers are positive. You're required to check the positivity of each integer and determine if the count of positive integers is exactly equal to two.

# functionality
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
# python-code-challenge3
This challenge involves crafting a Python function that computes the highest value of consonant substrings within a given lowercase string. You'll be working with a defined mapping of consonant characters to their corresponding values, and your function should find the highest cumulative value of any substring formed only by consonant characters.
 
 # functionality
 def highest_consonant_value(s: str) -> int:
    """
    Calculates the highest value of consonant substrings.

    Args:
        s (str): The input lowercase string with alphabetic characters only.

    Returns:
        int: The highest value of consonant substrings.
    """
