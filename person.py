import random


def randomize_attributes():
    """Generate a dictionary of random attributes."""
    attributes = {
        'Curiosity': random.randint(1, 100),
        'Temperance': random.randint(1, 100),
        'Passion': random.randint(1, 100),
        'Independence': random.randint(1, 100),
        'Luck': random.randint(1, 100),
        'Dexterity': random.randint(1, 100),
        'Creativity': random.randint(1, 100),
        'Resilience': random.randint(1, 100),
        'Empathy': random.randint(1, 100),
        'Intuition': random.randint(1, 100),
        'Focus': random.randint(1, 100),
        'Charisma': random.randint(1, 100),
        'Patience': random.randint(1, 100),
        'Adaptability': random.randint(1, 100),
        'Alertness': random.randint(1, 100),
        'Long-Term Memory': random.randint(1, 100),
        'Short-Term Memory': random.randint(1, 100)
    }

    #composite attributes
    attributes['Intellect'] = (attributes['Long-Term Memory'] + attributes['Curiosity'] + attributes['Focus']) // 3

    return attributes

class Person:
    def __init__(self, name, attributes=None, natural_mother=None, natural_father=None):
        self.name = name
        self.attributes = attributes if attributes is not None else {}

        self.skills = {
            'Navigation': 0,
            'Observation': 0,
            'Resource Identification': 0,
            'Basic Tool Use': 0,
            'Basic Communication': 0,
            'Stamina Management': 0,
            'Basic Shelter Seeking': 0
        }

        self.health = {
            'head': 100,
            'torso': 100,
            'left_arm': 100,
            'right_arm': 100,
            'left_leg': 100,
            'right_leg': 100,
            'heart': 100,
            'lungs': 100,
            'stomach': 100,
            'brain': 100
        }

        self.physical_energy = 100
        self.mental_energy = 100


    def calculate_initial_skills(self):
        skills = {}

        # Define the attribute weights for each skill
        skill_weights = {
            'Navigation': {'Intuition': 0.25, 'Focus': 0.2, 'Adaptability': 0.3, 'Luck': 0.2},
            'Observation': {'Curiosity': 0.1, 'Luck': 0.1, 'Intuition': 0.25, 'Focus': 0.25, 'Alertness': 0.3},
            'Resource Identification': {'Curiosity': 0.3, 'Intuition': 0.4, 'Observation': 0.3},
            'Basic Tool Use': {'Dexterity': 0.5, 'Creativity': 0.3, 'Focus': 0.2},
            'Basic Communication': {'Charisma': 0.5, 'Empathy': 0.3, 'Focus': 0.2},
            'Stamina Management': {'Resilience': 0.4, 'Patience': 0.3, 'Adaptability': 0.3},
            'Basic Shelter Seeking': {'Observation': 0.4, 'Adaptability': 0.4, 'Intuition': 0.2}
        }


    def inherit_attributes(self, parent1, parent2):
        """Creates a new person with attributes partially inherited from two parents."""
        new_attributes = {}
        for attribute in parent1.attributes.keys():
            parent1_value = parent1.attributes[attribute]
            parent2_value = parent2.attributes[attribute]

            # Average attributes from parents and add random variation
            inherited_value = (parent1_value + parent2_value) // 2
            variation = random.randint(-10, 10)  # Small random variation
            new_attributes[attribute] = max(1, min(100,
                                                   inherited_value + variation))  # Ensure values are between 1 and 100

        return Person("", attributes=new_attributes, natural_mother=parent1, natural_father=parent2)


