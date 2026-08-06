file = open("data.csv", "r")
new_file = open("new_data.csv", "w")

count = 0

for line in file:
    line = line.strip()

    if count == 0:
        new_file.write(line + ",Nationality\n")

    elif count == 1:
        new_file.write(line + ",Arabian\n")

    elif count == 2:
        new_file.write(line + ",British\n")

    elif count == 3:
        new_file.write(line + ",American\n")

    elif count == 4:
        new_file.write(line + ",Spanish\n")

    elif count == 5:
        new_file.write(line + ",French\n")

    elif count == 6:
        new_file.write(line + ",Pakistani\n")

    elif count == 7:
        new_file.write(line + ",Swedish\n")

    elif count == 8:
        new_file.write(line + ",Turkish\n")

    count += 1

file.close()
new_file.close()

print("Column added successfully")