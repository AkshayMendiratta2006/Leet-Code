class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        negative = (dividend < 0) != (divisor < 0)
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        quotient = 0
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            abs_dividend -= temp_divisor
            quotient += multiple
        if negative:
            quotient = -quotient
        return quotient