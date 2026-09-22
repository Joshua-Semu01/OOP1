class FamilyMember:
    def __init__(self,eye_color,home_village):
        self.eye_color=eye_color
        self.home_village=home_village
    def describe_familymember(self):
        print(f"eye_color:{self.eye_color},home_village:{self.home_village}")
class Mathew(FamilyMember):
    def __init__(self,eye_color,home_village,occupation):
        super().__init__(eye_color,home_village)
        self.occupation=occupation

    def describe_familymember(self):
        base_description = super().describe_familymember()
        return f"{base_description} He works as a :{self.occupation}."
       
Mathew=Mathew("brown","kibingo","farmer")
Mathew.describe_familymember()
print(Mathew.describe_familymember)

    