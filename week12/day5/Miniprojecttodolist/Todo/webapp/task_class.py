
from . import models, db

# Create a file called task_class.py.
# Create a class called Task.
# Create a function __init__(self,task). 
# The task parameter in the __init__ should have a default value of null. 
# This function assigns the task parameter to the attribute task_text.
# Create a function called get_tasks(self). 
# This function will fetch all of the todos saved inside your database and then return them.
# Create a function called save_task_to_db(self). 
# Its goal is to retrieve the data from the form, then to save the new todo to your database (ie. new record).




# In the task_class.py file, add another parameter called is_task_completed to the __init__(self,task) function. 
# The parameter should be False by default. This function assigns the is_task_completed parameter 
# to the attribute task_completed.

class Task()

    def __init__(self, task=null):
        self.task = task
        task_completed = False

    def get_tasks(self):
        tasks = models.Todo.query.all()
        return tasks

    def save_task_to_db(self):
        task = models.Todo()
        #retrieve data from the form and add to the database
        db.session.add(task)
        db.session.commit()


    