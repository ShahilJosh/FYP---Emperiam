import re
from readcv import text

# Example text output
text_output = text

# Define the regex pattern to match a name (assuming a name is a sequence of words separated by spaces)
pattern = r'\b[A-Za-z]+\s+[A-Za-z]+\s+[A-Za-z]+\b'

# Search for the pattern in the text output
match = re.search(pattern, text_output)

# Extract the matched name
if match:
    name = match.group()
    print(f"Name: {name}")
else:
    print("No name found in the text output.")