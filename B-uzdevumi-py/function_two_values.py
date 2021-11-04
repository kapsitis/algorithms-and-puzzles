
# Komplekso skaitļu reizināšana:
# i^2 = -1
# (a + bi)*(c + di) = (ac - bd) + (bc + ad)i
# Gribam atgriezt divus naturālus skaitļus: (ac - bd) un (bc + ad)
def complex_multiplication(a, b, c, d):
    e = a*c - b*d
    f = b*c + a*d
    return (e,f)


def main():
    # 2 + i, 2 - i
    (p, q) = complex_multiplication(2, 1, 2, -1)
    print("(2 + i)* (2 - i) = {} + {}i".format(p, q))

# 5 + 0i  var sadalīt pirmreizinātājos (2-1i), (2 + 1i)

if __name__ == '__main__':
    main()
