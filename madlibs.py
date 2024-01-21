# # string concatenation
# # how to make "subscribe to ___"?
# youtuber = "Markiplier" # some random string variable

# # a few ways to do this, but the last one is the best madlibs:
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}") # the almighty f string

adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
bird = input("Type of bird: ")
room = input("Room in a house: ")
verb_past = input("Verb (past tense): ")
verb1 = input("Verb: ")
relative = input("Relative's name: ")
noun1 = input("Noun: ")
liquid = input("A liquid: ")
verb_ing1 = input("Verb ending in -ing: ")
body_part = input("Part of the body (plural): ")
noun_plural = input("Plural noun: ")
verb_ing2 = input("Verb ending in -ing: ")
noun2 = input("Noun: ")

madlib = f"""It was a {adj1}, cold November day. I woke up to the {adj2} smell of {bird} roasting in the {room} downstairs. I {verb_past} down the stairs to see if I \
could help {verb1} the dinner. My mom said, 'See if {relative} needs a fresh {noun1}.' So I carried a tray of glasses full of {liquid} into the {verb_ing1} room. When \
I got there, I couldn't believe my {body_part}! There were {noun_plural} {verb_ing2} on the {noun2}!"""

print(madlib)