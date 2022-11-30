from Task import Task
from datetime import date
import pickle


"""
Class implements all the function required add, list, delete, query, done, report

It updates the file .todo.pickle that holds a pickles list of all the tasks

Also changes version.txt that makes sure that each uid get a unique id
"""
class Tasks:
    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = [] 
        with open("./.todo.pickle", 'rb') as f:
            while True:
                try:
                    self.tasks = (pickle.load(f))
                except:
                    break
    def pickle_tasks(self):
        """Picle your task list to a file"""
        with open ("./.todo.pickle", 'wb') as f:
            pickle.dump(self.tasks, f)

    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        print("ID\t Age\t Due Date\t Priorirty\t Task\t")
        print("--\t ---\t --------\t --------\t ----\t")
        for task in self.tasks:
            if task.completed == None:
                age = (date.today() - task.created).days
                if (task.due_date == None):
                    add1 ="\t"
                else:
                    add1 = ""
                print(str(task.uid) + "\t "+ str(age) + "d\t " +  str(task.due_date)  + "\t\t" + add1 + str(task.priority) + "\t" +  str(task.name))

    def report(self):
        print("ID\t Age\t Due Date\t Priorirty\t Task\t Created\t\t\t Completed\t")
        print("--\t ---\t --------\t --------\t ----\t ----------------------\t\t -----------------------")
        for task in self.tasks:
            age = (date.today() - task.created).days
            format_created = task.created.strftime('%A %B %d %Y')
            if task.completed != None:
                format_completed = task.completed.strftime('%A %B %d %Y')
            else:
                format_completed = 'None'

            if (task.due_date == None):
                    add1 ="\t"
            else:
                    add1 = ""
            print(str(task.uid) + "\t "+ str(age) + "d\t " +  str(task.due_date)  + "\t\t " + add1+ str(task.priority) + "\t " +  str(task.name) + "\t " + format_created + "\t " + str(format_completed))


    def done(self, uid):
        for task in self.tasks:
            if task.uid == uid:
                task.completed = date.today()
                print("Complete task: " + str(uid))
                self.pickle_tasks()
                return
        print("Could not find task: " + str(uid))

    def delete(self, uid):
        for task in self.tasks:
            if task.uid == uid:
                self.tasks.remove(task)
                self.pickle_tasks()
                print("Deleted Task: " + str(uid))
                return
        print("No ID in list with number: " + str(uid))
        return

    def query(self, args):
        print("ID\t Age\t Due Date\t Priorirty\t Task\t")
        print("--\t ---\t --------\t --------\t ----\t")
        for task in self.tasks:
            curr_name = (task.name).lower()
            for word in args:
                if word.lower() in curr_name:
                    if task.completed == None:
                        age = (date.today() - task.created).days
                        print(str(task.uid) + "\t "+ str(age) + "d\t " +  str(task.due_date)  + "\t\t" + str(task.priority) + "\t" +  str(task.name))
                        break

    def add(self, name, due_date, priority):
        fp = open('./version.txt', 'r+')
        uid = int(fp.readline().strip())
        fp.close()
        fp = open('./version.txt', 'w')
        fp.write(str(uid+1))
        fp.close()
        if priority == None:
            priority = 1
        new_t = Task(date.today(), None, name, uid, priority, due_date)
        self.tasks.append(new_t)


