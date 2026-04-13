class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        st = []

        for p, s in reversed(cars):
            time = (target - p) / s

            if not st or time > st[-1]:
                st.append(time)
            
        return len(st)