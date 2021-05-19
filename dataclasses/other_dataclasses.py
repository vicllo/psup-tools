
class Selectivity:
    def __init__(self, places_available, previous_last_entry):
        self.places_available = places_available
        self.previous_last_entry = previous_last_entry

    def __str__(self):
        return "Available places : "+str(self.places_available)+",Last entry last year : "+str(self.previous_last_entry)
