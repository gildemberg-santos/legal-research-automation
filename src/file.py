import os


class File:
    def __init__(self, path):
        self.path = path
        self.files = []

    def get_files(self, extension: str = 'pdf') -> list:
        if extension:
            ways = [os.path.join(self.path, name)
                    for name in os.listdir(self.path)]
            files = [file for file in ways if os.path.isfile(file)]
            self.files = [
                arq for arq in files if arq.lower().endswith(extension)]
        return self.files

    # def __enter__(self):
    #     self.file = open(self.path, 'w')
    #     return self.file

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.file.close()


