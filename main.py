LINE = "I am out of office, mostly because I never left it. I will answer your email right after the 4,000 emails ahead of yours."

# The entry must be exactly one line of 1-159 characters.
assert 1 <= len(LINE) <= 159, f"line is {len(LINE)} chars"
assert "\n" not in LINE
# The gate also rejects whitespace-only text: pin the no-padding rule
# (first run showed trim==self, now enforced so a stray space fails here).
assert LINE == LINE.strip(), "line has leading/trailing whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
