class Task():
    """creating a Taks with different parameters"""
    def __init__(self, taskId, title, associatedList=0, status="normal", description="", due=None, revision=0):
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
