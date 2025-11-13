import random
import time

class TrainForm:
    def __init__(self):
        self.destination = input("Enter destination : ")
        self.journey_From = input("Enter journey from : ")
        self.journey_To = input("Enter journey to : ")
        day = input("Enter journey date (Day) : ")
        month = input("Enter journey date (Month) : ")
        year = input("Enter journey date (Year) : ")
        self.journey_date = {
            "day": day,
            "month": month,
            "year": year,
        }
        self.first_name = input("Enter first name : ")
        self.last_name = input("Enter last name : ")
        self.age = input("Enter age : ")

        self.ticket_no = random.randint(100000, 999999)
        self.booking_time = time.strftime("%H:%M:%S %d-%m-%Y", time.localtime())
        self.seat_no = random.randint(1, 80)

    def printDetails(self):
        print("Destination :", self.destination)
        print("Journey From :", self.journey_From)
        print("Journey To :", self.journey_To)
        print("Journey Date :", f"{self.journey_date['day']}-{self.journey_date['month']}-{self.journey_date['year']}")
        print("Passenger Details :", {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        })
        print(f"Ticket Number : {self.ticket_no}")
        

    def printTrainName(self):
        train_names = ["Express Line", "Rapid Transit", "Coastal Cruiser", "Mountain Explorer", "City Connector"]
        self.selected_train = random.choice(train_names)
        print("Assigned Train Name :", self.selected_train)

    def saveTicket(self):
        with open("ticket.txt", "w") as f:
            f.write("----- Train Ticket -----\n")
            f.write(f"Booking Time: {self.booking_time}\n")
            f.write(f"Train Name : {self.selected_train}\n")
            f.write(f"Ticket Number: {self.ticket_no}\n")
            f.write(f"Seat Number: {self.seat_no}\n")
            f.write(f"Passenger Name: {self.first_name} {self.last_name}\n")
            f.write(f"Age: {self.age}\n")
            f.write(f"Destination: {self.destination}\n")
            f.write(f"Journey From: {self.journey_From}\n")
            f.write(f"Journey To: {self.journey_To}\n")
            f.write(f"Journey Date: {self.journey_date['day']}-{self.journey_date['month']}-{self.journey_date['year']}\n")
            print("Ticket saved successfully to ticket.txt")

    def showSummary(self):
        self.printDetails()
        self.printTrainName()
        self.saveTicket()


TrainForm_obj = TrainForm()
TrainForm_obj.showSummary()