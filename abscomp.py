class Speaker:
    def play_music(self):
        print("Boom am playing Music")
class DancingRobot:
    def __init__(self):
        self.speaker=Speaker()
    def dance(self):
        self.speaker.play_music()
        print("Kutama")
        print("Saka")
        
        
       