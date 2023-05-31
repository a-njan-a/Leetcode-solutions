class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.travel_time = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, checkin_time = self.check_in.pop(id)
        travel_time = t - checkin_time
        travel = (start_station, stationName)

        if travel in self.travel_time:
            total_time, count = self.travel_time[travel]
            self.travel_time[travel] = (total_time + travel_time, count+1)
        else:
            self.travel_time[travel] = (travel_time, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation, endStation)
        total_time, count = self.travel_time[travel]
        return total_time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)