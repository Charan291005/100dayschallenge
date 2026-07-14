from collections import Counter

string = "apple"
key = "eapl"

count = Counter(string)

answer = ""

for ch in key:
    answer += ch * count[ch]

print(answer)