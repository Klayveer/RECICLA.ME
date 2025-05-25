import os
import pandas as pd
import matplotlib.pyplot as plt

# Print the current working directory
print("Current working directory:", os.getcwd())

# Load the CSV file
file_path = 'CSV/data2024.csv'  # Ensure the correct file is specified
if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
    exit()

df = pd.read_csv(file_path)

# Remove any leading/trailing whitespace and extra quotes from column names
df.columns = df.columns.str.strip().str.replace('"', '')

# Rename columns if necessary
df.columns = df.columns.str.replace('Residuo', 'Resíduo')  # Correct the spelling

# Inspect the column names after cleaning
print("Column names after cleaning:", df.columns)

# Check if required columns exist
required_columns = ['Data', 'Tipo Resíduo', 'Peso']
for col in required_columns:
    if col not in df.columns:
        print(f"Error: '{col}' column not found in the DataFrame")
        print("Available columns:", df.columns)
        exit()

# Convert the "Data" column to datetime
df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d')

# Convert the "Peso" column to numeric, handling commas
df['Peso'] = df['Peso'].str.replace(',', '').astype(float)

# Set the font to Arial
#plt.rcParams['font.family'] = 'Arial'

# Disable scientific notation
plt.ticklabel_format(style='plain', useOffset=False, useLocale=False)

# Step 3: Create a plot for each "Tipo Resíduo"
unique_tipos = df['Tipo Resíduo'].unique()

for tipo in unique_tipos:
    tipo_df = df[df['Tipo Resíduo'] == tipo]
    
    # Resample the data by month and sum the weights
    tipo_df = tipo_df.set_index('Data').resample('M').sum().reset_index()
    
    plt.figure()
    plt.plot(tipo_df['Data'], tipo_df['Peso'])
    plt.title(f'{tipo} Peso vs Data (Monthly)')
    plt.xlabel('Data')
    plt.ylabel('Peso')
    plt.tight_layout()
    plt.savefig(f'{tipo}_monthly.png')

print("Plots created successfully.")
