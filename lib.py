from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")

with onto:
    class Student(Thing):
       label = ["Студент"]

    class LabWork(Thing):
        label = ["Лаба"]
               
    class Subject(Thing):
        label = ["Предмет"]

    class do(Student >> LabWork):
        python_name = "labs"
        label = ["Зроблено лаби"]    

    class lab_is_done(LabWork >> Student):
        python_name = "lab_is_done"    
        inverse_property = do
        label = ["Студенти, що зробили лабу"]

    class subject_have_Lab(Subject >> LabWork):
        python_name = "subject_have_Lab"    
        label = ["Предмет має лаби"]

    class lab_from_subject(LabWork >> Subject):
        python_name = "Lab_subject_have"  
        inverse_property  = subject_have_Lab
        label = ["Лаби з предмету"]

    

    subject1 = Subject(name="IT")
    subject2 = Subject(name="IS")

    AllDifferent([subject1, subject2])

    lab1 = LabWork(name="База знань")
    lab2 = LabWork(name="ЛР1")
    lab3 = LabWork(name="5. REST")

    lab1.subject_have_Lab.append(subject1)
    lab2.subject_have_Lab.append(subject1)
    lab3.subject_have_Lab.append(subject2)


    AllDifferent([lab1, lab2, lab3])

    student1 = Student(labs = [lab1], name="Біба")
    student2 = Student(labs = [lab1, lab2, lab3], name="Боба")
    student3 = Student(labs = [], name="Буба")
    student4 = Student(labs = [lab1, lab3], name="Беба")

    close_world(Student)

onto.save("onto.owl")







