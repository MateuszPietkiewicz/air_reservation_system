from .airplane import Airplane


class AirbusA380(Airplane):
    @staticmethod
    def get_airplane_model():
        return "Airbus A380"

    @staticmethod
    def get_seating_plan():
        return range(1, 26), 'ABCDEG'