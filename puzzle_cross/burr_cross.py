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
              'Z+': Point3D(0,0,2), 'Z-': Point3D(0,0,-2),
              '2Y+': Point3D(0,4,0), '3X-': Point3D(-6,0,0)}

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
        cubes_found = 0
        conflict = False
        conflict_pt = Point3D(0,0,0)
        conflict_block1 = 'N'
        conflict_block2 = 'N'

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
                    found_letter = 'N'
                    for letter in letters:
                        if self.blocks[letter].contains(Point3D(x, y, z)):
                            print('{} '.format(self.blocks[letter].num), end='')
                            found = True
                            found_letter = letter
                            cubes_found += 1
                            break
                    if found:
                        letters2 = copy.deepcopy(letters)
                        letters2.remove(found_letter)
                        for letter in letters2:
                            if self.blocks[letter].contains(Point3D(x, y, z)):
                                conflict = True
                                conflict_pt = Point3D(x,y,z)
                                conflict_block1 = found_letter
                                conflict_block2 = letter

                    if not found:
                        print('.', end=' ')
                print()
                if conflict:
                    print("********* WARNING: Blocks {}, {} intersect in point {}".format(conflict_block1, conflict_block2, conflict_pt))
                    conflict = False
                    conflict_pt = Point3D(0,0,0)
                    conflict_block1 = 'N'
                    conflict_block2 = 'N'
        print('Cubes found = {}'.format(cubes_found))





    def check1(self, level, move):
        shifted_offsets_list = list(self.get_six_offsets())
        for ltr in move[0]:
            shifted_offsets_list[ord(ltr) - ord('A')] = shifted_offsets_list[ord(ltr) - ord('A')] + DIRECTIONS[move[1]]
        shifted_offsets = tuple(shifted_offsets_list)
        return not (shifted_offsets in self.prev_offsets)

    def check2(self, level, move):
        shifted_points = set()
        remaining_letters = ['A', 'B', 'C', 'D', 'E', 'F']
        for ltr in move[0]:
            shifted_points.update([(pt + DIRECTIONS[move[1]]) for pt in self.blocks[ltr].spacePoints])
            remaining_letters.remove(ltr)
        for ltr in remaining_letters:
            if any(pt in shifted_points for pt in self.blocks[ltr].spacePoints):
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
        return max_offset >= 8



    # Pievienojam esošo gājienu
    def record(self, level, move):
        # print("RECORD {}, {}".format(self.move_list, move))
        self.move_list.append(move)
        for ltr in move[0]:
            self.blocks[ltr].translate(DIRECTIONS[move[1]])
        new_offsets_lists = list(self.get_six_offsets())
        # print("RECORD {} (from {}), level {}, new offset is {}".format(move, self.move_list, level, new_offsets_lists))

        self.prev_offsets.add(tuple(new_offsets_lists))


    def undo(self, level, move):
        # print("UNDO {}, {}".format(self.move_list, move))
        last_move = self.move_list.pop()
        for ltr in last_move[0]:
            self.blocks[ltr].translate((-1)*DIRECTIONS[last_move[1]])

    def moves(self, level):
        return MoveEnumeration(0)

block_sets = [['A'], ['B'], ['C'], ['D'], ['E'], ['F'],
              ['A', 'B'], ['A', 'C'], ['A', 'D'], ['A', 'E'], ['A', 'F'],
              ['B', 'C'], ['B', 'D'], ['B', 'E'], ['B', 'F'], ['C', 'D'],
              ['C', 'E'], ['C', 'F'], ['D', 'E'], ['D', 'F'], ['E', 'F'],
              ['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'B', 'E'], ['A', 'B', 'F'], ['A', 'C', 'D'],
              ['A', 'C', 'E'], ['A', 'C', 'F'], ['A', 'D', 'E'], ['A', 'D', 'F'], ['A', 'E', 'F']]

class MoveEnumeration:
    global block_sets
    cursor = 0
    end = 0
    next_moves = []

    # Konstruktors: iterators sāksies ar vērtību "initial" un beidzas ar max-1.
    def __init__(self, initial):
        self.next_moves = list(itertools.product(block_sets, ['X+', 'X-', 'Y+', 'Y-', 'Z+', 'Z-']))
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
    all_permutations = list(itertools.permutations(['A', 'B', 'C', 'D', 'E', 'F']))
    all_flips = list(itertools.product([0, 1], repeat=6))

    # all_permutations = [('A', 'C', 'B', 'D', 'F', 'E')]
    # all_flips = [(1, 0, 1, 1, 0, 1)]

    pp = [('A', 'C', 'B', 'D', 'F', 'E'), ('A', 'C', 'B', 'E', 'F', 'D'), ('A', 'C', 'E', 'B', 'F', 'D'), ('A', 'C', 'F', 'B', 'E', 'D'), ('A', 'D', 'B', 'C', 'E', 'F'),
          ('A', 'D', 'B', 'F', 'E', 'C'), ('A', 'D', 'E', 'B', 'F', 'C'), ('A', 'D', 'F', 'B', 'E', 'C')]
    ff = [(1, 0, 1, 1, 0, 1), (1, 0, 1, 1, 0, 1), (1, 0, 0, 1, 0, 1), (1, 0, 0, 1, 0, 1), (0, 0, 0, 1, 1, 0),
          (0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 1, 1), (0, 0, 0, 0, 1, 1) ]

    total_combinations = 0
    valid_combinations = 0
    found = False
    for perm in all_permutations:
        for flips in all_flips:
            # existing = False
            # for i in range(0):
            #     if perm == pp[i] and flips == ff[i]:
            #         existing = True
            # if existing:
            #     break

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
                    # pretty_moves = ['({}{},{})'.format(L, bcp.blocks[L].num,D) for (L, D) in bcp.move_list]
                    print('Moves: {}'.format(bcp.move_list))
                    print('  In Solution offsets are: {}'.format(bcp.get_six_offsets()))
                    print('  All visited positions: {}'.format(bcp.prev_offsets))

                    bcp.full_debug()
                    found = True
                    break
                else:
                    pass
                    #print('Could not solve!')
                    #break
        if found:
            break


def do_moves():
    global HARD_CROSS_A
    perm = ('A', 'C', 'D', 'B', 'E', 'F')
    flip = (1, 0, 1, 1, 0, 0)
    moves = [(['A'], 'Z-'), (['C'], '2Y+'), (['D'], 'Z+'), (['A', 'B', 'E'], 'Y-'),  (['A', 'B'], 'Y-'), (['E'], '3X-')]

    bpt = BurrCrossProblem(perm, flip, HARD_CROSS_A)
    print()
    print('**********  Initial State **********')
    letter_indices = [perm.index(x) + 1 for x in ['A', 'B', 'C', 'D', 'E', 'F']]
    bpt.full_debug()
    initial_offsets = list(bpt.get_six_offsets())

    for i in range(len(moves)):
        bpt.record(i, moves[i])
        numeric_moves = [(perm.index(x)+1) for x in moves[i][0]]
        print()
        print('**********  After move {}: {} = {}  **********'.format(i, moves[i], (numeric_moves, moves[i][1])))
        current_offsets = list(bpt.get_six_offsets())
        accumulated_shifts = [current_offsets[i] - initial_offsets[i] for i in range(6)]
        accumulated_shifts_dict = dict()
        for i in range(6):
            accumulated_shifts_dict[letter_indices[i]] = accumulated_shifts[i]
        sorted_shifts = sorted(accumulated_shifts_dict.items(), key=lambda x: x[0])
        halved_shifts = [(i, Point3D(pt.x//2, pt.y//2, pt.z//2)) for (i,pt) in sorted_shifts]

        print('     Accumulated shifts: {}'.format(halved_shifts))
        bpt.full_debug()

if __name__ == '__main__':
    # main()
    do_moves()

