
# Visādi 11-ciparu skaitļi, kas nesatur 5 savā decimālpierakstā, bet dalās ar 5.
N = 9
M = 5
rem = 10**(N-1) % M  # ja M=5, tad rem=0;  ja M=3, tad rem=1
if rem > 0:
    i = 10**(N-1) + (M - rem)
else:
    i = 10**(N-1)

total = 0
while i < 10**N:
    si = str(i)
    if "5" in si:
        pass
    else:
        total += 1
    i += 5

print('total = {}'.format(total))