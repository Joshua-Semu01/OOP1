class PhoneAlarm:
    def __init__(self, snooze_count =0):
        self.snooze_count=snooze_count
        
    def wake_me_up(self):
        return "Scream at full  volume"
class roomate:
    def __init__(self,name):
        self.name=name
    def wake_me_up(self):
        return f"{self.name} pours water on you."
class Mothercall:
    def wake_me_up(self):
        return "calls at 4:30am"
class Sunlightthroughthewindow:
    def wake_me_up(self):
        return "Sunlight creeps in"
morning=[
    PhoneAlarm(5),
    roomate("ERIC"),
    Mothercall(),
    Sunlightthroughthewindow()
]
def start_your_day(wake_me_up):
    return wake_me_up.wake_me_up()

for tap_me in morning:
    print(start_your_day(tap_me))