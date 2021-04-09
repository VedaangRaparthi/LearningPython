#Madlibs using fstrings
name = input("Name: ")
verb = input("Verb: ")
adj = input("Adjective: ")
madlib = f"""Hello, I am {name}.
I like to {verb}.
It's so {adj}!
My message for you: Always stay hydrated."""

print()
print(madlib)