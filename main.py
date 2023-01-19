import pandas as pd
import os

SAVE_FILE = "data.csv"

tasks = pd.Series(dtype="str")
if os.path.isfile(SAVE_FILE):
	data = pd.read_csv(SAVE_FILE, header=0, index_col=0)
	tasks = pd.Series([i for _, i in data.to_records()], dtype="str")

while True:
	print()
	print(f"""{"Tasks":=^38}""")
	for task_id, task in enumerate(tasks):
		print(f"[{task_id}]", task, sep=" ")
	
	print()
	print(f"""{"Actions":=^38}""")
	print(f"""[0] {"Exit": ^30}""")
	print(f"""[1] {"Create a task": ^30}""")
	print(f"""[2] {"Remove a task": ^30}""")
	print(f"""[3] {"Prioritize a task": ^30}""")
	print(f"""[4] {"Change priority of a task": ^30}""")
	print()
	
	action = input("Action: ")
	
	if action ==  "0":
		print("Bye!")
		break
	elif action ==  "1":
		task = pd.Series([input("Create New Task: ")])
		tasks = pd.concat([task, tasks])
		tasks.index = [x for x in range(len(tasks))]
		print("Added task!")
		tasks.to_csv(SAVE_FILE)
	elif action == "2":
		task_id = input("ID of task to remove: ")
		try:
			tasks = tasks.drop([int(task_id)])
			tasks.index = [x for x in range(len(tasks))]
			print(f"Removed task at {task_id}!")
			tasks.to_csv(SAVE_FILE)
		except:
			print("Invalid id!")
	elif action == "3":
		task_id = input("ID of task to prioritize: ")
		try:
			task = pd.Series([tasks[int(task_id)]])
			tasks = tasks.drop([int(task_id)])
			tasks = pd.concat([task, tasks])
			tasks.index = [x for x in range(len(tasks))]
			print(f"Prioritized task at {task_id}!")
			tasks.to_csv(SAVE_FILE)
		except:
			print("Invalid id!")
	elif action == "4":
		task_id = input("ID of task to change priority: ")
		task_priority = input("Priority: ")
		try:
			task = pd.Series([tasks[int(task_id)]], index=[int(task_priority)])
			tasks = tasks.drop([int(task_id)])
			tasks:pd.Series = pd.concat([task, tasks])
			tasks = tasks.sort_index()
			tasks.index = [x for x in range(len(tasks))]
			print(f"Set task at {task_id} to {task_priority}!")
			tasks.to_csv(SAVE_FILE)
		except:
			print("Invalid id!")
	else:
		print("Invalid action!")

