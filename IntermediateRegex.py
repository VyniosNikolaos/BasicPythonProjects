import re

# Groups and capturing
text = "Isaac Newton, physicist"
pattern = r"(\w+) (\w+)"
match = re.search(pattern, text)
if match:
    print(f"First name: {match.group(1)}, Last name: {match.group(2)}")

# Alternation
text = "Do you prefer Python or JavaScript?"
pattern = r"Python|JavaScript|Java|C\+\+"
matches = re.findall(pattern, text)
print(f"Programming languages mentioned: {matches}")

# Word boundaries
text = "The word 'the' is common, but 'there' and 'they' are different."
pattern = r"\bthe\b"
matches = re.findall(pattern, text)
print(f"Occurrences of 'the' as a whole word: {len(matches)}")

# Greedy vs. non-greedy matching
text = "<p>This is a paragraph.</p><p>This is another paragraph.</p>"
greedy_pattern = r"<p>.*</p>"
non_greedy_pattern = r"<p>.*?</p>"
print("Greedy match:", re.findall(greedy_pattern, text))
print("Non-greedy match:", re.findall(non_greedy_pattern, text))