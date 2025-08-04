# Create a new dictionary to maintain insertion order of tasks
person_schedule_ordered = defaultdict(list)

# Go through each row in order and append tasks in that order
for _, row in df_filtered.iterrows():
    task = row["Task"]
    start = row["Start Time"]
    end = row["End Time"]
    sign_ups = [name.strip() for name in str(row["Sign Ups"]).split(",")]
    time_range = f"{start}-{end}"

    for name in sign_ups:
        person_schedule_ordered[name].append(f"{time_range} {task}")

# Convert to DataFrame preserving original order
schedule_df_ordered = pd.DataFrame(
    [
        {"Name": name, "Schedule": "\n".join(tasks)}
        for name, tasks in person_schedule_ordered.items()
    ]
)

tools.display_dataframe_to_user(
    name="Ordered Individual Schedules", dataframe=schedule_df_ordered
)
