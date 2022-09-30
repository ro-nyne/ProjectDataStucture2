# Collect name, adress, phone number, e-mail
class Collector(object): # defind collecter class to collect data
    
    def __init__(self, name, adrs, tel, email):
        self.name = name
        self.adrs = adrs
        self.tel = tel
        self.email = email
        
    def __str__(self):
        str = 'Name: "% s" Adress: % s Tel. <% s> E-mail: % s'% (self.name, self.adrs, self.tel, self.email)
        return str
    
class Node:
    
    def __init__(self):
        pass