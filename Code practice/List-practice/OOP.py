class person:
    def __init__(self,name ,age, father_name, mother_name):
        self.name = name
        self.age = age
        self.father_name = father_name
        self.mother_name = mother_name
    
    def change_name(self,name):
        self.name = name



my_data = person("opi", 23,"sh", "hs") 
