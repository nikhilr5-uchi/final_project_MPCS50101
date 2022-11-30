"""
Creates a task

Simple class
"""


class Task:
    def __init__(self, created, completed, name, uid, priority, due_date= None):
        self.created = created
        self.completed = completed
        self.name = name
        self.uid = uid
        self.priority = priority
        self.due_date = due_date

    def __str__(self):
        return_string = "Name: " + str(self.name)
        return_string +=  "\nCreated: "+ self.created.strftime('%m/%d/%Y')
        if (self.completed == None):
            ret_completed = "False"
        else:
            ret_completed = self.completed
        return_string += "\nCompleted: " + str(ret_completed)
        return_string += "\nUID: " + str(self.uid)
        return_string += "\nPriority: " + str(self.priority)
        
        if (self.due_date == None):
            ret_due_date = 'None'
        else:
            ret_due_date = str(self.due_date)
        return_string+= "\nDue Date: " + ret_due_date


        return return_string