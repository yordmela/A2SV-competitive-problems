class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans=[]
        fahrenheit= (celsius*9)/5+32
        kelvin= celsius+273.15
        ans.append(kelvin)
        ans.append(fahrenheit)
        return ans

        