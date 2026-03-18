class TrailerNotFoundError(Exception):
    def __init__(self, message="Trailer not found"):
        self.message = message
        super().__init__(self.message)


class TrailerAlreadyCheckedInError(Exception):
    def __init__(self, message="Trailer already checked in"):
        self.message = message
        super().__init__(self.message)


class NoAvailableSpotError(Exception):
    def __init__(self, message="No available yard spot"):
        self.message = message
        super().__init__(self.message)


class SpotOccupiedError(Exception):
    def __init__(self, message="Yard spot is already occupied"):
        self.message = message
        super().__init__(self.message)