class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  
  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy
    
  def get_pickupPolicy(self, pickupPolicy):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + f" The pickup policy is: {self.pickupPolicy}."


mySchool = PrimarySchool("The Best School", 500, "Only parents")
mySchool.set_numberOfStudents(600)
print(mySchool)