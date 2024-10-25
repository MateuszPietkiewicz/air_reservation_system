class Airplane:
    def get_seat_no(self):
        rows, seats = self.get_seating_plan()
        return len(rows) * len(seats)