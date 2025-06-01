import json

class DataBase:
    def File_Register(self, Name, Email, Password):
        with open(r"Data.json", "r") as F1:
            data= json.load(F1)
        if Email in data:
            return False
        else:
            data[Email]=[Name, Password]
            with open(r"Data.json", "w") as F1:
                json.dump(data, F1)
            return True

    def Check_Credentials(self, email, password):
        with open(r"Data.json", "r") as F1:
            data = json.load(F1)
        if email in data and data[email][1] == password:
            name = data[email][0]
            return {"name": name, "email": email}
        else:
            return None

