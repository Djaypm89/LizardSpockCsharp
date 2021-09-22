import sys,time,random
class Type_Speed:    
    def slow_type(self,speed):
        typing_speed = int(speed) #wpm
        for l in self:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random()*10.0/typing_speed)
        return print ('')