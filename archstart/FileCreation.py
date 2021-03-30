class FileCreation:
    def __init__(self, fileName):
      self.fileName = fileName
    
    def createFile(self):
        f = open(self.fileName, "w")
