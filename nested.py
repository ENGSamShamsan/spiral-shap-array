# Ask the user to enter the number of the rows or columns
# Numbers of row and colums should be the same for the square shape
# Make sure to parse your entry to integer
n = int(input("enter the size of the list "))
# Then create a nested list with the length of the number entered
nested_list= [[0 for i in range(n)] for j in range(n)]
# Finally Print it in a square shape
low=0
high=n-1
x=1
levels=int((n+1)/2)
for level in range(levels):
    for i in range(low,high+1):
        nested_list[level][i]= x
        x+=1
        
    for i in range(low+1,high+1):
        nested_list[i][high]= x
        x+=1
        
    for i in range(high-1,low-1,-1):
        nested_list[high][i]= x
        x+=1
        
    for i in range(high-1,low,-1):
        nested_list[i][low]= x
        x+=1
        
    low+=1
    high-=1
    
for i in range(n):
    for j in range(n):
        print(nested_list[i][j],end="\t")# print the row elements with
        # a tab space after each element
    print()# Print in new line after each row

