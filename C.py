l = str
list = []

for i in range(4):
    l=str(input())
    l_new = str(l).replace('-', '').replace('(', '').replace(')', '').replace('+7', '8').replace('495', '').replace('8', '') #Parsing initial string
    list.append(l_new) #Creating a list of new (parsed) strings 
for j in range(1,4):
    if list[0] == list[j]: #Comparing second, third and fourth strings in the list with the first one
        list[j] = 'YES'
    else:
        list[j] = 'NO'
    print(list[j])
