from collections import Counter

def word_frequency_counter(text):
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Count word frequency
    freq = Counter(words)
    
    # Get top 3
    top_three = freq.most_common(3)
    
    print("Top 3 most frequent words:")
    for word, count in top_three:
        print(f"{word}: {count}")

# Example run
paragraph = input("Enter a paragraph: ")
word_frequency_counter(paragraph)
