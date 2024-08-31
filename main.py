import random
from person import *

def main():
    print("hey!")
    test_person = Person("bob")
    print(test_person.name)
    # Example usage

    # Generate initial people with randomized attributes
    person1 = Person("Alice", attributes=randomize_attributes())
    person2 = Person("Bob", attributes=randomize_attributes())

    # Display initial attributes
    print(f"Person 1 Attributes: {person1.attributes}")
    print(f"Person 2 Attributes: {person2.attributes}")

    # Create a child with inherited attributes
    child = person1.inherit_attributes(person1, person2)

    print(f"Child Attributes: {child.attributes}")
    child.name = "Alicia"
    print("Name of child: " + child.name)

main()