n = ['a', 'b', 'c', 'a', 'b', 'a', 'd']
m = ['a', 'z', 'b']

char_counts = {}


for character in n:
    if character in char_counts:
        char_counts[character] += 1
    else:
        char_counts[character] = 1


for letter in m:
    if letter in char_counts:
        print(f"Letter '{letter}' appears {char_counts[letter]} times")
    else:
        print(f"Letter '{letter}' appears 0 times")