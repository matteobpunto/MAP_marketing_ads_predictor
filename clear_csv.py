# --- IMPORT SECTION ---
import csv
# --- END OF IMPORT SECTION ---


# Function to count empty values (empty strings or 'None') in a CSV file
def count_empty_values(csv_file):
    """
       Counts the number of empty values (empty strings or 'None') in a CSV file.

       """
    count = 0
    total_values = 0
    with open("Advertising_modified.csv", newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            total_values += len(row)
            for elem in row:
                if elem.strip() == '':
                    count += 1


    percentage = (count / total_values * 100) if total_values > 0 else 0
    return count, percentage
# Function to remove rows containing empty values or 'None'
def remove_rows_with_empty_values(input_file, output_file):
    """
       Removes rows that contain empty values (empty strings or 'None') from a CSV file.
    """

    rows = []
    with open("Advertising_modified.csv", newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            keep_row = True
            for cell in row:
                if not cell.strip() or cell.strip().lower() == 'none':
                    keep_row = False
                    break
            if keep_row:
                rows.append(row)

    with open("Advertising_clear.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# --- MAIN CODE ---
# Example usage
file_path = "your_file.csv"  # Replace with the path to your CSV file
empty_values, empty_percentage = count_empty_values(file_path)
print(f"Empty values found: {empty_values} ({empty_percentage:.2f}%)")

output_file_path = "file_pulito.csv"  # Replace with the name of the output file
remove_rows_with_empty_values(file_path, output_file_path)
print(f"Cleaned file saved as: {output_file_path}")



