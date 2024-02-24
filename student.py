class Student:

  def __init__(self,name,grade):

    self.name=name

    self.grade=grade


  def __str__(self):

    return "name: "+self.name+" grade: "+str(self.grade)



  def __repr__(self):

        return f"Student(name='{self.name}', grade='{self.grade}')"



  def name_new(self,name1):

    self.name1=name1

    print(self.name1)


s=Student("Alice" ,10)

print(s)


s1=Student("Bob",12)

print(s1)


s2=Student("Charlie",9)
print(s2)
