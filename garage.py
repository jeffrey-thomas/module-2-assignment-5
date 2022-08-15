class ParkingGarage():
    
    def __init__(self, capacity):

        #create required lists of tickets and parking spaces
        self.tickets = [i for i in range(capacity)]
        self.parking_spaces = [i for i in range(capacity)]

        #required current ticket dictionary
        self.current_ticket = {"paid":False}

    # - takeTicket
    # - This should decrease the amount of tickets available by 1
    # - This should decrease the amount of parkingSpaces available by 1
    def take_ticket(self):
        #if tickets are available
        if(len(self.tickets)>0):
            self.tickets.pop()
            self.parking_spaces.pop()
        else:
            print("Sorry, the parking garage is full.")

    # - payForParking
    # - Display an input that waits for an amount from the user and store it in a variable
    # - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
    # - This should update the "currentTicket" dictionary key "paid" to True
    def pay_for_parking(self):
        payment = input("Please enter your payment amount:")
        if payment:
            print("Thank you! You have 15 minutes to leave the parking garage.")
            self.current_ticket["paid"] = True

    # -leaveGarage
    # - If the ticket has been paid, display a message of "Thank You, have a nice day"
    # - If the ticket has not been paid, display an input prompt for payment
    # - Once paid, display message "Thank you, have a nice day!"
    # - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
    # - Update tickets list to increase by 1 (meaning add to the tickets list)
    def leave_garage(self):
        if self.current_ticket["paid"]:
            print("Thank you, have a nice day.")
        else:
            payment = input("Please enter your payment amount:")
            #they must pay to leave
            while not payment:
                payment = input("Please enter your payment amount:")

            print("Thank you, have a nice day.")

        self.parking_spaces.append(len(self.parking_spaces))
        self.tickets.append(len(self.tickets))

def test_garage():
    garage = ParkingGarage(0)
    garage.take_ticket()    #should print not enough room
    
    garage = ParkingGarage(10)
    garage.take_ticket()
    print(len(garage.tickets)) #should print 9

    garage.pay_for_parking() #give empty response
    garage.leave_garage()   #should ask for payment

    print(len(garage.tickets)) # should print 10

    garage.take_ticket()

    garage.pay_for_parking() #give non-empty response
    garage.leave_garage()   #should not ask for payment

test_garage()    
