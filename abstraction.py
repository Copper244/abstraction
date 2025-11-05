#learning abstraction

#abstraction means to simplify complex code
#or wrap complex code into a box called
#a function
#first we define a function
def speech ():
i_have_a_dream_speech = "I may not get there with you. But I want you to know tonight, that we, as a people, will get to the Promised Land. And so I'm happy tonight; I'm not worried about anything; I'm not fearing any man. Mine eyes have seen the glory of the coming of the Lord"

word_find = "freedom"

if word_find in i_have_a_dream:
    print("found")
else :
    print("not found")

question = input("did you find the word?")
print('your response is : ', question)


speech()
speech()