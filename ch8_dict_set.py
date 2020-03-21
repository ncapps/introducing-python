# 8.1
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse",
}

# 8.2
print(e2f["walrus"])

# 8.3
f2e = {}
for english, french in e2f.items():
    f2e[french] = english

print(f2e)

# 8.4
print(f2e["chien"])

# 8.5
print(set(e2f))

# 8.6
life = {
    "animals":
        {
            "cats": ["Henri", "Grumpy", "Lucy"],
            "octopi": "",
            "emus": "",
        },
    "plants": "",
    "other": "",
}

# 8.7
print(list(life.keys()))

# 8.8
print(list(life["animals"].keys()))

# 8.9
print(life["animals"]["cats"])

# 8.10
squares = {number: number**2 for number in range(10)}
print(squares)

# 8.11
odd = {number for number in range(10) if number % 2 != 0}
print(odd)

# 8.12
for thing in (f'Got {number}' for number in range(10)):
    print(thing)

# 8.13
keys = ('optimistic', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
print(dict(zip(keys, values)))

# 8.14
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
print(dict(zip(titles, plots)))
