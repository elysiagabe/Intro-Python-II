class Item: 
    def __init__(self, name, description):
        self.name = name
        self.desc = description

    def __str__(self):
        return f"{self.name}: {self.desc}"
