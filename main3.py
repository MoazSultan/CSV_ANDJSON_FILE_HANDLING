import csv

class Student:

    def delete_column(self):

        f = open(r"C:\Users\HP\Desktop\module.csv", "r", newline='')

        reader = csv.reader(f, delimiter=',')

        data = []

        header = next(reader)

        col_name = input("Enter the column name to delete: ")

        if col_name not in header:
            print("Column not found.")
            f.close()
            return

        index = header.index(col_name)

        del header[index]
        data.append(header)

        for row in reader:
            del row[index]
            data.append(row)

        f.close()

        f = open(r"C:\Users\HP\Desktop\module.csv", "w", newline='')

        writer = csv.writer(f, delimiter=',')

        writer.writerows(data)

        f.close()

        print("Column deleted successfully.")

    def delete_row(self):
        f = open(r'C:\Users\HP\Desktop\module.csv', 'r', newline='')

        reader = csv.reader(f, delimiter=',')

        rows = []

        value = input("Enter the Roll no of student to Delete: ")
        header = next(reader)
        rows.append(header)

        for r in reader:
            if r[0] != value:
                rows.append(r)

        f.close()

        f2 = open(r'C:\Users\HP\Desktop\module.csv', 'w', newline='')
        writer = csv.writer(f2, delimiter=',')
        writer.writerows(rows)
        f2.close()
        print("Row deleted successfully.")




    def add_column(self):

        f = open(r'C:\Users\HP\Desktop\module.csv', 'r', newline='')

        reader = csv.reader(f)

        all = []

        row = next(reader)

        column = input("Enter the new column name: ")
        row.append(column)
        all.append(row)

        for row in reader:

            if not row:
                continue

            value = input("Enter value: ")
            row.append(value)
            all.append(row)

        f.close()

        f = open(r'C:\Users\HP\Desktop\module.csv', 'w', newline='')

        wo = csv.writer(f, delimiter=',')

        wo.writerows(all)

        f.close()

        print("Column added successfully.")

    def write_data(self):

        f = open(r'C:\Users\HP\Desktop\module.csv', 'w', newline='')

        wo = csv.writer(f, delimiter=',')

        list = []
        list.append(["Rollno", "Name", "Age", "Class", "Percentage"])

        num = int(input("Enter the number of students: "))
        for i in range(num):
            rn = input("Enter the student roll number: ")
            n = input("Enter the student name: ")
            a = int(input("Enter the student age: "))
            c = int(input("Enter the student Class: "))
            p = float(input("Enter the student percentage: "))
            list.append([rn, n, a, c, p])

        wo.writerows(list)

        f.close()

        print("Data written successfully.")

    def append_data(self):

        f = open(r'C:\Users\HP\Desktop\module.csv', 'r', newline='')

        reader = csv.reader(f, delimiter=',')

        header = next(reader)

        f.close()

        f = open(r'C:\Users\HP\Desktop\module.csv', 'a', newline='')

        wo = csv.writer(f, delimiter=',')

        num = int(input("Enter the number of students: "))

        data = []

        for i in range(num):

            row = []

            for column in header:
                value = input(f"Enter the student {column}: ")

                row.append(value)

            data.append(row)

        wo.writerows(data)

        f.close()

        print("Rows appended successfully.")


def main():

    s = Student()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Write Data")
        print("2. Append Data(Row)")
        print("3. Append Column")
        print("4. Delete Row")
        print("5. Delete Column")
        print("6. Exiting")

        choice = int(input("Enter your choice: "))

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
            print("Exiting...")
            break

        else:
            print("Invalid Choice")


main()