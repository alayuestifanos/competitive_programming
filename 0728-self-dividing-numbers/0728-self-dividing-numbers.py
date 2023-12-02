class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_numbers = []
        for number in range(left, right + 1):
            temp = number
            is_self_dividing_number = True
            while temp > 0:
                digit = temp % 10
                if digit == 0 or number % digit != 0:
                    is_self_dividing_number = False
                    break
                temp = temp // 10
            if is_self_dividing_number:
                self_dividing_numbers.append(number)
        return self_dividing_numbers