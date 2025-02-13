from typing import override
from Equipment import Equipment


class LeafItem(Equipment):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    @override
    def add_child(self, equipment):
        raise NotImplementedError(f"Error: Cannot add '{equipment.name}' to a LeafItem '{self.name}'!")

    @override
    def remove_child(self, equipment):
        raise NotImplementedError(f"Error: Cannot remove an item from a LeafItem '{self.name}'!")

    @override
    def get_contents(self):
        return None

    @override
    def get_weight(self):
        return self.weight