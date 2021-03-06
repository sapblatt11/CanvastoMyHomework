from datetime import datetime, timedelta


class Assignment:

    def __init__(self, name="No Name", course="", dueAt="1/1/2019", description="No Description"):
        self.name = name
        self.course = course
        #date = datetime.strptime(dueAt, "%Y-%m-%dT%H:%M:%S%z") - timedelta(days=1)
        self.dueAt = datetime.strftime(dueAt, "%m/%d/%Y")
        if description == None:
            self.description = "No Description"
        else:
            self.description = description
