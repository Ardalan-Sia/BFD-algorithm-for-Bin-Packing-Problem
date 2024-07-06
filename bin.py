from item import Item
class Bin:
    def __init__(self, capacity: float) -> None:
        self.initial_capacity = capacity
        self.current_capacity = capacity
        self.items = []

    def space_left(self):
        return self.initial_capacity - self.current_capacity

    def get_current_space(self):
        return self.current_capacity

    def change_capacity(self, amount: float):
        self.current_capacity -= amount

    def add_item(self, item: Item):
        if item.get_id() not in [i.get_id() for i in self.items] and self.current_capacity >= item.get_size():
            self.items.append(item)
            self.change_capacity(item.get_size())
        
    def remove_item(self, item: Item):
        if item.get_id() in [i.get_id() for i in self.items]:
            self.items = [i for i in self.items if i.get_id() != item.get_id()]
            self.change_capacity(-item.get_size())
