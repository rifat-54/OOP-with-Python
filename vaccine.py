class Vaccine:
    def __init__(self,name,country,interval):
        self.name=name
        self.country=country
        self.interval=interval


class Person:

    def __init__(self,*parameter):
        if(len(parameter)==3):
            self.name=parameter[0]
            self.age=parameter[1]
            self.role=parameter[2]
        elif(len(parameter)==2):
            self.name=parameter[0]
            self.age=parameter[1]
            self.role="General Citizen"
        else:
            self.name=parameter[0]
            self.role="General Citizen"

        

    def pushVaccine(self,*parameter):
        VaccineName=parameter[0].name
        if(self.age<25 and self.role!="Student"):
            print("Sorry ",self.name," Your age less than 25 you cant take vacine")
            return

        if(len(parameter)==1):
            self.firstDose="Given"
            self.secondDose=parameter[0].interval
            self.vaccineName=VaccineName
            print("1st dose done for ",self.name)

        else:
            if(self.vaccineName!=VaccineName):
                print("Sorry ",self.name," you cannot take two different vaccine")
                return
            self.secondDose="Given"
            print("2nd dose done for ",self.name)
          

    def showDetail(self):
        print("Name: ",self.name,"Age: ",self.age,"Type: ",self.role,
              "\nVaccine Name: ",self.vaccineName,
              "\n1st dose: ",self.firstDose)
        if(self.secondDose!="Given"):
              print("2nd dose: Please come after",self.secondDose," Days")
        else:
            print("2nd dose: Given")

    
# ==============================================================================================================

astra = Vaccine("AstraZeneca", "I-JK", 60)
modr = Vaccine("Moderna", "I-JK", 30)
sin = Vaccine("Sinopharm", "China", 30)


pl =Person ("Bob",21 , "Student")
p2 = Person("Carol", 23, "Actor")
p3=Person("David",34)

print("================================================================================")

pl.pushVaccine(astra)

print("================================================================================")

pl.showDetail()

print("================================================================================")

pl.pushVaccine(sin,"2nd Dose")

print("================================================================================")

pl.pushVaccine(astra,"2nd Dose")

print("================================================================================")

pl.showDetail()

print("================================================================================")

p2.pushVaccine(sin)
print("================================================================================")

 
p3.pushVaccine(modr)
print("================================================================================")
p3.showDetail()
print("================================================================================")

p3.pushVaccine(modr,"2nd Dose")
print("================================================================================")
p3.showDetail()



        