import csv


class Student:

    def __init__(self):
        self.filename = r"C:\Users\HP\Desktop\module.csv"



    def read_file(self):

        f = open(self.filename, "r", newline='')

        reader = csv.reader(f)

        data = []

        for row in reader:
            data.append(row)

        f.close()

        return data

    def write_file(self, data):

        f = open(self.filename, "w", newline='')

        writer = csv.writer(f)

        writer.writerows(data)

        f.close()

    def display_data(self):

        data = self.read_file()

        print()

        for row in data:
            for value in row:
                print(f"{value:<15}", end="")
            print()


    def write_data(self):

        data = []

        header = ["Rollno", "Name", "Age", "Class", "Percentage"]

        data.append(header)

        num = int(input("Enter the number of students: "))

        for i in range(num):

            rn = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            clas = input("Enter Class: ")
            per = input("Enter Percentage: ")

            data.append([rn, name, age, clas, per])

        self.write_file(data)

        print("Data written successfully.")



    def append_data(self):

        data = self.read_file()

        header = data[0]

        num = int(input("Enter the number of students: "))

        for i in range(num):

            row = []

            for column in header:

                value = input(f"Enter {column}: ")

                row.append(value)

            data.append(row)

        self.write_file(data)

        print("Rows appended successfully.")



    def add_column(self):

        data = self.read_file()

        header = data[0]

        column = input("Enter new column name: ")

        if column in header:
            print("Column already exists.")
            return

        header.append(column)

        for row in data[1:]:

            value = input(f"Enter value for Roll No {row[0]}: ")

            row.append(value)

        self.write_file(data)

        print("Column added successfully.")



    def delete_row(self):

        data = self.read_file()

        roll = input("Enter Roll Number to delete: ")

        new_data = []

        new_data.append(data[0])

        found = False

        for row in data[1:]:

            if row[0] != roll:
                new_data.append(row)
            else:
                found = True

        if found:
            self.write_file(new_data)
            print("Row deleted successfully.")
        else:
            print("Roll Number not found.")



    def delete_column(self):

        data = self.read_file()

        header = data[0]

        column = input("Enter column name to delete: ")

        if column not in header:
            print("Column not found.")
            return

        index = header.index(column)

        for row in data:

            del row[index]

        self.write_file(data)

        print("Column deleted successfully.")



    def update_row(self):

        data = self.read_file()

        header = data[0]

        roll = input("Enter Roll Number to update: ").strip()

        target_row = None

        for row in data[1:]:
            if row[0].strip().lower() == roll.lower():
                target_row = row
                break

        if target_row is None:
            print("Roll Number not found.")
            return

        print("\nCurrent Data:")

        for i in range(len(header)):
            print(f"{i + 1}. {header[i]}: {target_row[i]}")

        # lowercase-name -> actual index, so lookups are case/space tolerant
        header_lookup = {h.strip().lower(): i for i, h in enumerate(header)}

        print("\nEnter the column name to update (or 'done' to finish):")

        while True:

            column = input("\nColumn name: ").strip()

            if column.lower() == "done":
                break

            key = column.lower()

            if key not in header_lookup:
                print("Column not found. Check spelling and try again.")
                continue

            index = header_lookup[key]
            actual_name = header[index]

            new_value = input(f"Enter new value for {actual_name} [{target_row[index]}]: ")

            if new_value != "":
                target_row[index] = new_value
                print(f"{actual_name} updated.")
            else:
                print("No change (empty value).")

        self.write_file(data)
        print("Row updated successfully.")



def main():

    s = Student()

    while True:

        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Write Data")
        print("2. Append Data (Row)")
        print("3. Append Column")
        print("4. Delete Row")
        print("5. Delete Column")
        print("6. Display CSV Data")
        print("7. Update Row")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            s.write_data()

        elif choice == 2:
            s.append_data()

        elif choice == 3:
            s.add_column()

        elif choice == 4:
            s.delete_row()

        elif choice == 5:
            s.delete_column()

        elif choice == 6:
            s.display_data()

        elif choice == 7:
            s.update_row()

        elif choice == 8:
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


main()