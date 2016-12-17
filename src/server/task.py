class Task():
    """creating a Taks with different parameters"""
    def __init__(self, taskId, title, associatedList="defaultList", status="normal", description="", due=None, revision=0):
        self.id = taskId
        self.title = title
        self.list = associatedList
        self.status = status
        self.description = description
        self.due = due
        self.revision = revision

    def revision_up(self):
        self.revision += 1

    def revision_down(self):
        self.revision -= 1


Task1 = Task(1, "Penny Lane")
Task2 = Task(2, "Yellow Submarine")
Task3 = Task(3, "Octopuses Garden")
Task4 = Task(4, "Lady Madonna")
