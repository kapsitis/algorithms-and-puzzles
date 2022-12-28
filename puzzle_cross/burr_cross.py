import sys
import time
import itertools
import copy

from backtrack import *

class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    # Reizina vektoru ar skaitli (skaitlim jābūt rakstītam pa kreisi no vektora)
    def __rmul__(self, other):
        return Point3D(other*self.x, other*self.y, other*self.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def abs(self):
        return int(max(abs(self.x), abs(self.y), abs(self.z)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __ne__(self, other):
        return not self.__eq__(other)


DIRECTIONS = {'X+': Point3D(2,0,0), 'X-': Point3D(-2,0,0),
              'Y+': Point3D(0,2,0), 'Y-': Point3D(0,-2,0),
              'Z+': Point3D(0,0,2), 'Z-': Point3D(0,0,-2)}

# An "empty" block, if some position in the Burr cross has to be left empty.
CROSS00 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

FULL_CROSS = [
    [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
     [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]],
    [[3, 3, 3, 3, 1, 0, 0, 1, 3, 3, 3, 3],
     [3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3]],
    [[3, 3, 3, 3, 1, 0, 0, 3, 3, 3, 3, 3],
     [3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3]],
    [[3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3],
     [3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3]],
    [[3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3],
     [3, 3, 3, 3, 1, 0, 0, 1, 3, 3, 3, 3]],
    [[3, 3, 3, 3, 3, 0, 0, 1, 3, 3, 3, 3],
     [3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3]]
]

HARD_CROSS_A = [
    [[3, 3, 3, 3, 1, 2, 0, 1, 3, 3, 3, 3],
     [3, 3, 3, 3, 1, 3, 1, 1, 3, 3, 3, 3]],
    [[3, 3, 3, 3, 1, 0, 1, 1, 3, 3, 3, 3],
     [3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3]],
    [[3, 3, 3, 3, 1, 1, 0, 1, 3, 3, 3, 3],
     [3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3]],
    [[3, 3, 3, 3, 1, 1, 0, 1, 3, 3, 3, 3],
     [3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 3, 3]],
    [[3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3],
     [3, 3, 3, 3, 1, 3, 1, 1, 3, 3, 3, 3]],
    [[3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3],
     [3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 3, 3]]
]



# One piece for the Burr cross of size 12x2x2.
class Block:
    arrays = []
    spacePoints = []
    offset = Point3D(0,0,0)
    num = 0

    # Mark the points involved.
    # Place the origin at the center of the Block.
    def __init__(self, arrays, letter, flip, num):
        # print('Creating Block({}, {}, {})'.format(arrays, letter, flip))
        self.spacePoints = []
        self.arrays = arrays
        self.offset = Point3D(0, 0, 0)
        self.num = num

        for i in range(0, 2):
            for j in range(0, 12):
                if arrays[i][j] // 2 == 1:
                    self.spacePoints.append(Point3D(2*j-11, 2*i - 1, 1))
                if arrays[i][j] % 2 == 1:
                    self.spacePoints.append(Point3D(2*j-11, 2*i - 1, -1))
        # Need to start with a 180 degree turn around vertical Z axis
        if flip == 1:
            self.rotateZ(1)
            self.rotateZ(1)
        if letter == 'A':
            self.rotateX(1)
            self.translate(Point3D(0, -2, 0))
        elif letter == 'B':
            self.rotateX(-1)
            self.translate(Point3D(0, 2, 0))
        elif letter == 'C':
            self.rotateZ(-1)
            self.translate(Point3D(0, 0, -2))
        elif letter == 'D':
            self.rotateZ(-1)
            self.rotateY(1)
            self.rotateY(1)
            self.translate(Point3D(0, 0, 2))
        elif letter == 'E':
            self.rotateY(1)
            self.rotateZ(1)
            self.rotateZ(1)
            self.translate(Point3D(-2, 0, 0))
        elif letter == 'F':
            self.rotateY(1)
            self.translate(Point3D(2, 0, 0))


    # Rotate counter-clockwise (dir = +1) or clockwise (dir = -1) around X axis
    def rotateX(self, dir):
        self.spacePoints = [Point3D(p.x, dir*p.z, -dir*p.y) for p in self.spacePoints]

    # Rotate counter-clockwise (dir = +1) or clockwise (dir = -1) around Y axis
    def rotateY(self, dir):
        self.spacePoints = [Point3D(-dir*p.z, p.y, dir*p.x) for p in self.spacePoints]

    # Rotate counter-clockwise (dir = +1) or clockwise (dir = -1) around Z axis
    def rotateZ(self, dir):
        self.spacePoints = [Point3D(dir*p.y, -dir*p.x, p.z) for p in self.spacePoints]

    def translate(self, vect):
        self.offset = self.offset + vect
        self.spacePoints = [(p + vect) for p in self.spacePoints]

    def contains(self, pt):
        return pt in self.spacePoints


# https://johnrausch.com/PuzzlingWorld/chap05.htm
class BurrCrossProblem:
    perm = ('A', 'B', 'C', 'D', 'E', 'F')
    flips = (0, 0, 0, 0, 0, 0)
    move_list = []
    # (Letter -> Block) mapping
    blocks = dict()
    prev_offsets = set()

    def __init__(self, perm, flips, crosses):
        self.perm = perm
        self.flips = flips
        self.move_list = []
        self.blocks = dict()
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        for i in range(len(letters)):
            self.blocks[letters[i]] = Block(crosses[i], self.perm[i], self.flips[i], i+1)
        self.prev_offsets = set()
        self.prev_offsets.add(self.get_six_offsets())


    def get_six_offsets(self):
        current_offsets = [self.blocks[letter].offset for letter in ['A', 'B', 'C', 'D', 'E', 'F']]
        result = copy.deepcopy(current_offsets)
        return tuple(result)


    def can_fit(self):
        all_points = set()
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        for letter in letters:
            for pt in self.blocks[letter].spacePoints:
                if pt in all_points:
                    return False
                else:
                    all_points.add(pt)
        return True


    def full_debug(self):
        # print('display')
        minX, maxX, minY, maxY, minZ, maxZ = -11, 11, -11, 11, -11, 11
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        for letter in letters:
            for pt in self.blocks[letter].spacePoints:
                minX, maxX = min(minX, pt.x), max(maxX, pt.x)
                minY, maxY = min(minY, pt.y), max(maxY, pt.y)
                minZ, maxZ = min(minZ, pt.z), max(maxZ, pt.z)
        print('minX = {}, maxX = {}, minY = {}, maxY = {}, minZ = {}, maxZ = {}'.format(minX, maxX, minY, maxY, minZ, maxZ))


        for z in range(maxZ, minZ-2, -2):
            print('   *** Level({}) ***'.format(z))
            for y in range(minY, maxY+2, 2):
                for x in range(minX, maxX+2, 2):
                    found = False
                    for letter in letters:
                        if self.blocks[letter].contains(Point3D(x, y, z)):
                            print('{} '.format(self.blocks[letter].num), end='')
                            found = True
                            break
                    if not found:
                        print('.', end=' ')
                print()
        # TODO: Print warnings, iff blocks overlap in some Point3D

    def check1(self, level, move):
        shifted_offsets_list = list(self.get_six_offsets())
        shifted_offsets_list[ord(move[0]) - ord('A')] = shifted_offsets_list[ord(move[0]) - ord('A')] + DIRECTIONS[move[1]]
        shifted_offsets = tuple(shifted_offsets_list)
        return not (shifted_offsets in self.prev_offsets)

    def check2(self, level, move):
        shifted_spacePoints = [(pt + DIRECTIONS[move[1]]) for pt in self.blocks[move[0]].spacePoints]
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        letters.remove(move[0])
        for letter in letters:
            if any(pt in shifted_spacePoints for pt in self.blocks[letter].spacePoints):
                return False
        return True

    # Vai gājiens norādītajā virzienā ir derīgs?
    # "move" ir formātā "('A', 'X+')"
    def valid(self, level, move):
        c1 = self.check1(level, move)
        c2 = self.check2(level, move)
        # print('level = {}, move = {}, c1 = {}, c2 = {}'.format(level, move, c1,c2))
        return c1 and c2

    # Vai polimonda līnija pabeigta?
    def done(self, level):
        # return len(self.prev_offsets) >= 6
        max_offset = 0
        for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
            if self.blocks[letter].offset.abs() > max_offset:
                max_offset = self.blocks[letter].offset.abs()
        return max_offset >= 6



    # Pievienojam esošo gājienu
    def record(self, level, move):
        # print("RECORD {}, {}".format(self.move_list, move))
        self.move_list.append(move)
        self.blocks[move[0]].translate(DIRECTIONS[move[1]])
        new_offsets_lists = list(self.get_six_offsets())
        self.prev_offsets.add(tuple(new_offsets_lists))


    def undo(self, level, move):
        # print("UNDO {}, {}".format(self.move_list, move))
        last_move = self.move_list.pop()
        self.blocks[last_move[0]].translate((-1)*DIRECTIONS[last_move[1]])

    def moves(self, level):
        return MoveEnumeration(0)

class MoveEnumeration:
    cursor = 0
    end = 0
    next_moves = []

    # Konstruktors: iterators sāksies ar vērtību "initial" un beidzas ar max-1.
    def __init__(self, initial):
        self.next_moves = list(itertools.product(['A', 'B', 'C', 'D', 'E', 'F'], ['X+', 'X-', 'Y+', 'Y-', 'Z+', 'Z-']))
        self.cursor = initial - 1
        self.end = len(self.next_moves)

    # Sagatavo iteratoru "for" cikla pašā sākumā un atgriež to
    def __iter__(self):
        return self

    # atgriež tekošo vērtību intervālā [initial; max-1]. Ja beidzas, tad izlec no cikla ar "StopIteration"
    def __next__(self):
        self.cursor += 1
        if self.cursor < self.end:
            return self.next_moves[self.cursor]
        raise StopIteration



def main():
    global FULL_CROSS
    global HARD_CROSS_A
    # all_permutations = list(itertools.permutations(['A', 'B', 'C', 'D', 'E', 'F']))
    # all_flips = list(itertools.product([0, 1], repeat=6))

    all_permutations = [('A', 'C', 'B', 'D', 'F', 'E')]
    all_flips = [(1, 0, 1, 1, 0, 1)]

    total_combinations = 0
    valid_combinations = 0
    found = False
    for perm in all_permutations:
        for flips in all_flips:
            total_combinations += 1
            bcp = BurrCrossProblem(perm, flips, HARD_CROSS_A)

            if total_combinations % 1000 == 0:
                print("({} combinations verified)".format(total_combinations))
            if bcp.can_fit():
                #print('Solving {}, {} ... '.format(perm, flips), end='')
                valid_combinations += 1

                b = Backtrack(bcp)
                if b.attempt(0):
                    print('Solving {}, {} ... '.format(perm, flips), end='')
                    pretty_moves = ['({}{},{})'.format(L, bcp.blocks[L].num,D) for (L, D) in bcp.move_list]
                    print('Moves: {}'.format(pretty_moves))
                    print('  In Solution offsets are: {}'.format(bcp.get_six_offsets()))
                    bcp.full_debug()
                    found = True
                    break
                else:
                    pass
                    #print('Could not solve!')
                    #break
        if found:
            break


    # print('total_combinations = {}'.format(total_combinations))



    # bcp = BurrCrossProblem(['D', 'C', 'E', 'A', 'B', 'F'], [0, 0, 0, 0, 1, 1],
    #                         [CROSS01, CROSS02, CROSS03, CROSS04, CROSS05, CROSS06])
    # bcp.full_debug()


    # for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
    #     print('Block {} has {} points'.format(letter, len(bcp.blocks[letter].spacePoints)))
    # print("Can fit = {}".format(bcp.can_fit()))
    #


if __name__ == '__main__':
    main()

