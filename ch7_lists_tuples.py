# 7.1
years_list = [1987, 1988, 1989, 1990, 1991]

# 7.2
print(years_list[3], "was my third birthday")

# 7.3
print(years_list[-1], "is the last year")

# 7.4
things = ["mozzarella", "cinderella", "salmonella"]

# 7.5
print(things[1].capitalize())
print(things)

# 7.6
things[0] = things[0].upper()
print(things)

# 7.7
things.pop()
print(things)

# 7.8
surprise = ["Groucho", "Chico", "Harpo"]

# 7.9
print(surprise[2][::-1].lower().capitalize())

# 7.10
even = [number for number in range(10) if number % 2 == 0]
print(even)

# 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

for first, second in rhymes:
    for s1 in start1:
        print(s1.capitalize(),'! ', sep='',end='')
    print(first.capitalize(), "!", sep='')
    print(start2, end=' ')
    print(second, ".", sep='')