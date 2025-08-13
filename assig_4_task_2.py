user_input = input("Enter text to write to the file: ")
file = open("output.txt", "w")
file.write(user_input + "\n")
print("Data successfully written to output.txt\n")
file.close()

additional = input("Enter additional text to append: ")
file = open("output.txt", "a")
file.write(additional + "\n")
print("Data successfully appended")
file.close()

print("Final content of output.txt")
file1 = open("output.txt", "r")
for line in file1:
    print(line.strip())
file1.close()
