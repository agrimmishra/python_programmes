def count_letters(combinedNm, letters):
    """
    Counts the total occurrences of specified letters in the combined name string.

    Parameters:
    combinedNm (str): The concatenated string of boy's and girl's names.
    letters (str): A string containing the letters to count.

    Returns:
    int: The total count of the specified letters in the combined name string.
    """
    return sum(combinedNm.count(letter) for letter in letters)

# Taking names as input
boyNm = input("Enter the boy's name: ").strip().lower()  # Prompt for the boy's name and normalize
girlNm = input("Enter the girl's name: ").strip().lower()  # Prompt for the girl's name and normalize

# Combine the names into one string
combinedNm = boyNm + girlNm

# Calculate the first digit of the love score by counting occurrences of 't', 'r', 'u', 'e'
first_digit = count_letters(combinedNm, "true")

# Calculate the second digit of the love score by counting occurrences of 'l', 'o', 'v', 'e'
second_digit = count_letters(combinedNm, "love")

# Print the love score by concatenating the two digits
print(f"Your love score is {first_digit}{second_digit}")