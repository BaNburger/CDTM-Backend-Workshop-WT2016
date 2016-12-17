class List():
    """creating a List in which tasks live"""
    def __init__(self, listId, title, revision=0):
        self.id = listId
        self.title = title
        self.revision = revision

    def revision_up(self):
        return self.revision += 1

    def revision_down(self):
        return self.revision -= 1

defaultList = List(0, "defaultList")

List1 = List(1, "Revolver")
List2 = List(2, "Abbey Roads")
