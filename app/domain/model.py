import json


class Client:
    CIF = 1
    Name = "Default"
    LastName = "Default"
    Link = "Default"
    age = 18
    isAdult = True

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

