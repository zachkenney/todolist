from pathlib import Path
Path("ToDo.txt").touch(exist_ok=True)

def writeList(taskList):
    result = "".join(taskList)
    with open("ToDo.txt", "w") as file:
        file.write(result)

def writeFile(task):
    with open("ToDo.txt", "a") as file:
        file.write(task + "\n")

def markComplete(complete):
    taskList = []
    with open("ToDo.txt", "r") as file:
        taskList = file.readlines()

    found = False
    for item in taskList:
        if complete + '\n' == item.lower():
            idx = taskList.index(item)
            task = complete.capitalize() + " DONE!\n"
            taskList[idx] = task
            writeList(taskList)

            found = True
            break
    if not found:
        print("You haven't added that task yet.")

def deleteTask(deleteItem):
    taskList = []
    with open("ToDo.txt", "r") as file:
        taskList = file.readlines()

    found = False
    for item in taskList:
        if deleteItem + '\n' == item:
            taskList.remove(item)
            writeList(taskList)

            found = True
            break
    if not found:
        print("You haven't added that task yet.")

def viewList():
    with open("ToDo.txt", "r") as file:
        print(file.read())

def run():
    selection = input("Would you like to do... \n1. View List \n2. Add Task \n3. Mark Complete \n4. Delete Task \n > ")
    if selection == "1":
        viewList()
        run()
    elif selection == "2":
        task = input("What task do you want to accomplish?\n > ").capitalize()
        writeFile(task)
        run()
    elif selection == "3":
        complete = input("What did you acommplish? \n > ").lower()
        markComplete(complete)
        run()
    elif selection == "4":
        deleteItem = input("What item are you deleting?\n > ")
        deleteTask(deleteItem)
        run()
    else:
        print("Invalid selection.")
        run()

run()
