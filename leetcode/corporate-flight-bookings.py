class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        def findPrefixsum(arr):
            accu=0
            new=[0]*(len(arr))
            for i in range(len(arr)):
                accu+=arr[i]
                new[i]=accu
            return new
        booked= [0]*n
        for booking in bookings:
            booked[booking[0]-1]+=booking[-1]
            if  booking[1]-1<n-1:
                booked[booking[1]]-=booking[-1]

        ans= findPrefixsum(booked)
        return ans



        