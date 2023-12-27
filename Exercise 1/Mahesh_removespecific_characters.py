################
Strings Functions
Coding with Strings Functions to remove specific characters  By: Sai Mahesh
25DEC2023
#####

#Delete a certain character 
text_with_brackets = "(IaC is the course for python programming)"
text_without_brackets = text_with_brackets.strip ('(')
text_without_brackets = text_without_brackets.strip (')')
print(text_without_brackets)