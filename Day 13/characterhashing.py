n = ['a', 'b', 'c', 'a', 'b', 'a', 'd']
m = ['a', 'z', 'b']

# Brute force character matching
for letter in m:
    count = 0
    for character in n:
        if character == letter:
            count += 1
    print(f"Letter '{letter}' appears {count} times")