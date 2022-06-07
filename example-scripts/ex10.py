print "I am 6'2\" tall."  # escape double-quote inside string
print 'I am 6\'2" tall.'  # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# The only reason you might need """ instead of '''(or vice versa) is if the string iteself contains a triple quote.
# If a string contains both triple-single-quotes and triple-double-quotes, then you will have to escape one of them.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies """
\t* Catnip\n\t* Grass
'''
