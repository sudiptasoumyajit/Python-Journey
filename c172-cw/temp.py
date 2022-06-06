class doctor():
    def __init__(self):
        print("DOCTOR")
    def BMI(weight,height):
        bmi=weight/(height*height)
        print("Your BMI Is:"+str(bmi))
    def heart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("Heart Rate: Normal")
        else:
            print("Heart Rate: Critical")
class Paitent(doctor):
    def __init__(self, name, weight, height, heart_rates):
        self.paitent_name=name
        self.paitent_weight=weight
        self.paitent_height=height
        self.paitent_heart_rates=heart_rates
    def healthCheck(self):
        print("\n Patient Name:",self.paitent_name)
        doctor.BMI(self.paitent_weight,self.paitent_height)
        doctor.heart_rate(self.paitent_heart_rates)
paitent1=Paitent("Jhon",30,0.99912,90)
paitent1.healthCheck()
paitent2=Paitent("Merry",100,0.9,20)
paitent2.healthCheck()