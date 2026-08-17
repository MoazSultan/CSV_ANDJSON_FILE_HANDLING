import json


class JSONManager:

    def __init__(self):
        self.filename = r"C:\Users\HP\Desktop\data.json"



    def read_file(self):

        try:
            f = open(self.filename, "r")
            data = json.load(f)
            f.close()
        except FileNotFoundError:
            data = {}
        except json.JSONDecodeError:
            data = {}

        return data

    def write_file(self, data):

        f = open(self.filename, "w")

        json.dump(data, f, indent=4)

        f.close()

    def display_data(self):

        data = self.read_file()

        print()

        print(json.dumps(data, indent=4))

        print()



    def parse_path(self, path_input):
        """Split a path like 'University / CS/ ' into clean, non-empty
        segments: ['University', 'CS']. Strips whitespace around each
        segment and drops empty ones caused by leading/trailing/double
        slashes."""

        raw_parts = path_input.split("/")

        clean_parts = [p.strip() for p in raw_parts if p.strip() != ""]

        return clean_parts



    def get_nested_value(self, data, path_list):

        current = data

        for key in path_list:

            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None

        return current



    def set_nested_value(self, data, path_list, value):

        current = data

        for key in path_list[:-1]:

            if key not in current:
                current[key] = {}

            current = current[key]

        current[path_list[-1]] = value

        return data



    def delete_nested_value(self, data, path_list):

        current = data

        for key in path_list[:-1]:

            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return False

        last_key = path_list[-1]

        if last_key in current:
            del current[last_key]
            return True

        return False



    def write_data(self):

        data = {}

        num_level1 = int(input("Enter number of Level 1 keys (e.g., University, College): "))

        for i in range(num_level1):

            level1_key = input("Enter Level 1 key name: ")

            data[level1_key] = {}

            num_level2 = int(input(f"  Enter number of Level 2 keys inside '{level1_key}': "))

            for j in range(num_level2):

                level2_key = input(f"    Enter Level 2 key name: ")

                data[level1_key][level2_key] = {}

                num_level3 = int(input(f"      Enter number of Level 3 keys inside '{level2_key}': "))

                for k in range(num_level3):

                    level3_key = input(f"        Enter Level 3 key name: ")

                    data[level1_key][level2_key][level3_key] = {}

                    num_level4 = int(input(f"          Enter number of Level 4 items inside '{level3_key}': "))

                    for m in range(num_level4):

                        item_key = input(f"            Enter item key name: ")
                        item_value = input(f"            Enter item value: ")

                        data[level1_key][level2_key][level3_key][item_key] = item_value

        self.write_file(data)

        print("JSON data written successfully.")

    def add_data(self):

        data = self.read_file()

        print("\nEnter path where to add data (e.g., University/CS/Semester1)")
        path_input = input("Enter path: ")

        path_list = self.parse_path(path_input)

        if len(path_list) < 1:
            print("Invalid path.")
            return

        key_name = input("Enter new key name to add: ")
        key_value = input("Enter value for this key: ")

        target = self.get_nested_value(data, path_list)

        if target is None:
            print("Path not found.")
            return

        if not isinstance(target, dict):
            print("Cannot add data here because this path is not an object.")
            return

        if key_name in target:
            print("Key already exists.")
            return

        target[key_name] = key_value

        self.write_file(data)

        print("Data added successfully.")



    def add_object(self):

        data = self.read_file()

        print("\nEnter parent path where to add the object (e.g., University/CS/Semester1)")
        print("Leave blank to add it at the top level.")
        path_input = input("Enter path: ")

        path_list = self.parse_path(path_input)

        # Empty path means "add at root" - a deliberate choice, not a typo.
        if path_list:
            target = self.get_nested_value(data, path_list)

            if target is None:
                print("Parent path not found. Create it first (or check spelling).")
                return

            if not isinstance(target, dict):
                print("Cannot add an object here because this path is not an object.")
                return
        else:
            target = data

        obj_name = input("Enter object name to create: ")

        if obj_name in target:
            confirm = input(
                f"'{obj_name}' already exists here and has data under it. "
                f"Overwrite it and everything inside it? (y/n): "
            )
            if confirm.strip().lower() != "y":
                print("Cancelled. No changes made.")
                return

        num_items = int(input("Enter number of key-value pairs inside this object: "))

        new_obj = {}

        for i in range(num_items):

            k = input(f"  Enter key {i+1}: ")
            v = input(f"  Enter value {i+1}: ")

            new_obj[k] = v

        target[obj_name] = new_obj

        self.write_file(data)

        print("Object added successfully.")



    def update_data(self):

        data = self.read_file()

        print("\nEnter path to data you want to change (e.g., University/CS/Semester1/Ali)")
        path_input = input("Enter path: ")

        path_list = self.parse_path(path_input)

        if len(path_list) < 1:
            print("Invalid path.")
            return

        current_value = self.get_nested_value(data, path_list)

        if current_value is None:
            print("Path not found.")
            return

        if isinstance(current_value, dict):
            print(f"\nThis path points to a whole object, not a single value:")
            print(json.dumps(current_value, indent=4))
            confirm = input(
                "\nReplacing it will DELETE everything inside it and replace it "
                "with a single text value. Continue? (y/n): "
            )
            if confirm.strip().lower() != "y":
                print("Cancelled. No changes made.")
                return
        else:
            print(f"\nCurrent value at this path: {current_value}")

        new_value = input("Enter new value: ")

        data = self.set_nested_value(data, path_list, new_value)

        self.write_file(data)

        print("Data updated successfully.")



    def delete_data(self):

        data = self.read_file()

        print("\nEnter path to delete (e.g., University/CS/Semester1/Ali)")
        path_input = input("Enter path: ")

        path_list = self.parse_path(path_input)

        if len(path_list) < 1:
            print("Invalid path.")
            return

        result = self.delete_nested_value(data, path_list)

        if result:
            self.write_file(data)
            print("Data deleted successfully.")
        else:
            print("Path not found.")



    def read_path(self):

        data = self.read_file()

        print("\nEnter path to read (e.g., University/CS/Semester1)")
        path_input = input("Enter path: ")

        path_list = self.parse_path(path_input)

        if len(path_list) < 1:
            print("Invalid path.")
            return

        value = self.get_nested_value(data, path_list)

        if value is None:
            print("Path not found.")
        else:
            print(f"\nValue at path '{'/'.join(path_list)}':")
            if isinstance(value, dict):
                print(json.dumps(value, indent=4))
            else:
                print(value)



def main():

    j = JSONManager()

    while True:

        print("\n========== JSON MANAGEMENT SYSTEM ==========")
        print("1. Write Data (Fresh JSON)")
        print("2. Add Data at Specific Path")
        print("3. Add Object at Specific Path")
        print("4. Update Data at Path")
        print("5. Delete Data at Path")
        print("6. Read Data at Path")
        print("7. Display Full JSON")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            j.write_data()

        elif choice == 2:
            j.add_data()

        elif choice == 3:
            j.add_object()

        elif choice == 4:
            j.update_data()

        elif choice == 5:
            j.delete_data()

        elif choice == 6:
            j.read_path()

        elif choice == 7:
            j.display_data()

        elif choice == 8:
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


main()