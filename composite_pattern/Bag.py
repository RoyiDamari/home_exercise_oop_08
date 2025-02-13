from typing import override
from Equipment import Equipment


class CompositeBag(Equipment):
    def __init__(self, name):
        super().__init__(name)
        self.contents = []

    @override
    def add_child(self, equipment):
        self.contents.append(equipment)

    @override
    def remove_child(self, equipment):
        if equipment in self.contents:
            self.contents.remove(equipment)
            print(f"Removed '{equipment.name}' from '{self.name}'.")
        else:
            print(f"Warning: '{equipment.name}' is not in '{self.name}', cannot remove.")

    @override
    def get_contents(self, indent=0):
        spaces = "  " * indent
        result = f"{spaces}Bag: {self.name}\n"

        for obj in self.contents:
            if isinstance(obj, CompositeBag):
                child_content = obj.get_contents(indent + 1)
            else:
                child_content = obj.name

            result += f"{spaces}  {child_content}\n"

        return result.strip()

    @override
    def get_weight(self):
        return sum(equipment.get_weight() for equipment in self.contents)

    def __str__(self):
        return f"Bag({self.name}) containing: {', '.join(obj.name for obj in self.contents)}"
