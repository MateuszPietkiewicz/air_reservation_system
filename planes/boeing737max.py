from .airplane import Airplane


class Boeing737Max(Airplane):
    @staticmethod
    def get_airplane_model():
        return "Beoing 737 Max"

    @staticmethod
    def get_seating_plan():
        return range(1, 46), 'ABCDEGHJK'