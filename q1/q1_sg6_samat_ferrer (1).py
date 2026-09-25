'''
#5 FERRER, Reginald Andrei D.
9-samat                                  FA6
'''

class Lab:
    def __init__(self, room_number):
        self.room_number = room_number
        
class Technician:
    def __init__(self, name, assigned_lab = None):
        self.name = name
        self.assigned_lab = assigned_lab
    def assign_lab(self, lab_object):
        self.assigned_lab = lab_object

room_numb = input("Please enter the lab room number: ")
chem_lab = Lab(room_numb)
Mr_Cruz = Technician("Mr. Cruz")

Mr_Cruz.assign_lab(chem_lab)

print("Technician:", Mr_Cruz.name)
print("Assigned Room:", Mr_Cruz.assigned_lab.room_number )