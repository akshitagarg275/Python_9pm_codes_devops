'''
Write a class Train which has methods to book a ticket, get status(no of seats), 
and get fare information of trains running under Indian Railways.

[1,2,3,4,5]
'''

class Train:

    def __init__(self,tname,tseats,tfare):
        self.tname=tname
        self.tseats=tseats
        self.seat=list(range(1,tseats+1))
        self.tfare=tfare
    
    def status(self):
        print("******STATUS******")
        print(f"Name of train: {self.tname}")
        print(f"Total no of seats available: {self.tseats}")
        print(f"seats available for booking: {self.seat}")
        print(f"Fare of one seat: {self.tfare}")
        print('**********************')
    
    def bookTicket(self, noOfTickets):
        if noOfTickets > len(self.seat):
            print(f"{noOfTickets} Seats are not available")
            print(f"Seats left : {len(self.seat)}")
        else:
            allocated_seats= []
            fare = 0
            for i in range(noOfTickets):
                allocated_seats.append(self.seat.pop(0))
                fare += self.tfare
            print(f"Seats booked: {allocated_seats} and total fare is: {fare}")
    
    def cancelTicket(self,ticketNo):
        if ticketNo in self.seat or ticketNo > self.tseats or ticketNo < 1:
            print("Check ticket No!")
        else:
            self.seat.append(ticketNo)
            print("Cancellation completed")

obj = Train("Rajdhani Express", 5, 50)
# obj.status()

obj.bookTicket(3)

# obj.status()

obj.cancelTicket(3)
obj.status()

