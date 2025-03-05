# # --- IMPORT SECTION ---
# import csv
# # --- END OF IMPORT SECTION ---
#
#
# # Function to count empty values (empty strings or 'None') in a CSV file
# def count_empty_values(csv_file):
#     """
#        Counts the number of empty values (empty strings or 'None') in a CSV file.
#
#        """
#     count = 0
#     total_values = 0
#     with open("Advertising_modified.csv", newline='', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             total_values += len(row)
#             for elem in row:
#                 if elem.strip() == '':
#                     count += 1
#
#
#     percentage = (count / total_values * 100) if total_values > 0 else 0
#     return count, percentage
# # Function to remove rows containing empty values or 'None'
# def remove_rows_with_empty_values(input_file, output_file):
#     """
#        Removes rows that contain empty values (empty strings or 'None') from a CSV file.
#     """
#
#     rows = []
#     with open("Advertising_modified.csv", newline='', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             keep_row = True
#             for cell in row:
#                 if not cell.strip() or cell.strip().lower() == 'none':
#                     keep_row = False
#                     break
#             if keep_row:
#                 rows.append(row)
#
#     with open("Advertising_clear.csv", mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerows(rows)
#
# # --- MAIN CODE ---
# # Example usage
# file_path = "your_file.csv"  # Replace with the path to your CSV file
# empty_values, empty_percentage = count_empty_values(file_path)
# print(f"Empty values found: {empty_values} ({empty_percentage:.2f}%)")
#
# output_file_path = "file_pulito.csv"  # Replace with the name of the output file
# remove_rows_with_empty_values(file_path, output_file_path)
# print(f"Cleaned file saved as: {output_file_path}")


import pandas as pd

def count_empty_values(csv_file):
    """
    Counts the number of empty values (empty strings or 'None') in a CSV file.
    """
    df = pd.read_csv(csv_file, dtype=str)  # Read as string to avoid conversion issues
    empty_count = df.isin(['', 'None']).sum().sum()
    total_values = df.size
    percentage = (empty_count / total_values * 100) if total_values > 0 else 0
    return empty_count, percentage, df.shape[0]  # Also return total row count

def remove_rows_with_empty_values(input_file, output_file):
    """
    Removes rows that contain empty values (empty strings or 'None') from a CSV file.
    """
    df = pd.read_csv(input_file, dtype=str)  # Read as string to preserve 'None' values
    total_rows_before = df.shape[0]
    df_cleaned = df.replace({'': None, 'None': None}).dropna()
    total_rows_after = df_cleaned.shape[0]
    removed_rows = total_rows_before - total_rows_after
    removed_percentage = (removed_rows / total_rows_before * 100) if total_rows_before > 0 else 0
    df_cleaned.to_csv(output_file, index=False)
    return removed_rows, removed_percentage

# --- MAIN CODE ---
file_path = "Advertising_modified.csv"  # Replace with the path to your CSV file
empty_values, empty_percentage, total_rows = count_empty_values(file_path)
print(f"Total rows: {total_rows}")
print(f"Empty values found: {empty_values} ({empty_percentage:.2f}%)")

output_file_path = "file_clear.csv"  # Replace with the name of the output file
removed_rows, removed_percentage = remove_rows_with_empty_values(file_path, output_file_path)
print(f"Rows removed: {removed_rows} ({removed_percentage:.2f}%)")
print(f"Cleaned file saved as: {output_file_path}")