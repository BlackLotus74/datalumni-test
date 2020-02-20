"""
Python program to print all Prime numbers in an Interval
If num is divisible by any number between 2 and val, it is not prime
"""
arrayPrimaryNumber = []   #mettre nombre premiers dans une liste
for num in range(2, 1001):
    if num > 1:
        for i in range(2, num):
            if(num % i)==0:
                break
        else: 
            arrayPrimaryNumber.append(num)

"""
deleting a string object in a list based on the length 
[to add a slice]
"""

for i in arrayPrimaryNumber[:]:  #nombre composé moins de 2 chiffres plus dans la liste
        if len(str(i)) < 2:
            arrayPrimaryNumber.remove(i)


"""
Remove element from given list containing specific digits
[Using List comprehension and any() function]
"""
numbersToDelete = ['1', '7']   #on enleve les 1 et 7
Output = [a for a in arrayPrimaryNumber if not  
          any(b in numbersToDelete for b in str(a))] #list en intension


"""
find the sum of the elements of the list
"""
mystery_number=[x for x in Output if sum(list(map(int,str(x))))<11]
print(mystery_number)



#mystery_number = # TODO

#print(f'Le nombre mystère est le : {mystery_number}')