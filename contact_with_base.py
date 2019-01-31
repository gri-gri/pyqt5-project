class DatabaseClass:
    def __init__(self, filename=None):
        FILE_NAME = 'database.json'
        import json
        self.file_name = FILE_NAME if filename is None else filename
        with open(self.file_name, mode='r', encoding='utf-8') as file:
            self.data = json.loads(file.read())

    def add_task(self, dct):
        self.data.append(dct)

    def obnov(self):
        import json
        with open(self.file_name, mode='w', encoding='utf-8') as file:
            file.write(json.dumps(self.data))
            
        

