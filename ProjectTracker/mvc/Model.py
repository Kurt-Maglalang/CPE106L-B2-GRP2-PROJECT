# Replace with your actual project data model
# WARNING: THIS IS MERELY A PLACEHOLDER. 
class Project:
    def __init__(self, id, name, progress, deadline, attributes=None, objectives=None, notes=None):
        self.id = id
        self.name = name
        self.progress = progress
        self.deadline = deadline
        self.attributes = attributes or {}
        self.objectives = objectives or []
        self.notes = notes or ""
