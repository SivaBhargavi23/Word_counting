#prompting the user to enter a sentence or paragraph
print("Enter your text here:")
text = str(input())
#Word counting logic
# Check if there are any words
if len(text.split()) > 0:
  # Count and print the number of words
  words = len(text.split())
  print("The number of words in your text is:", words)
else:
  # Print a message if there are no words
  print("There are no words in your text.")
