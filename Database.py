import os
import json

class DataBase:
    def __init__(self):
        self.data_file = os.path.join(os.path.dirname(__file__), "Data.json")

    def File_Register(self, Name, Email, Password):
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w") as f:
                json.dump({}, f)

        with open(self.data_file, "r") as F1:
            data = json.load(F1)

        if Email in data:
            return False
        else:
            data[Email] = [Name, Password]
            with open(self.data_file, "w") as F1:
                json.dump(data, F1)
            return True

    def Check_Credentials(self, email, password):
        with open(self.data_file, "r") as F1:
            data = json.load(F1)

        if email in data and data[email][1] == password:
            name = data[email][0]
            return {"name": name, "email": email}
        else:
            return None
