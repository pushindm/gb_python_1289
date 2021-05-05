import time
from itertools import cycle

class TrafficLight:
    
    __color = None
    
    def running(self):
        tic = time.perf_counter()
        for el in cycle(zip(['red', 'yellow', 'green'], [7, 2, 5])):
            TrafficLight.__color = el[0]
            print(f"Color: {TrafficLight.__color}")
            time.sleep(el[1])
            toc = time.perf_counter()
            if toc - tic > 20:
                break
        print('done')
 
# main       
traffic_light = TrafficLight()
traffic_light.running()
