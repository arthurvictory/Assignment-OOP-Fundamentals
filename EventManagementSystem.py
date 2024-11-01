class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.number_of_participants = 0

    
    def add_participant(self, name):
        self.name = name
        self.number_of_participants += 1
        print(f"{self.name} passed the check and has made the list!")

    def participant_count(self):
        print(f"The total number of people who passed the check: {self.number_of_participants}")
        return self.number_of_participants
    
event = Event("Super secret club", "March 20, 1998")
event.add_participant("Andrew Victory")
event.add_participant("Arthur Victory")
event.add_participant("Rita Victory")
event.add_participant("Larry Victory")
event.participant_count()   