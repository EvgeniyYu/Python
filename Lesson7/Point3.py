class Cell:
    def __init__(self, cnt_points):
        self.__cnt_points = cnt_points
    def __add__(self, other):
        return  Cell(self.__cnt_points + other.__cnt_points)
    def __sub__(self, other):
        val = self.__cnt_points - other.__cnt_points
        if val < 0:
            return 'Result is less zero'
        else:
            return Cell(val)
    def __mul__(self, other):
        val = self.__cnt_points * other.__cnt_points
        return Cell(val)
    def __truediv__(self, other):
        val = self.__cnt_points // other.__cnt_points
        return Cell(val)
    def __str__(self):
        return str(self.__cnt_points)
    def make_order(self, new_cnt_points):
        sResult = ''
        for i in range(1, self.__cnt_points + 1):
            if i == new_cnt_points:
                sResult += '*\n'
                new_cnt_points *= 2
                continue
            sResult += '*'
        return sResult


cell1 = Cell(15)
cell2 = Cell(4)
cell_add = cell1 + cell2
cell_sub = cell1 - cell2
cell_mult = cell1 * cell2
cell_div = cell1 / cell2
print(f'Add: {cell_add} Sub: {cell_sub} Multi: {cell_mult} Div: {cell_div}')
print(f'Cells look like as:\n{cell1.make_order(5)}')
