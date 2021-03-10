# 16.Imagine you are creating a Super Mario game. You need to define aclass to represent Mario. What would it look like?
# If you aren't familiar with SuperMario, use your own favorite video or board game to model a player.

class Mario():
    def __init__(self, name, nickname, gender, occupation, nationality):
        self.name = name
        self.nickname = nickname
        self.gender = gender
        self.occupation = occupation
        self.nationality = nationality

    def mario_details(self):
        print(f'Name: {self.name}')
        print(f'Nickname: {self.nickname}')
        print(f'Gender: {self.gender}')
        print(f'Occupation: {self.occupation}')
        print(f'Nationality: {self.nationality}')


class Power(Mario):
    def __init__(self, name, nickname, gender, occupation, nationality):
        super().__init__(name, nickname, gender, occupation, nationality)
        self.speed = 50
        self.height = 3

    def mushroom(self):
        print('After eating mushroom...........')
        self.speed = self.speed + 20
        print(f'Speed has changed into {self.speed}m/s.')
        self.height = self.height + 2
        print(f'Height has been increased to {self.height} meter.')


profile = Mario('Mario Mario', 'Super Mario', 'Male', 'Plumber', 'Italian')
profile.mario_details()
profile = Power('Mario Mario', 'Super Mario', 'Male', 'Plumber', 'Italian')
profile.mushroom()
