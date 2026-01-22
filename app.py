import csv
import sys


def add_task(task):
    with open("data.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Task"] == task and row["Status"] == "0":
                print(f"Task '{task}' already exists with ID {row['ID']}.")
                return

    with open("data.csv", "r") as f:
        lines = f.readlines()
        last_line = lines[-1] if lines else "0"
        last_id = (
            int(last_line.split(",")[0]) if last_line.strip() != "ID,Task,Status" else 0
        )

    new_id = last_id + 1
    with open("data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_id, task, 0])

    print(f"Task added successfully with ID {new_id}")


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 2:
        sys.exit(1)

    op = args[0]
    task = " ".join(args[1:])

    if op == "add":
        add_task(task)
