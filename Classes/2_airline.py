"""
Airline System - Create a reservation system which books airline seats. It charges various
rates for particular sections of the plane. Example, first class is going to cost more than
coach. Keep track of what seats are available and can be bought.

https://github.com/karan/Projects
"""

from dataclasses import dataclass
from enum import Enum

class SeatType(Enum):
    First = 6
    Business = 20
    Coach = 60

@dataclass
class Seat:
    type: SeatType
    name: str

class Plane:

    def __init__(self, callsign: str, first: int, business: int, coach: int) -> None:
        self.callsign = callsign
        self.first = first
        self.business = business
        self.coach = coach

        self.first_bought = []
        self.business_bought = []
        self.coach_bought = []
    
    def purchase_seat(self, seat: Seat) -> str | None:
        if seat.type == SeatType.First:
            if self.first == 0:
                return "No more first class seats available"
            self.first_bought.append(Seat(SeatType.First, seat.name))
            self.first -= 1
        if seat.type == SeatType.Business:
            if self.business == 0:
                return "No more business class seats available"
            self.business_bought.append(Seat(SeatType.Business, seat.name))
            self.business -= 1
        if seat.type == SeatType.Coach:
            if self.coach == 0:
                return "No more coach class seats available"
            self.coach_bought.append(Seat(SeatType.Coach, seat.name))
            self.coach -= 1

class Airline:

    FIRST = SeatType.First.value
    BUSINESS = SeatType.Business.value
    COACH = SeatType.Coach.value

    def __init__(self) -> None:
        self.planes = [
            Plane('DL774', self.FIRST, self.BUSINESS, self.COACH),
            Plane('DL192', self.FIRST, self.BUSINESS, self.COACH),
            Plane('DL588', self.FIRST, self.BUSINESS, self.COACH)
        ]
        self.plane_callsigns = [plane.callsign for plane in self.planes]

    def sell_ticket(self, plane: Plane) -> None:
        name = input("Enter your name: ")
        seat_dict = {
            "FIRST": SeatType.First,
            "BUSINESS": SeatType.Business,
            "COACH": SeatType.Coach
        }
        while seat_type := input("Enter type of seat to purchase (First/Business/Coach): ").upper():
            if seat_type not in seat_dict.keys():
                print("Not a valid seat type.")
                continue
            seat_type = seat_dict[seat_type]
            response = plane.purchase_seat(Seat(seat_type, name))
            if response != None:
                print(response)
                continue
            print("Successfully purchased seat!")
            return

    def get_desired_plane(self) -> None:
        while desired_plane := input("Enter the callsign of your desired flight: "):
            if desired_plane not in self.plane_callsigns:
                print("That plane does not currently have a flight.")
                continue
            for plane in self.planes:
                if plane.callsign == desired_plane:
                    self.sell_ticket(plane)
                    return

a = Airline()
a.get_desired_plane()