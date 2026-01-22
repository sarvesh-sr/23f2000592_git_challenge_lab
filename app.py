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


def list_tasks(show_all=False):
    with open("data.csv", "r") as f:
        reader = list(csv.DictReader(f))

    print(f"{'ID':<5} {'Task':<20} {'Status':<10}")
    print("-" * 35)

    for row in reversed(reader):
        if not show_all and row["Status"] == "1":
            continue

        status = "Done" if row["Status"] == "1" else "Pending"
        print(f"{row['ID']:<5} {row['Task']:<20} {status:<10}")


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 1:
        sys.exit(1)

    op = args[0]

    if op == "add" or (op == "-a" and len(args) >= 2):
        task = " ".join(args[1:])
        add_task(task)
    elif op == "list" or (op.startswith("-") and "l" in op):
        show_all = "-a" in args[1:] or (op.startswith("-") and "a" in op and op != "-a")
        list_tasks(show_all)
