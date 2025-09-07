# Thursday Lab

class Patient:
    def __init__(self, number_in, name_in, medical_card_in, type_in):
        self.number = number_in
        self.name = name_in
        self.medical_card = medical_card_in
        self.type = type_in
        self.len_stay_in = 0
        self.amount_due = 0

#(a)
    def set_stay(self, len_stay_in):
        self.len_stay = len_stay_in
        return len_stay_in
#(b)
    def get_name(self):
        return self.name
#(c)
    def calc_bill(self):
        if self.medical_card:
            self.amount_due = 0
        elif self.type:
            self.amount_due = self.len_stay * 300
        elif not self.type:
            self.amount_due = self.len_stay * 100
#(f)
    def print(self):
        print("Patient num:", self.number)
        print("Patient name:", self.name)
        if self.medical_card:
            print("Medical Card Y/N: Y")
        else:
            print("Medical Card Y/N: N")
        if self.type:
            print("Private patient Y/N: Y ")
        else:
            print("Private patient Y/N: N")
        print(self.name + "'s bill amount €", self.amount_due)


p1 = Patient('78922', 'Jane Austin', True, True)
p1.set_stay(10)
p1.calc_bill()
p1.print()

p2 = Patient('67453', 'Henry James', False, True)
p2.set_stay(7)
p2.calc_bill()
p2.print()

#(g)
patient_num = input("Enter patient number:")
patient_name = input("Enter patient name:")
med_card = input("Medical Card Y/N:")
private_pat = input("Private Patient Y/N:")
len_stay = int(input("Enter length of stay:"))

if med_card.lower() == 'y':
    med_card = True

else:
    med_card = False

if private_pat.lower() == 'y':
    private_pat = True

else:
    private_pat = False
p3 = Patient(patient_name, patient_name, med_card, private_pat)
p3.set_stay(len_stay)
p3.calc_bill()
p3.print()