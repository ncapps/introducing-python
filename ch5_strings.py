# 5.1 Capitalize the word starting with m
song = """When an eel grabs your arm,
And it causes a great harm,
That's - a moray!"""

song = song.replace(" m", " M")
print(song) 

# 5.2 Print each list question with its correctly
# matching answer, in the form:
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]

answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

print(f'Q: {questions[0]}\nA: {answers[1]}')
print(f'Q: {questions[1]}\nA: {answers[2]}')
print(f'Q: {questions[2]}\nA: {answers[0]}')

# 5.3 Write the following poem by using old-style formatting.
# Substitute the strings
poem = """
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he\'s a %s"""
args = ("roast beef", "ham", "head", "clam")
print(poem % args)

# 5.4 Write a form letter by using new-style formatting.
letter = """
Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
"""


print(letter.format(
    salutation="Mr.",
    name="Cat",
    product="shovel",
    verbed="leaked",
    room="bathroom",
    animals="dogs",
    amount="500",
    percent="60",
    spokesman="Jerry",
    job_title="Duke"
))

names = ["duck", "gourd", "spitz"]
for name in names:
    cap_name = name.capitalize()
    print(f'{cap_name}y Mc{cap_name}face')