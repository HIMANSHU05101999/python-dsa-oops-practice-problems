# OOP Revision Exercise 19
#
# Hospital Records
#
# Difficulty: ★★★☆☆
#
# ----------------------------------------------------
# Patient
# ----------------------------------------------------
#
# A Patient object stores:
#
# - patient_id
# - name
# - disease
# - room_number
#
# Implement:
#
# - properties for all attributes
# - room_number should be updateable
# - __str__()
#
#
# Example:
#
# ID: 101
# Name: Alice
# Disease: Flu
# Room: 203
#
#
# ----------------------------------------------------
# Hospital
# ----------------------------------------------------
#
# Store Patient objects in a dictionary:
#
#     patient_id -> Patient object
#
#
# ----------------------------------------------------
# Methods
# ----------------------------------------------------
#
# add_patient(patient)
#
# Add a Patient object to the hospital.
#
# If the patient_id already exists,
# replace the old Patient object with the new one.
#
#
# update_room(patient_id, new_room)
#
# Update the room number of the specified patient.
#
# If the patient does not exist,
# do nothing.
#
#
# get_patient(patient_id)
#
# Return the Patient object.
#
# If the patient is not found,
# return None.
#
#
# list_patients()
#
# Print every patient stored in the hospital.
#
# Use each Patient object's __str__() method.
#
#
# statistics()
#
# Print:
#
# total patients
#
# patients per disease
#
# Example:
#
# Total patients: 7
#
# Flu: xxx
# Covid: xx
# Cancer: x
# Diabetes: x
#
#
# ----------------------------------------------------
# Interface
# ----------------------------------------------------
#
# Commands:
#
# 1 add patient
# 2 update room
# 3 search patient
# 4 list patients
# 5 statistics
# 0 exit
#
#
# ----------------------------------------------------
# Example Session
# ----------------------------------------------------
#
# 1
# Patient ID: 101
# Name: Alice
# Disease: Flu
# Room: 203
#
# 1
# Patient ID: 102
# Name: Bob
# Disease: Covid
# Room: 305
#
# 2
# Patient ID: 101
# New Room: 210
#
# 3
# Patient ID: 101
#
# Output:
#
# ID: 101
# Name: Alice
# Disease: Flu
# Room: 210
#
# 5
#
# Output:
#
# Total patients: 2
#
# Flu: x
# Covid: x

class Patient:
    def __init__(self, p_id, name, disease, room):
        self.__p_id=p_id
        self.__name=name
        self.__disease=disease
        self.__room=room

    @property
    def name(self):
        return self.__name

    @property
    def p_id(self):
        return self.__p_id

    @property
    def disease(self):
        return self.__disease

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self,val):
        self.__room=val
     
    def __str__(self):
        return f"ID: {self.__p_id} Name: {self.__name} Disease: {self.__disease} Room: {self.__room}"

class Hospital:
    def __init__(self):
        self.__patients={}

    def add_patient(self, p_id, name, disease, room):
        patient=Patient(p_id, name, disease, room)
        self.__patients[p_id]=patient

    def update_room(self, p_id, room):
        if p_id in self.__patients:
            self.__patients[p_id].room=room

    def search(self,p_id):
        if p_id in self.__patients:
            return self.__patients[p_id]

    def list_patients(self):
        return {p_id:patient for p_id,patient in self.__patients.items()}

    def stats(self):
        stat={}
        for _,patient in self.__patients.items():
            if patient.disease not in stat:
                stat[patient.disease]="x"
            else:
                stat[patient.disease]+="x"
        return stat
    
class Application:
    def __init__(self):
        self.__interact=Hospital()

    def view(self):
        print("1 add patient\n2 update room\n3 search patient\n4 list patients\n5 statistics\n0 exit")

    def choice(self):
        self.view()
        while True:
            ch=input("Enter Choice: ")
            if ch=="1":
                p_id=input("Enter Patient ID: ")
                name=input("Enter Patient Name: ")
                disease=input("Enter Patient Disease: ")
                room=input("Enter Room Alloted: ")            
                self.__interact.add_patient(p_id,name,disease,room)
            if ch=="2":
                p_id=input("Enter Patient ID: ")
                room=input("Enter Room Alloted: ")
                self.__interact.update_room(p_id,room)
            if ch=="3":
                p_id=input("Enter Patient ID: ")
                print(self.__interact.search(p_id))
            if ch=="4":
                for _,patient in self.__interact.list_patients().items():
                    print(patient)
            if ch=="5":
                for disease, num_of_patients in self.__interact.stats().items():
                    print(f"{disease}: {num_of_patients}")
            if ch=="0":
                return

exe=Application()
exe.choice()
        