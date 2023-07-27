import random
import string
import re

def rewrite_text(text, perplexity, burstiness):
    """Rewrites text to have the specified perplexity and burstiness.

  Args:
    text: The text to be rewritten.
    perplexity: The desired perplexity of the rewritten text.
    burstiness: The desired burstiness of the rewritten text.

  Returns:
    The rewritten text.
  """

    new_text = ""
    for word in text.split():
        new_word = word
        if random.random() < burstiness / 100:
            new_word = random.choice(string.ascii_lowercase)
        elif random.random() < perplexity / 100:
            new_word = str(random.choices(list(string.ascii_lowercase + string.digits + " ")))
            new_word = re.sub(r"[^a-zA-Z0-9 ]", "", new_word)
        new_text += new_word
    return str(new_text)

def main():
    """Prompts the user to enter text and then scrambles it."""

    text = input("Enter the text you want to scramble: ")
    perplexity = int(input("Enter the perplexity: "))
    burstiness = int(input("Enter the burstiness: "))
    new_text = rewrite_text(text, perplexity, burstiness)
    print(f"The scrambled text is: {new_text}")

if __name__ == "__main__":
    main()