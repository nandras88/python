from collections import Counter
print('\n 1. feladat ...\n')
name = "Andras"
age = 32
fav_fruit = "citrom"
print('Sziasztok, %s vagyok %d eves\nA kedvenc gyumolcsom a %s' %
      (name, age, fav_fruit))

print('\n 2. feladat ...\n')
i = 0
text = "FOR:Nem fogok csalni a vizsgan\n"
for i in range(100):
    print(text)

i = 0
string = "WHILE :Nem fogok csalni a vizsgan\n"
while i < 100:
    print(string)
    i = i + 1

print('\n 3. feladat ...\n')
i = 0
for i in range(100):
    if i % 3 == 0:
        print("PIFF")
    elif i % 7 == 0:
        print("PAFF")
    elif i % 3 & i % 7 == 0:
        print("PIFF PAFF")

print('\n 4. feladat ...\n')
i = 0
rows = 8
for i in range(rows):
    print(' '*(rows-i-1) + '*'*(2*i+1))

print('\n 5. feladat ...\n')
inputarray = [4, 5, 6, 7, 8]


def avarage(inputarray):
    return sum(inputarray) / len(inputarray)


result = avarage(inputarray)
print('Az atlag %d\n' % (result))

"""
print('\n 6. feladat ...\n')
def printMatrix(mat):

    for i in range(0, len(mat)):
        for j in range(0, len(mat)):

            print(mat[i][j], end=" ")
        print("")


test = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


def transposeMatrix(mat):
    for i in range(0, len(mat)):
        for j in range(i, len(mat)):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp


def reverseColums(mat):
    k = len(mat)-1
    for i in range(0, len(mat)):
        for j in range(0, k):
            temp = mat[j][i]
            mat[j][i] = mat[k][i]
            mat[k][i] = temp
            k = k - 1


print(len(test))
transposeMatrix(test)
reverseColums(test)
printMatrix(test)
"""

print('\n 7. feladat ...\n')


def mostComonCharacters(inputStr):
    characters = inputStr.lower()
    dictionary = {}
    for letters in characters:
        if letters in dictionary:
            dictionary[letters] += 1
        else:
            dictionary[letters] = 1
    topThree = Counter(dictionary).most_common(3)
    for i in topThree:
        print(i[0], " :", i[1], " ")


name = "almaretekmogyor"
mostComonCharacters(name)

print('\n 8. feladat ...\n')


def palindrome(input):
    length = len(input)
    palindromes = []
    for i in range(1, length+1):
        min = 0
        while (min+i) < length+1:
            if(input[min:(min+i)] == input[min:(min+i)][::-1]) and len(input[min:(min+i)]) >= 3:
                palindromes.append(input[min:(min+i)])
            min = min+1
    return palindromes


print(palindrome("dog goat dad duck doodle never"))
print(palindrome("racecar"))

print('\n 9. feladat ...\n')
num = 153
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "Armstrong number")
else:
    print(num, "not an Armstrong number")
