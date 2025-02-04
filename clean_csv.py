import pandas as pd

def remove_duplicates(csv_file, output_file):
    try:
        # Load CSV into a DataFrame
        df = pd.read_csv(csv_file)

        # Remove duplicate rows (keeping the first occurrence)
        df_cleaned = df.drop_duplicates(subset=['URL'])

        # Save the cleaned DataFrame to a new CSV file
        df_cleaned.to_csv(output_file, index=False)

        print(f"Duplicates removed. Cleaned file saved as '{output_file}'.")
    except Exception as e:
        print(f"Error processing CSV: {e}")

# Example usage
input_csv = "teste_erros5_data.csv"  # Replace with your input CSV file
output_csv = "sem_duplicados_data.csv"  # Output file without duplicates
remove_duplicates(input_csv, output_csv)