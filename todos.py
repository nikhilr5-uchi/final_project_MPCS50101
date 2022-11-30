from Tasks import Tasks
from Task import Task
import argparse
import sys
import pickle
import datetime

"""
This is the main function and it basically checks that the first arguement is one of the required if it is
not then the function prints out error message


Calls each function based on first argument. i.e. checks what user is trying to do and then calls 
corresponding Tasks function
"""


def main():
    if len(sys.argv) < 2:
        print("Does not have right arguement")
        print("Must have one of follow arguements: \n --add\n --delete\n --list\n --report\n --query\n --done")
        return
    first_arg = sys.argv[1]
    tasks = Tasks()
    if (first_arg == '--add' or first_arg == '-add'):

        try:
            parser = argparse.ArgumentParser()
            parser.add_argument(first_arg,
                                type = str,
                                help ='Enter a todo item') 

            parser.add_argument("--due",
                                type = str, 
                                help ="Due Date", 
                                required = False)

            parser.add_argument("--priority",
                                type = int, 
                                help ="priority", 
                                required = False)
            args = parser.parse_args()

            add_priority = 1
            if (args.priority):
                add_priority = args.priority

            if (args.due != None):
                format = '%m/%d/%Y'
                datetime_str = datetime.datetime.strptime(args.due, format)
            else:
                datetime_str = None
            tasks.add(args.add, args.due, args.priority)
            tasks.pickle_tasks()

        except:
            print("There was an error in creating your task. Run \"todo -h\" for usage instructions.")
            return
        
    elif (first_arg == '--done' or first_arg =='-done'):
        parser = argparse.ArgumentParser()
        parser.add_argument('--done', type= int, required=True)

        args = parser.parse_args()

        tasks.done(args.done)
    elif (first_arg == '--list' or first_arg =='-list'):
        tasks.list()
    elif (first_arg == '--report' or first_arg =='-report'):

        tasks.report()
    elif (first_arg == '--query' or first_arg =='-query'):
        parser = argparse.ArgumentParser()
        parser.add_argument('--query', type=str, required=False, nargs="+", help="priority of task; default value is 1")

        args = parser.parse_args()

        tasks.query(list(args.query))
    elif (first_arg == '--delete' or first_arg =='-delete'):

        parser = argparse.ArgumentParser()
        parser.add_argument('--delete', type= int, required=True)

        args = parser.parse_args()

        tasks.delete(args.delete)
    else: 
        print("Does not have right arguement")
        print("Must have one of follow arguements: \n --add\n --delete\n --list\n --report\n --query\n --done")
        return

"""
Just used to debug and clean out old tasks when trying to restart 
"""
def clean_files():
    fp = open('./.todo.pickle','w')
    fp.write("")
    fp.close()

    fp = open('./version.txt', 'w')
    fp.write("0")
    fp.close()

if __name__ == "__main__":
    main()
    

    #clean_files()