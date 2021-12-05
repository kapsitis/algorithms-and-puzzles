import os

tests = ['uzd01test01.txt',
         'uzd02test02.txt',
         'uzd03test03.txt',
         'uzd04test04.txt',
         'uzd05test05.txt',
         'uzd06test06.txt',
         'uzd07test07.txt',
         'uzd08test08.txt',
         'uzd01test09.txt',
         'uzd01test10.txt']

for test in tests:
    #with open('uzd01out.txt', 'a') as myfile:
    #    myfile.write('# Testa fails: {}'.format(test))
    os.system('python uzdevums1.py < {} >> uzd01out.txt'.format(test))

