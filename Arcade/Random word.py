from random_word import RandomWords

def generate_random_word():
    r = RandomWords()
    word = r.get_random_word()
    return word.lower() if word else "default"  # Fallback in case no word is fetched

# Example usage
print("Random Word:", generate_random_word())
