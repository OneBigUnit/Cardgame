import os


class OpenMyPath:

    def __init__(self, path):
        self.path = path
        self.rev_path = f"{(path.count('/') + 1) * '../'}"[:-1]

    def __enter__(self):
        os.chdir(self.path)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.chdir(self.rev_path)
