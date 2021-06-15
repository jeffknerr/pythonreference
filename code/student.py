
class Student(object):
  """student objects"""

  def __init__(self, name, year, username):
    """constructor, given student name, year, username"""

    self.name = name
    self.year = year
    self.username = username
    self.quizzes = []            # initially, no quiz
    self.labs = []               # or lab grades

  def __str__(self):
    """this one *must* return a string"""
    s = "%s (%s) -- %d" % (self.name, self.username, self.year)
    s += "\n%s\n%s" % (self.quizzes, self.labs)
    return s

  def addQuizGrade(self, qgrade):
    """add a given grade to the quizzes list"""
    self.quizzes.append(qgrade)

  def addLabGrade(self, lgrade):
    """add a given grade to the labs list"""
    self.labs.append(lgrade)

  def currentGrade(self):
    """
    calculate and return current grade.
    quizzes are 60%, labs 40% of total grade
    """
    quizavg = 0.0
    if len(self.quizzes) > 0:
      quizavg = sum(self.quizzes)/len(self.quizzes)
    labavg = 0.0
    if len(self.labs) > 0:
      labavg = sum(self.labs)/len(self.labs)
    grade = quizavg*.60 + labavg*.40
    return grade

#####################################################

def main():
  s1 = Student("Lee Majors", 2020, "lmajors1")
  print(s1)
  s2 = Student("Lindsay Wagner", 2022, "lwagner2")
  print(s2)
  s1.addQuizGrade(78)
  s1.addQuizGrade(75)
  s1.addQuizGrade(83)
  s1.addLabGrade(91)
  s1.addLabGrade(90)
  print(s1)
  print(s1.currentGrade())
  print(s2.currentGrade())

if __name__ == "__main__":
  main()

