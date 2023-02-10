import copy
import cell

class Spreadsheet:
    def __init__(self, row, column):
        if isinstance(row, int) and isinstance(column, int) and row > 0 and column > 0:
            self.row = row
            self.column = column
            self.spreadsheet = [[cell.Cell() for x in range(column)] for y in range(row)]
        else:
            raise ValueError

    def setCellAt(self, row:int, column:int, val: cell.Cell or str):
        if 0 <= row < self.row and 0 <= column < self.column:
            if isinstance(val, cell.Cell):
                self.spreadsheet[row][column] = copy.deepcopy(val)
            else:
                self.spreadsheet[row][column].setValue(val)

    def getCellAt(self, row:int, column:int):
        if isinstance(row, int) and isinstance(column, int) and 0 < row < self.row and 0 < column < self.column:
            return self.spreadsheet[row][column]
        else:
            raise ValueError

    def addRow(self, row:int):
        if 0 <= row < self.row:
            self.spreadsheet.insert(row, [cell.Cell() for y in range(self.column)])
            self.row += 1
        else:
            raise ValueError


    def removeRow(self, row:int):
        if 0 <= row < self.row:
            del self.spreadsheet[row]
            self.row -= 1
        else:
            raise ValueError


    def addColumn(self, column:int):
        if 0 <= column < self.column:
            for x in self.spreadsheet:
                x.insert(column, cell.Cell())
            self.column += 1
        else:
            raise ValueError


    def removeColumn(self, column:int):
        if 0 <= column < self.column:
            for x in self.spreadsheet:
                del x[column]
            self.column -= 1
        else:
            raise ValueError


    def swapRows(self, row1:int, row2:int):
        if 0 <= row1 < self.row and 0 <= row2 < self.row:
            self.spreadsheet[row1], self.spreadsheet[row2] = self.spreadsheet[row2], self.spreadsheet[row1]
        else:
            raise ValueError

    def swapColumns(self, col1:int, col2:int):
        if 0 <= col1 < self.column and 0 <= col2 < self.column:
            self.spreadsheet[col1], self.spreadsheet[col2] = self.spreadsheet[col2], self.spreadsheet[col1]
        else:
            raise ValueError
