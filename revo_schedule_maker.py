import pandas as pd
from collections import defaultdict

# Load the updated CSV file
updated_file_path = "/Users/akatzman26/Downloads/Revo 25 Schedule - Main.csv"
df_updated = pd.read_csv(updated_file_path)

# Drop the second row (index 1) and rows without necessary columns
df_updated_cleaned = df_updated.drop(index=1)
df_filtered_updated = df_updated_cleaned.dropna(subset=["Task", "Sign Ups", "Start Time", "End Time"])

# Rebuild the ordered schedule
person_schedule_updated = defaultdict(list)

for _, row in df_filtered_updated.iterrows():
    task = row["Task"]
    start = row["Start Time"]
    end = row["End Time"]
    sign_ups = [name.strip() for name in str(row["Sign Ups"]).split(",")]
    time_range = f"{start}-{end}"
    
    for name in sign_ups:
        person_schedule_updated[name].append(f"{time_range} {task}")

# Create the DataFrame
schedule_df_updated = pd.DataFrame([
    {"Name": name, "Schedule": "\n".join(tasks)}
    for name, tasks in person_schedule_updated.items()
])

# Save the schedule to a CSV file
output_file = "/Users/akatzman26/Downloads/revo_schedule_output.csv"
schedule_df_updated.to_csv(output_file, index=False)
print(f"Schedule has been saved to {output_file}")
