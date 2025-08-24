# Step 1: Write user input to a file
text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append additional data
extra_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(extra_text + "\n")
print("Data successfully appended.")

# Step 3: Read and display final content
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())