class SeatManager:

    def __init__(self, n: int):
        self.totalSeats = n
        self.unreserved = [i for i in range(1,n+1)]
        self.reserved = []

    def reserve(self) -> int:
        lowestUnreserved = heapq.heappop(self.unreserved)
        heapq.heappush(self.reserved, lowestUnreserved)
        return lowestUnreserved
 
    def unreserve(self, seatNumber: int) -> None:
        for i in range(0, len(self.reserved)):
            if (self.reserved[i] == seatNumber):
                self.reserved.pop(i);
                heapq.heappush(self.unreserved, seatNumber)
                break;
            
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)