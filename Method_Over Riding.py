class Bank:
    def __init__(self,cname,Branch,IFSC,location):
        self.cname=cname
        self.Branch=Branch
        self.IFSC=IFSC
        self.location=location

    def Customer_Deatils(self):
        print(f'Customer Name is {self.cname} and Bank Branch Name is {self.Branch} and Bank IFSC code is {self.IFSC} and Bank Location is {self.location}')


class ICIC_BANK(Bank):
    def __init__(self,pan_card_number,aadhar_number):
        super().__init__(cname="Naman",Branch="Delhi",IFSC=100,location="Metro")
        self.pan_card_number=pan_card_number
        self.aadhar_number= aadhar_number


    def Customer_verification(self):
        print(f' customer pan card number is {self.pan_card_number} and aadhar number is {self.aadhar_number}')

i=ICIC_BANK("CSJ56PK67",12345676)
i.Customer_Deatils()
i.Customer_verification()

#===================================================================================
'''
class Bank:
    def __init__(self,cname,Branch,IFSC,location):
        self.cname=cname
        self.Branch=Branch
        self.IFSC=IFSC
        self.location=location

    def Customer_Deatils(self):
        print(f'customer name is {self.cname} and bank branch name is {self.Branch} and bank IFsC code is {self.IFSC} and bank location is {self.location}')


class ICIC_BANK(Bank):
    def __init__(self,cname,Branch,IFSC,location,pancardnumber,aadharnumber):
        super().__init__(cname,Branch,IFSC,location)
        self.PanCardNumber=pancardnumber
        self.aadharnumber=aadharnumber


    def Customer_verification(self):
        print(f' customer pan card number is {self.pancardnumber} and aadhar number is {self.aadharnumber}')

i=ICIC_BANK("Naman","ICICBranch","1234 ICICI","Metro","CSJ5678PK","1234-4567-9876")
i.Customer_Deatils()
i.Customer_verification()
'''