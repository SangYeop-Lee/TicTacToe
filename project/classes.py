import datetime

class DaysLeft:

    def __init__(self, name, date):

        self.name = name
        self.daysLeft = datetime.datetime.now().date() - date
        self.daysLeft = self.daysLeft.days