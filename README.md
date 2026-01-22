# Todo CLI

A simple todo app to manage tasks via the command line.

## Usage

### Add a task
```bash
python3 app.py add <task name>
# or
python3 app.py -a <task name>
```

### List tasks
```bash
# List pending tasks (newest first)
python3 app.py list
# or
python3 app.py -l

# List all tasks including completed
python3 app.py list -a
# or
python3 app.py -al
```

### Mark task as completed
```bash
python3 app.py done <task id>
# or
python3 app.py -d <task id>
```

### Mark task as pending (undone)
```bash
python3 app.py undone <task id>
# or
python3 app.py -u <task id>
```
