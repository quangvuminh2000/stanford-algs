"""
Problem: Integer Multiplication
Input: Two n-digit nonnegative integers, x and y
Output: The product x.y
"""


def multiplication(data_file: str):
    with open(data_file, "r") as f:
        x = int(f.readline())
        y = int(f.readline())

    return karatsuba_multiplication(x, y)


def hs_multiply(x: int, y: int) -> int:
    # Change to string number
    strx = str(x)
    stry = str(y)

    res = 0
    for n in range(len(strx)):
        for m in range(len(stry)):
            prod = eval(f"{strx[n]}*{stry[n]}")
            power = 10 ** ((len(strx) - n - 1) + (len(stry) - m - 1))
            res += prod * power

    return res


def karatsuba_multiplication(x: int, y: int) -> int:
    # Base case: x,y < 10
    if x < 10 and y < 10:
        return x * y

    sx = str(x)
    sy = str(y)
    m = max(len(sx), len(sy))
    # Fill paddings pre
    sx = "0" * (m - len(sx)) + sx
    sy = "0" * (m - len(sy)) + sy
    # Get middle point ceil and floor
    m1 = (m + 1) // 2
    m2 = m // 2

    # Divide the number into halves (left-right)
    lx = int(str(sx[:m1]))
    rx = int(str(sx[m1:]))
    ly = int(str(sy[:m1]))
    ry = int(str(sy[m1:]))

    # Recursively compute
    lx_ly = karatsuba_multiplication(lx, ly)
    rx_ry = karatsuba_multiplication(rx, ry)
    lr_xy = karatsuba_multiplication(lx + rx, ly + ry)

    # Compute the *terms*
    lxry_lyrx = lr_xy - lx_ly - rx_ry

    return (lx_ly * 10 ** (2 * m2)) + (lxry_lyrx * 10**m2) + rx_ry
