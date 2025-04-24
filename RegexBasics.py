import re

# Basic pattern matching
text = "The quick brown fox jumps over the lazy dog"

# Simple search
pattern = r"fox"
if re.search(pattern, text):
    print("Pattern 'fox' found")

# Find all occurrences
pattern = r"the"
matches = re.findall(pattern, text, re.IGNORECASE)
print(f"Occurrences of 'the': {len(matches)}")

# Match at the beginning
pattern = r"^The"
if re.match(pattern, text):
    print("Text starts with 'The'")

# Basic character classes
pattern = r"[aeiou]"
vowels = re.findall(pattern, text, re.IGNORECASE)
print(f"Vowels found: {vowels}")

# Digits
phone = "Call me at 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"
if re.search(pattern, phone):
    print("Valid phone number format found")

# Basic quantifiers
pattern = r"z{2}"  # two consecutive 'z's
if re.search(pattern, "I love pizzza!"):
    print("'zz' found")

# Wildcard
pattern = r"b.g"  # any character between 'b' and 'g'
matches = re.findall(pattern, "big bag bug")
print(f"Matches for 'b.g': {matches}")