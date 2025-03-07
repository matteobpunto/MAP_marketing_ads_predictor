# # --- IMPORT SECTION ---
import pandas as pd
# # --- END OF IMPORT SECTION ---

def count_empty_values(df: pd.DataFrame) -> tuple[int,float,int]:
    """
    Counts the number of empty values (empty strings or 'None') in a CSV file.
    """
    def is_empty(value):
        return pd.isna(value) or value == '' or value == 'None' or value == ' '
    empty_count = df.map(is_empty).sum().sum()

    total_values = df.size
    percentage = (empty_count / total_values * 100) if total_values > 0 else 0
    return empty_count, percentage, df.shape[0]

def remove_rows_with_empty_values(df: pd.DataFrame, output_file: str) -> tuple[int,float]:
    """
    Removes rows that contain empty values (empty strings or 'None') from a CSV file.
    """
    total_rows_before = df.shape[0]
    df_cleaned = df.replace({'': None, 'None': None}).dropna()
    total_rows_after = df_cleaned.shape[0]
    removed_rows = total_rows_before - total_rows_after
    removed_percentage = (removed_rows / total_rows_before * 100) if total_rows_before > 0 else 0
    df_cleaned.to_csv(output_file, index=False)
    return removed_rows, removed_percentage


# --- MAIN CODE ---
# Replace with the path to your CSV file
file_path = "Advertising_modified.csv"
df = pd.read_csv(file_path, dtype=str)

empty_values, empty_percentage, total_rows = count_empty_values(df)
print(f"Total rows: {total_rows}")
print(f"Empty values found: {empty_values} ({empty_percentage:.2f}%)")

# Replace with the name of the output file
output_file_path = "file_clear.csv"
removed_rows, removed_percentage = remove_rows_with_empty_values(df, output_file_path)
print(f"Rows removed: {removed_rows} ({removed_percentage:.2f}%)")
print(f"Cleaned file saved as: {output_file_path}")