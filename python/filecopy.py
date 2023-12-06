def copy_and_convert_to_uppercase(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            content = input_file.read()

        uppercase_content = content.upper()

        with open(output_file_path, 'w') as output_file:
            output_file.write(uppercase_content)

        print(f"Content successfully copied to {output_file_path}")

    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Unable to read or write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


try:
    input_file_path = input("Enter the path of the input file: ")
    output_file_path = input("Enter the path of the output file: ")

    copy_and_convert_to_uppercase(input_file_path, output_file_path)

except KeyboardInterrupt:
    print("\nOperation aborted by the user.")
