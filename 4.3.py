def count(file_path):
    frequencies = {}
    total_letters = 0

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            for char in line.lower():
                if char.isalpha():
                    total_letters += 1
                    frequencies[char] = frequencies.get(char, 0) + 1

    for char in frequencies:
        frequencies[char] = frequencies[char] / total_letters

    return frequencies

print("Первый файл")
file_path = "/home/stud/local_git/PSA_DZ3/zadanie3.1.txt"  
frequencies1 = count(file_path)
print(frequencies1)

print("Второй файл")
file_path2 = "/home/stud/local_git/PSA_DZ3/zadanie3.2.txt"  
frequencies2 = count(file_path2)
print(frequencies2)

print("Третий файл")
file_path3 = "/home/stud/local_git/PSA_DZ3/zadanie3.3.txt"  
frequencies3 = count(file_path3)
print(frequencies3)
