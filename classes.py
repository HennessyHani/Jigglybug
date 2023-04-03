class StuNt:

      def __init__(self, name, age, classroom):
          self.name = name
          self.age = age
          self.classroom = classroom

          
      def testscore(self, val1, val2, val3):
          testscore = (val1 + val2 + val3)/3
          return testscore

student1 = StuNt('hela', int(14), 'indigo')
print(student1.age)

student2 = StuNt('loki', int(1000), 'amber')
print(student2.age)

val1 = int(input())
val2 = int(input())
val3 = int(input())

print(student1.testscore(val1, val2, val3))



