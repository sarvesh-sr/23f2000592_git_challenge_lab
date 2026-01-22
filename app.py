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


def list_tasks():
    with open("data.csv", "r") as f:
        reader = csv.DictReader(f)
        print(f"{'ID':<5} {'Task':<20} {'Status':<10}")
        print("-" * 35)
        for row in reader:
            status = "Done" if row["Status"] == "1" else "Pending"
            print(f"{row['ID']:<5} {row['Task']:<20} {status:<10}")


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 1:
        sys.exit(1)

    op = args[0]

    if op in ["add", "-a"] and len(args) >= 2:
        task = " ".join(args[1:])
        add_task(task)
    elif op in ["list", "-l"]:
        list_tasks()
