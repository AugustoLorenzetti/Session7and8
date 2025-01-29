s = "hello"

print(help(s.capitalize()))
print(s.capitalize())
print("HELLO".casefold()) #same as .lower() method

print("hello".center(50))
print("hello".center(50, "."))

print("I see a little dove".count("e")) # how many times do i see "e"
print("bananananana".count("ana"))

x = "I do not count nor compare"
print(f"there are: {x.count("o")} 'o's inside {x}") #how many o's are in the sentence

print("helloooo695656pool".find("l",10)) #find "l" starting from position 10

#find positions that a string appear
s = "bob guesss home meet bob so they can take bob some where"
pos = 0

while True:
    start = s.find("bob", pos)
    if start == -1: #if they dont find the letter is  -1
        break
    print("found bob in position", start)
    pos = start + 1

#filler, fill between each elements of the list
items = ["cat", "rat", "mouse", "house"]
print("+another+".join(items))
print("I LIKE to go HiKing".lower().upper())
print("I like to go skiing".title())

#replace, replace item with item inside the string
print("I like to go skiing".replace("i","l").replace("e", "3"))

#split
print("I like to go skiing".split())






