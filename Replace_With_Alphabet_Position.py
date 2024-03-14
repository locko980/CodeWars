def alphabet_position(text):
    NUM = 31
    result = ''
    
    for i in text:
        if i == "." or i==" ":
            continue
        result += f'{(ord(i) & NUM)}' + " "
    
    return result
        
print(alphabet_position("The sunset sets at twelve o' clock."))

# NUM = 31
  
# # Function to calculate the position
# # of characters
# def positions(str):
#     for i in str:
          
#         # Performing AND operation
#         # with number 31
#         print((ord(i) & NUM), end =" ")
  
# # Driver code
# str = "The sunset sets at twelve o' clock."
# positions(str)