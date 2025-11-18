def get_text_input():
    return input("Enter a sentence: ")

def count_words(text):
    return len(text.split())

def print_result(word_count):
    print("The text contains",word_count,"words.")

user_text=get_text_input()
count=count_words(user_text)
print_result(count)
