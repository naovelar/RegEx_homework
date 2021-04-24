#Print each persons name and twitter handle, using groups, should look like:

==============
#Full Name / Twitter
==============

#Derek Hawkins / @derekhawkins
#Erik Sven-Osterberg / @sverik
#Ryan Butz / @ryanbutz
#Example Exampleson / @example
#Ripal Pael / @ripalp
#Darth Vader / @darthvader


f = open("files/regex-test.txt")

data = f.readlines()

print(data)


person_name = re.compile("([A-Z][\w]+) ([A-Z][\w]+)@([a-z][\w])")

twitter_handle = person_name.findall(data)

print(twitter_handle)

#Regex project
#Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)

with open("files/regex.txt") as f:
    data = f.readlines()
    new_data = [item.strip() for item in data]
    print(new_data)
    
pattern = re.compile("([A-Z][a-z]*) ( [A-Z][a-z]*)? ( [A-Z][a-z])")

for name in new_data:
    match = pattern.search(name)
    if match:
        print(name)
    else:
        print(None)
