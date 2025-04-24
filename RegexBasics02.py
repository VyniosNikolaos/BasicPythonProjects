import re

# 1. Literal characters
text = "Hello, World!"
pattern = r"World"
if re.search(pattern, text):
    print("'World' found in the text")

# 2. Metacharacters
# . (dot) - matches any character except newline
pattern = r"h.llo"
print(re.findall(pattern, "hello hallo hillo", re.IGNORECASE))

# ^ (caret) - matches start of the string
pattern = r"^Hello"
print(re.match(pattern, "Hello, World!") is not None)

# $ (dollar) - matches end of the string
pattern = r"World!$"
print(re.search(pattern, "Hello, World!") is not None)

# 3. Character classes
# [abc] - matches any one character within the brackets
pattern = r"[aeiou]"
print(re.findall(pattern, "Hello World"))

# [^abc] - matches any one character not within the brackets
pattern = r"[^aeiou]"
print(re.findall(pattern, "Hello World"))

# 4. Predefined character classes
# \d - digit, \D - non-digit
print(re.findall(r"\d", "There are 123 apples"))
print(re.findall(r"\D", "There are 123 apples"))

# \w - word character, \W - non-word character
print(re.findall(r"\w", "Hello, World! 123"))
print(re.findall(r"\W", "Hello, World! 123"))

# \s - whitespace, \S - non-whitespace
print(re.findall(r"\s", "Hello World"))
print(re.findall(r"\S", "Hello World"))

# 5. Quantifiers
# * - 0 or more occurrences
print(re.findall(r"ca*t", "ct cat caat caaat"))

# + - 1 or more occurrences
print(re.findall(r"ca+t", "ct cat caat caaat"))

# ? - 0 or 1 occurrence
print(re.findall(r"colou?r", "color colour"))

# {n} - exactly n occurrences
print(re.findall(r"\d{3}", "123 1234 12345"))

# {n,m} - between n and m occurrences
print(re.findall(r"\d{2,3}", "123 1234 12345"))

# 6. Escaping special characters
# Use \ to match literal special characters
print(re.findall(r"\.", "Hello. How are you?"))

# 7. Groups and capturing
# () - creates a capturing group
match = re.search(r"(\w+) (\w+)", "John Doe")
if match:
    print(f"First name: {match.group(1)}, Last name: {match.group(2)}")

# 8. Non-capturing groups
# (?:) - creates a non-capturing group
print(re.findall(r"(?:Mr|Mrs|Ms)\. \w+", "Mr. Smith and Mrs. Johnson"))

# 9. Alternation
# | - matches either expression
print(re.findall(r"cat|dog", "I have a cat and a dog"))