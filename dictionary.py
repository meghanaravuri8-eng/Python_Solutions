s = "aabbcccc"

counts = {}

for ch in s:
    counts[ch] = counts.get(ch, 0) + 1

for ch, count in counts.items():
    print(f"{ch}={count}")