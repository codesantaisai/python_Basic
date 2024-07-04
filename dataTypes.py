#literal assingment

# firstName = "Jathurshan"
# lastName  = "Santhirasekaram"

# print(type(firstName))
# print(type(lastName)==str)
# print(isinstance(firstName,int))

# contstructor function

# name = str("Jathurshan")
# print(type(name))
# print(type(name)==str)
# print(isinstance(name,int))

#concatination
# fullName = firstName+" "+lastName+"!"
# print(fullName)

#casting

# decade = str(24)

# print(decade)
# print(type(decade))

# statement = "I was born in"+ decade + " years ago"

# print(statement)
# print(type(statement))


# multiLine = """
#     This is a multiline string
#         I can span multiple lines
#             And print them as is
#     """
# print(multiLine)
# print(type(multiLine))


# sentence = "I\'m Jathurshan Santhirasekaram \t I\'m a Software Engineer and \n FullStack Developer"
# print(sentence)
# print(sentence.lower())
# print(sentence.upper())
# print(sentence.title())
# print(sentence.replace("FullStack",".NET"))


# print(len(sentence))
# sentence += "     "
# sentence += "this is jathu"+ "    "


# print(len(sentence))
# print(len(sentence.strip()))


#Build a Menu

# title = "menu".upper() # change to uppercase
# print(title.center(20,"=")) #title will place in the center then R&L side will replace with # 
# print("Coffee".ljust(16,".")+"$1".rjust(4)) #left align .from the left 16 char replace by . then $1 remaining empty space
# print("Muffin".ljust(16,".")+"$2".rjust(4)) #left align .from the left 16 char replace by . then $1 remaining empty space
# print("Cheesecake".ljust(16,".")+"$4".rjust(4)) #left align .from the left 16 char replace by . then $1 remaining empty space


#index

name = "jathurshan"
print(name[0])
print(name[-1])
print(name[1:-1])
print(name[1:])

#some methods return boolean data

print(name.startswith("j"))
print(name.endswith("n"))