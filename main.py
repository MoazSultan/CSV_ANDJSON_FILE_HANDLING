class FileHandler:

    # Read a file
    def read_file(self, filename):
        try:
            file = open(filename, "r")

            for line in file:
                print(line.strip())

            file.close()

        except FileNotFoundError:
            print("File not found.")

    # Write to a file (overwrite)
    def write_file(self, filename, text):
        file = open(filename, "w")
        file.write(text)
        file.close()

        print("Data written successfully.")

    # Append to a file
    def append_file(self, filename, text):
        file = open(filename, "a")
        file.write(text)
        file.close()

        print("Data appended successfully.")

    # Add a row to CSV
    def add_row(self, filename, row):
        file = open(filename, "a")
        file.write("\n" + row)
        file.close()

        print("Row added successfully.")

    # Add a column to CSV
    def add_column(self, filename, column_name, values):

        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        # Remove blank lines
        clean_lines = []

        for line in lines:
            line = line.strip()

            if line != "":
                clean_lines.append(line)

        # Check if column already exists
        header = clean_lines[0]

        if column_name in header.split(","):
            print("Column already exists.")
            return

        file = open(filename, "w")

        count = 0

        for line in clean_lines:

            if count == 0:
                file.write(line + "," + column_name + "\n")

            else:

                if count - 1 < len(values):
                    file.write(line + "," + values[count - 1] + "\n")
                else:
                    file.write(line + ",Unknown\n")

            count += 1

        file.close()

        print("Column added successfully.")


# ---------------- MAIN PROGRAM ----------------

handler = FileHandler()

while True:

    print("\n========== FILE MENU ==========")
    print("1. Read File")
    print("2. Write File")
    print("3. Append File")
    print("4. Add Row to CSV")
    print("5. Add Column to CSV")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        filename = input("Enter filename: ")
        handler.read_file(filename)

    elif choice == "2":

        filename = input("Enter filename: ")
        text = input("Enter text: ")

        handler.write_file(filename, text)

    elif choice == "3":

        filename = input("Enter filename: ")
        text = input("Enter text to append: ")

        handler.append_file(filename, text)

    elif choice == "4":

        filename = input("Enter CSV filename: ")

        print("\nEnter complete row separated by commas.")
        print("Example:")
        print("110,John,22,Male,AI,5,3.75,London")

        row = input("Row: ")

        handler.add_row(filename, row)

    elif choice == "5":

        filename = input("Enter CSV filename: ")
        column_name = input("Enter new column name: ")

        print("\nEnter one value for each student.")
        print("Type DONE when finished.\n")

        values = []

        while True:

            value = input("Value: ")

            if value.upper() == "DONE":
                break

            values.append(value)

        handler.add_column(filename, column_name, values)

    elif choice == "6":

        print("Program exited.")
        break

    else:

        print("Invalid choice.")