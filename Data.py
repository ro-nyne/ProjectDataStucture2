# Collect name, adress, phone number, e-mail
class Data(object): # defind collecter class to collect data
    
    def __init__(self, name, adrs, tel, email) -> None:
        self.name = name
        self.adrs = adrs
        self.tel = tel
        self.email = email
        
    def __str__(self) -> str:
        str = 'Name: "% s" Adress: % s Tel. <% s> E-mail: % s'% (self.name, self.adrs, self.tel, self.email)
        return str
    
    def __repr__(self) -> str:
        val = self.name.title() + ', ' + self.adrs + ', ' + self.tel + ', ' + self.email
        return val