def solve(s):
    # Define a dictionary to map characters to their values
    char_values = {char: ord(char) - ord('a') + 1 for char in
'abcdefghijklmnopqrstuvwxyz'}

    # Initialize variables to keep track of the current substring and its value
    current_substring = ''
    max_value = 0

    # Iterate through the characters in the input string
    for char in s:
        if char not in 'aeiou':
            # If the character is a consonant, add it to the current substring
            current_substring += char
        else:
            # If the character is a vowel, calculate the value of the current substring
            substring_value = sum(char_values[char] for char in
current_substring)
            # Update the maximum value if the current substring has a higher value
            max_value = max(max_value, substring_value)
            # Reset the current substring
            current_substring = ''

    # Calculate the value of the last consonant substring (if any)
    substring_value = sum(char_values[char] for char in current_substring)
    max_value = max(max_value, substring_value)

    return max_value

# Test cases
print(solve("zodiacs"))  # Output: 26
print(solve("strength"))  # Output: 57
