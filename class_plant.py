# Model a class for a plant

class Plant:
    """docstring for Plant."""
    def __init__(self, name, kingdom, family, subfamily, genus):
        self.name = name
        self.kingdom = kingdom
        self.family = family
        self.subfamily = subfamily
        self.genus = genus
    
    def describe_plant(self):
        """ Prints a summary of the plant """
        print(f"{self.name} belongs to the {self.kingdom} kingdom.")
        print(f"Further details: Family {self.family}, subfamily {self.subfamily}, genus {self.genus}")
    

aplant = Plant('facelia', 'plantae', 'boraginaceae', 'Hydrophylloideae','Phacelia')

aplant.describe_plant()
