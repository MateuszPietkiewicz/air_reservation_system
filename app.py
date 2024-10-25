from pprint import pprint as pp
from flight.flight import Flight
from planes import AirbusA380, Boeing737Max
from helpers import card_printer


def main():
    airbus = AirbusA380()
    boeing = Boeing737Max()
    f = Flight('LO127', airbus)
    print(boeing.get_seating_plan())
    # print(f.get_airline())
    # print(f.get_number())
    # print(f.get_model())
    print(airbus.get_seat_no())
    # print(boeing.get_seat_no())
    f.allocate_passanger(passanger="Lech K", seat = "12C")
    f.allocate_passanger(passanger="Jarosław K", seat = "12B")
    f.allocate_passanger(passanger="Paweł K", seat = "12A")
    # f.relocate_passanger("12A", "25G")
    pp(f.seating_plan)
    print(f.get_empty_seat())

    for passenger in f.get_passenger_list():
        print(passenger)

    f.print_tickets(card_printer)

if __name__ == '__main__':
    main()
