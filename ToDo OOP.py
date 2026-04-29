from pathlib import Path
# rewriting using OOP
class TodoList:
    def __init__(self, filepath='ToDo.txt'):
        self.filepath = filepath
        Path(self.filepath).touch(exist_ok=True)
    
    # Function for loading the file as a list.
    def _load(self):
        with open(self.filepath, 'r') as file:
            return file.readlines()

    def getList(self):    
        list = self._load()
        if not list:
            print("\nNothing here yet.")
        for i, item in enumerate(list, start=1):
            print(f'\t{i}. {item.strip()}')

    # Function for saving the list to the file. This does overwrite the list.
    def _save(self, taskList):
        with open(self.filepath, 'w') as file:
            file.writelines(taskList)
    
    # Function for appending a single item to the file.
    def _append(self, task):
        with open(self.filepath, 'a') as file:
            file.write(task.capitalize() + '\n')
    
    # Function for marking an item completed.
    def markComplete(self, index, task):
        taskList = self._load()
        self.index = index
        
        found = False
        for item in taskList:  
            if task.strip() == item.lower().strip(): #accounting for differences in capitalization
                task = task.capitalize() + ' X\n' #modifying the given task to now be given an X
                idx = taskList.index(item) # getting the index of the given item and setting it variable idx
                taskList[idx] = task # at the previously retrieved index, updating the task to be the new string with the X
                self._save(taskList)

                found = True #item is found so break the loop
                break
        if not found:
            print('You haven\'t added that task yet.')
    
    # Function for deleting an unneeded task from the list.
    def deleteTask(self, task):
        taskList = self._load()
        
        found = False
        for item in taskList:
            if task.strip().lower() == item.lower().strip():
                taskList.remove(item)
                self._save(taskList)

                found = True
                break
        if not found:
            print('You haven\'t added that task yet.')        

    def run(self):
        selection = input('\nWould you like to do... \n' \
        '1. View List \n' \
        '2. Add Task \n' \
        '3. Mark Complete \n' \
        '4. Delete Task \n > ')
        
        if selection == '1': # View the current list
            self.getList()
            self.run()
        elif selection == '2': # Add a task
            task = input('What task do you want to accomplish?\n > ').capitalize()
            self._append(task)
            self.run()
        elif selection == '3': # Mark a task as complete
            list = self._load()
            self.getList()
            task = input('What did you acommplish? \n > ').lower()
            self.markComplete(task)
            self.run()
        elif selection == '4': # Delete a task that is no longer needed
            task = input('What item are you deleting?\n > ')
            self.deleteTask(task)
            self.run()
        else:
            print('Invalid selection.')
            self.run()
            
zk = TodoList()
zk.run()

