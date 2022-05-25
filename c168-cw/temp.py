class Citizen:
    def __init__(self,name,age,dob,id_number,gender):
        self.citizen_name=name
        self.citizen_age=age
        self.citizen_dob=dob
        self.citizen_id=id_number
        self.citizen_gender=gender
    def add_citizen(self):
        print("__________________________________________________________________")
        print('Name: '+self.citizen_name)
        print('Age: '+self.citizen_age)
        print('Date Of Birth: '+self.citizen_dob)
        print('Family ID: '+self.citizen_id)
        print('Gender: '+self.citizen_gender)
        print("Citizen Exists")
        print("__________________________________________________________________")
citizen1=Citizen("Soumyajit Das","13 Year","03 / 03 / 2009","01","Male, Teenager")
citizen1.add_citizen()
citizen2=Citizen("Mili Sarkar Das","38 Year","NaN","02","FeMale, Mother")
citizen2.add_citizen()
citizen3=Citizen("Sudipta Das","40 Year","NaN","03","Male, Father")
citizen3.add_citizen()