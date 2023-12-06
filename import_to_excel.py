import argparse
from pathlib import Path
import pandas as pd

def import_data(file_path, num_columns, output_title, force_overwrite):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Read the header to determine the number of columns
        header = lines[0].strip().split()
        actual_num_columns = len(header)

        if num_columns is not None and actual_num_columns != num_columns:
            print(f"Error: Specified number of columns ({num_columns}) does not match the actual number of columns ({actual_num_columns})")
            return

        # Read the rest of the file into a DataFrame
        df = pd.DataFrame([line.strip().split() for line in lines[1:]], columns=header)

        # Determine the output title
        output_title = output_title or Path(file_path).stem

        # Write the DataFrame to an Excel file with the openpyxl engine
        output_file = f"{output_title}.xlsx"

        # Check if the file already exists
        if Path(output_file).exists():
            if force_overwrite:
                print(f"Overwriting existing file '{output_file}'.")
            else:
                user_input = input(f"File '{output_file}' already exists. Do you want to overwrite it? (y/n): ").lower()
                if user_input != 'y':
                    new_output_file = input("Enter a new file name: ")
                    output_file = f"{new_output_file}.xlsx"

        df.to_excel(output_file, index=False, engine='openpyxl')

        print(f"Data successfully imported and written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Import data from CSV or space-separated files to Excel.")
    parser.add_argument("file", nargs="?", help="Path to the input file (CSV or space-separated).")
    parser.add_argument("-c", "--columns", type=int, help="Number of columns in the file (optional).")
    parser.add_argument("-o", "--output", help="Output title for the Excel file (optional).")
    parser.add_argument("-f", "--force", action="store_true", help="Force overwrite without prompting.")

    args = parser.parse_args()

    if not args.file or args.columns is None:
        parser.print_usage()
        return

    import_data(args.file, args.columns, args.output, args.force)

if __name__ == "__main__":
    main()