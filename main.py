student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# Load the NATO phonetic alphabet from the CSV file into a DataFrame
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Convert the DataFrame to a dictionary using dictionary comprehension
nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Function to convert a word to NATO phonetic code words
def get_phonetic_representation(word):
    """
    Convert the input word to its phonetic code word list using the dictionary created from CSV data.

    Parameters:
    word (str): The word input by the user.

    Returns:
    list: A list of phonetic code words for each letter in the word.
    """
    return [nato_alphabet[letter] for letter in word.upper() if letter in nato_alphabet]

# Example usage:
# Main program loop
while True:
    # Prompt the user for a word
    word = input("Enter a word to convert to the NATO phonetic alphabet (or type 'exit' to quit): ")

    # Check if the user wants to exit
    if word.lower() == 'exit':
        print("Goodbye!")
        break

    # Get the phonetic representation and display it
    try:
        phonetic_list = get_phonetic_representation(word)
        print("Phonetic Code Words:", phonetic_list)
    except KeyError:
        print("Please enter a word containing only alphabetic characters.")

    # Ask if they want to enter another word
    print()  # Add a blank line for better readability
