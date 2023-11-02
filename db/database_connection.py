import sqlite3

class DatabaseConnection:
    
    def __init__(self, file):
        self.connection = None
        self.file = file

    def __enter__(self):
        self.connection = sqlite3.connect(self.file)
        return self.connection    
    
    def __exit__(self, exe_type, exe_val, exe_tb):
        if exe_type or exe_val or exe_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()