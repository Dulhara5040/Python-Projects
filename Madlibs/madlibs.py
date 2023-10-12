# srting concatenation (aka how to put strings together)
# suppose we want to create a string that saya "subscribe to  __"
#youtuber ="Pocky5040" #some string variable

# few ways print the output
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")\

adjective = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
person = input("Person: ")

madlib = f"Computer programming is so {adjective}! It makes me so excied att the time beacuse\
    I love to {verb1}.Stay hydrated and {verb2} like you are {person}!"

print(madlib)