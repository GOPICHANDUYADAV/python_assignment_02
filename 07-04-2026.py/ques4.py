#digital clock
class DigitalClock:
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def display(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def tick(self):
        self.seconds += 1

        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1

        if self.hours == 24:
            self.hours = 0


# Test
clock = DigitalClock(23, 59, 58)

clock.display()

for i in range(5):
    clock.tick()
    clock.display()