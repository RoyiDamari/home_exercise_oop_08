from Bag import  CompositeBag
from Item import LeafItem

def main():
    # Create individual items
    water_bottle = LeafItem("Water Bottle", 1.0)
    cheese = LeafItem("Cheese", 0.5)
    bread = LeafItem("Bread", 0.7)
    corn = LeafItem("Corn", 0.8)
    bamba = LeafItem("Bamba", 0.3)
    beesley = LeafItem("Beesley", 0.4)
    marshmallow = LeafItem("Marshmallow", 0.2)

    # Create bags
    snack_bag = CompositeBag("Snack Bag")
    snack_bag.add_child(bamba)
    snack_bag.add_child(beesley)
    snack_bag.add_child(marshmallow)
    snack_bag.add_child(water_bottle)

    healthy_food_bag = CompositeBag("Healthy Food Bag")
    healthy_food_bag.add_child(bread)
    healthy_food_bag.add_child(cheese)
    healthy_food_bag.add_child(snack_bag)

    main_bag = CompositeBag("Main Bag")
    main_bag.add_child(healthy_food_bag)
    main_bag.add_child(corn)

    # Trying to add a child to a Leaf (Should Raise Error)
    try:
        cheese.add_child(LeafItem("Extra Cheese", 0.2))
    except NotImplementedError as e:
        print(f"Exception Caught: {e}")

    # Trying to remove an item from a Leaf (Should Raise Error)
    try:
        cheese.remove_child(bamba)
    except NotImplementedError as e:
        print(f"Exception Caught: {e}")

    print("-" * 50)
    # Compute total weight
    print(f"Total equipment weight: {main_bag.get_weight()} kg")

    print("-" * 50)
    # Print Nested Structure
    print(main_bag.get_contents())


if __name__ == "__main__":
     main()