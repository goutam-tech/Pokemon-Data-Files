# The code snippet `import pandas as pd`, `import glob`, and `import os` are importing necessary
# Python libraries for the script to work. Here is what each import statement does:
import pandas as pd
import glob
import os

# The line `excel_files = glob.glob("./DB_Create/report/*.xlsx")` is using the `glob` module to search
# for all files with a `.xlsx` extension in the directory `./DB_Create/report/`. It returns a list of
# file paths that match the specified pattern, which are then stored in the `excel_files` variable for
# further processing in the script.
excel_files = glob.glob("./DB_Create/report/XLSX/*.xlsx")

# This `for` loop iterates over each file path in the `excel_files` list, reads the Excel file using
# `pd.read_excel(file)`, extracts the base name of the file, and then proceeds to convert the data
# into CSV and SQL formats.
for file in excel_files:
    df = pd.read_excel(file)

    base_name = os.path.splitext(os.path.basename(file))[0]

    csv_file = f"./DB_Create/report/CSV/{base_name}.csv"
    df.to_csv(csv_file, index=False)

    sql_file = f"./DB_Create/report/SQL/{base_name}.sql"
    table_name = base_name.lower()

    with open(sql_file, "w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            columns = ", ".join(df.columns)
            values = []
            for v in row.values:
                if pd.isna(v):
                    values.append("NULL")
                elif isinstance(v, (int, float)):
                    values.append(str(v))
                else:
                    values.append(f"'{str(v)}'")
            values_str = ", ".join(values)
            f.write(f"INSERT INTO {table_name} ({columns}) VALUES ({values_str});\n")

    print(f"Converted {file} → {csv_file}, {sql_file}")

print("All Excel files converted to CSV and SQL successfully.")