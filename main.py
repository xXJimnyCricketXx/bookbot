def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)
        
        # Sorting the character counts by frequency in descending order
        sorted_character_counts = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
        
        print_report(word_count, sorted_character_counts)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()  # Convert the text to lowercase
    char_count = {}
    for char in text:
        if char.isalpha():  # Consider only alphabetical characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def print_report(word_count, sorted_character_counts):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for char, count in sorted_character_counts:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

main()
