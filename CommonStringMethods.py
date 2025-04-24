# Sample string
text = "Hello, World!"

# Converting case
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {'hello world'.title()}")

# Stripping whitespace
padded_text = "   some text   "
print(f"Stripped: '{padded_text.strip()}'")
print(f"Left stripped: '{padded_text.lstrip()}'")
print(f"Right stripped: '{padded_text.rstrip()}'")

# Replacing substrings
print(f"Replacing 'World' with 'Python': {text.replace('World', 'Python')}")

# Splitting strings
comma_separated = "apple,banana,cherry"
print(f"Splitting by comma: {comma_separated.split(',')}")

# Joining strings
words = ['Hello', 'World', 'of', 'Python']
print(f"Joining with spaces: {' '.join(words)}")

# Finding substrings
print(f"Index of 'World': {text.index('World')}")
print(f"Does it start with 'Hello'? {text.startswith('Hello')}")
print(f"Does it end with 'Python'? {text.endswith('Python')}")

# Counting occurrences
print(f"Count of 'l' in '{text}': {text.count('l')}")

# Checking string content
numeric_string = "12345"
alpha_string = "AbCdE"
print(f"Is '{numeric_string}' numeric? {numeric_string.isnumeric()}")
print(f"Is '{alpha_string}' alphabetic? {alpha_string.isalpha()}")

# Centering string
print(f"Centered: {text.center(20, '*')}")