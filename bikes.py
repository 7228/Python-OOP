import datetime

class BikeRental():
    def __init__(self,costumer,bike,amount,duration,time_rented):
        
        self.costumer = costumer
        self.bike = bike
        self.amount = amount
        self.duration = duration
        self.time_rented = time_rented
        
        self.all_bikes = {
            "TVS Jupiter":300,"TVS Jupiter-450":350,"Yamaha MT-15":400,"TVS Apache":200,
            "Yamaha R15S":450,"Hero Splendor Plus":250,"TVS Apache":500,"TVS Ronin":350,
            "Royal Enfield Classic 350":600,"Royal Enfield Bullet 350":550,"Yamaha YZF R15 V3":650,
            "Yamaha MT 15":500,"Hero Splendor Plus":400,"Bajaj Pulsar 150":100,"KTM 200 Duke":300,
            "Bajaj Pulsar NS200":150,"Suzuki SV650":700,"Suzuki GSX-R600":750,"Honda CBF125M":750,
            "Yamaha YZF-R1":800,"Yamaha YBR125":800,"Triumph Bonneville":850,"Triumph Tiger":900,
            "BMW R1200":1000,"Piaggio Vespa":100
        }

        self.bikes_copy = self.all_bikes.copy()

        if self.amount == 1:
            del self.all_bikes[self.bike[0]]
        else:
            for x in self.bike:
                del self.all_bikes[x]

    def catalogue(self):
        print("In our catalogue we currently have the following bikes: ")
        for x in self.all_bikes:
            print("\n", x)

    def issue_bill(self):
        if self.amount == 1 and self.duration == 'daily':
            bill = self.bikes_copy[self.bike[0]]
            self.all_bikes[self.bike[0]] = self.bikes_copy[self.bike[0]]
        
        elif self.amount == 1 and self.duration == 'weekly':
            bill = self.bikes_copy[self.bike[0]] * 2
            self.all_bikes[self.bike[0]] = self.bikes_copy[self.bike[0]]
        
        elif self.amount == 1 and self.duration == 'monthly':
            bill = self.bikes_copy[self.bike[0]] * 5
            self.all_bikes[self.bike[0]] = self.bikes_copy[self.bike[0]]
        
        elif self.amount > 1 and self.duration == 'daily':
            bill = 0
            for x in self.bike:
                bill += self.bikes_copy[x]
                self.all_bikes[x] = self.bikes_copy[x]
        
        elif self.amount > 1 and self.duration == 'weekly':
            bill = 0
            for x in self.bike:
                bill += (self.bikes_copy[x] * 2)
                self.all_bikes[x] = self.bikes_copy[x]
        
        elif self.amount > 1 and self.duration == 'weekly':
            bill = 0
            for x in self.bike:
                bill += (self.bikes_copy[x] * 5)
                self.all_bikes[x] = self.bikes_copy[x]

        print(f"You have rented {self.bike} for {self.duration} use, starting on {self.time_rented}. Your bill is {bill}$")

    
    def time(self):
        convo = datetime.datetime.strptime(self.time_rented,"%d-%M-%Y")
        return(convo)            

rental1 = BikeRental("Vladimir Cakic",['Yamaha R15S'],1,'daily','18-8-2022')
print(rental1.bike)        
rental1.issue_bill()

rental2 = BikeRental("Nenad Filipovic",['TVS Ronin','Suzuki GSX-R600'],2,'weekly','18-8-2022')
print(rental2.issue_bill())
print(rental2.time())

class TennisPlayer():
    def __init__(self,name,last,gs):
        self.name = name
        self.last = last
        self.gs = gs

    @classmethod
    def create_new(cls,str1):
        name,last,gs = str1.split("-")
        return(cls(name,last,gs))

djokovic = TennisPlayer("Novak","Djokovic",21)
print(djokovic.gs)

new_player = TennisPlayer.create_new("Janko-Tipsarevic-0")
print(new_player.name)








