#for this game we will use string concatenation

madlib1="\nMake sure your lunch (container) is filled with nutritious (adjective1) food. \
Do not go to the (adjective2) food stand across the street from school. \
The hamburgers they serve are fried in (noun1) and are made of (noun2) meat.\n "
print(madlib1)

con=input("container:")
adj=input("adjective1:")
adj2=input("adjective2:")
noun=input("noun1:")
noun2=input("noun2:")
madlib=f"Make sure your lunch {con} is filled with nutritious {adj} food. \
Do not go to the {adj2} food stand across the street from school. \
The hamburgers they serve are fried in {noun} and are made of {noun2} meat. "
print(madlib)