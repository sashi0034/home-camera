

class Config:
    def __init__(self) -> None:
        self.can_picture: bool = True
        self.shot_interval: int = 5
        return

    def set_can_picture(self, flag: bool):
        self.can_picture = flag
        
    def set_shot_interval(self, num: int):
        self.shot_interval = num


