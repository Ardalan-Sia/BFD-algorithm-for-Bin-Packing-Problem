class Item:
    def __init__(self, id : int, size) -> None:
        self.id = id
        self.size = size
        pass
    
    def get_size(self):
        return self.size
    
    def get_id(self):
        return self.id