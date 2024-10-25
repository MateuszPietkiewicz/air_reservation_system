class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number

        rows, seats = self.airplane.get_seating_plan()
        self.seating_plan = [None] + [{letter: None for letter in seats} for _ in rows]

    def get_airline(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_model(self):
        return self.airplane.get_airplane_model()

    def _parse_seat(self, seat):
        rows, seats = self.airplane.get_seating_plan()
        letter = seat[-1]

        if letter not in seats:
            raise ValueError(f"Invalid seat letter: {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid row number: {row_text}")

        if row not in rows:
           raise ValueError(f"Row number is out of range: {row}")

        return row, letter



    def allocate_passanger(self, passanger, seat):
        row, letter = self._parse_seat(seat)

        if self.seating_plan[row][letter] is not None:
            raise ValueError(f"Seat is already taken: {seat}")

        self.seating_plan[row][letter] = passanger

    def relocate_passanger(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seat(seat_from)

        if self.seating_plan[row_from][letter_from] is None:
            raise ValueError(f"Seat from is not occupied: {seat_from}.")

        row_to, letter_to = self._parse_seat(seat_to)

        if self.seating_plan[row_to][letter_to] is not None:
            raise ValueError(f"Seat is occupied: {seat_to}.")

        self.seating_plan[row_to][letter_to] = self.seating_plan[row_from][letter_from]
        self.seating_plan[row_from][letter_from] = None

    def get_empty_seat(self):
        # return sum((seat for seat in row.values()
        #             if seat is None)
        #            for row in self.seating_plan if row is not None)

        num = 0
        for row in self.seating_plan:
            if row is not None:
                for passenger in row.values():
                    if passenger is None:
                        num += 1
        return num

    def get_passenger_list(self):
        rows, seats = self.airplane.get_seating_plan()

        for row in rows:
            for letter in seats:
                passenger = self.seating_plan[row][letter]
                if passenger is not None:
                    yield passenger, f'{row}{letter}'

    def print_tickets(self, printer):
        for passenger, seat in self.get_passenger_list():
            printer(passenger, seat, self.get_model(), self.flight_number)