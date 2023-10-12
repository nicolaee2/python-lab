dividend = 15
divisor = 9

if divisor == 0:
    print("Can't divide by 0")
    exit(-1)

# check sign
if (dividend < 0) ^ (divisor < 0):
    sign = "-"
else:
    sign = ""

dividend, divisor = abs(dividend), abs(divisor)
quotient = dividend // divisor
remainder = dividend % divisor

result = [str(quotient), "."]

for i in range(100):
    remainder *= 10
    quotient, remainder = divmod(remainder, divisor)
    result.append(str(quotient))

print(sign + "".join(result))
