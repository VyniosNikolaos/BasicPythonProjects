import re

# Named groups
text = "John Doe, 30 years old"
pattern = r"(?P<name>\w+ \w+), (?P<age>\d+) years old"
match = re.search(pattern, text)
if match:
    print(f"Name: {match.group('name')}, Age: {match.group('age')}")

# Lookahead and lookbehind
text = "123abc456def789"
pattern = r"\d+(?=[a-z])"  # Numbers followed by letters
print("Numbers followed by letters:", re.findall(pattern, text))

pattern = r"(?<=[a-z])\d+"  # Numbers preceded by letters
print("Numbers preceded by letters:", re.findall(pattern, text))

# Verbose regex (multiline with comments)
pattern = re.compile(r"""
    \b          # Word boundary
    (\d{1,3})   # 1-3 digits
    (?:         # Non-capturing group
        ,\d{3}  # Comma followed by 3 digits
    )*          # Zero or more times
    (?:\.\d+)?  # Optional decimal part
    \b          # Word boundary
""", re.VERBOSE)

text = "1,000,000.00 is a million"
match = pattern.search(text)
if match:
    print(f"Found number: {match.group()}")