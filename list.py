n = int(input("Enter number of operation you want to make:"))
list = []

print("insert i e: Insert integer e at position i. \nprint: Print the list. \nremove e: Delete the first occurrence of integer e. \nappend e: Insert integer e at the end of the list. \nsort: Sort the list. \nreverse: Reverse the list.")

for index in range (n):
    str  = input("enter operation : ")
    if str == 'insert':
        loc,integer = input("enter location and integer : " ).split()
        list.insert(int(loc),int(integer))
    if str == 'print':
        print(list)
    if str == 'append':
        integer = int(input("enter integer : "))
        list.append(integer)
    if str == 'remove':
        integer = int(input("enter integer : "))
        list.remove(integer)
    if str == 'sort':
        list.sort()
    if str == 'reverse':
         list.reverse()