class FileObject():
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    def __del__(self):
        self.file.close()
        del self.file
