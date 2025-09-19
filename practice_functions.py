def count_vowels(string):
    count=0
    for i in range(len(string)):
        if string[i] in "aeiouy":
            count+=1
    return count
print(count_vowels("Sera!"))

def count_consonants(string):
    count=0
    for i in range(len(string)):
        if string[i] not in "aeiouy":
            count+=1
    return count
print(count_consonants("Dumbass"))
                   

