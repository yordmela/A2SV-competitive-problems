class Solution:
    def average(self, salary: List[int]) -> float:
        sum=0
        maximum= max(salary)
        minimum= min(salary)
        for i in range(len(salary)):
            if salary[i]!=maximum and  salary[i]!= minimum:
                sum+=salary[i]
        return sum/(len(salary)-2)

        