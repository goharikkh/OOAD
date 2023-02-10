import cell
import spreadsheet as sp
import datetime

#testing Cell functions
def  testing_cell(obj: cell.Cell, val, color):
    obj.setValue(val)
    if obj.getValue() == str(val):
        print("get | set_value - passed")
    else:
        print("get | set_value - failed")

    obj.setColor(color)
    try:
        colors = {0: "white",
                  1: "black",
                  2: "green",
                  3: "purple",
                  4: "yellow"}
        if obj.getColor() == colors[color]:
            print("get | set_color - passed")
        else:
            print("get | set_color - failed")
    except ValueError:
        print("get | set_color - passed")


    try:
        if obj.toInt() == int(val):
            print("toInt passed")
        else:
            print("toInt failed")
    except ValueError:
        print("toInt passed")


    try:
        if obj.toFloat() == float(val):
            print("toFloat passed")
        else:
            print("toFloat failed")
    except ValueError:
        print("toFloat passed")

    try:
        if obj.toDate() != datetime.date(val[:4], val[5:7], val[8:]):
            print("toDate failed")
        else:
            print("toDate passed")
    except ValueError:
        print("toDate passed")



    obj.reset()
    if obj.getValue() == "" and obj.getColor() == "white":
        print("reset passed")
    else:
        print("reset failed")

test_cell = cell.Cell()
testing_cell(test_cell, "hello", 1)




def spread_set(obj: sp.Spreadsheet, row, column, val):
    obj.setCellAt(row, column, val)

    if isinstance(val, cell.Cell):
        if obj.getCellAt(row, column).getValue() == val.getValue() and obj.getCellAt(row, column).getColor() == val.getColor():
            print("sp get | set - passed")
        else:
            print("sp get | set - failed")

    else:
        if obj.getCellAt(row, column).getValue() == str(val):
            print("sp set | get - passed")
        else:
            print("sp get | set - failed")

test_cell = cell.Cell()
test_sp = sp.Spreadsheet(10, 10)
spread_set(test_sp, 5, 5, test_cell)

def add_row_testing(obj : sp.Spreadsheet, row):
    skzbnakan = obj.row
    obj.addRow(row)
    try:
        if obj.row == skzbnakan + 1 :
            print("add_row passed")
        else:
            print("add_row failed")
    except ValueError:
        print("add_row passed")

add_row_testing(test_sp, 2)

def remove_row_testing(obj : sp.Spreadsheet, row):
    skzbnakan = obj.row
    obj.removeRow(row)
    try:
        if obj.row == skzbnakan - 1:
            print("add_row passed")
        else:
            print("add_row failed")
    except ValueError:
        print("add_row passed")


remove_row_testing(test_sp, 2)


def add_column_testing(obj : sp.Spreadsheet, column):
    skzbnakan = obj.column
    obj.addColumn(column)
    try:
        if obj.column == skzbnakan + 1:
            print("add_column passed")
        else:
            print("add_column failed")
    except ValueError:
        print("add_column passed")

add_column_testing(test_sp, 2)


def remove_column_testing(obj : sp.Spreadsheet, column):
    skzbnakan = obj.column
    obj.removeColumn(column)
    try:
        if obj.column == skzbnakan - 1:
            print("add_column passed")
        else:
            print("add_column failed")
    except ValueError:
        print("add_column passed")

remove_column_testing(test_sp, 2)

def test_swap_rows(obj : sp.Spreadsheet, row1, row2):
    try:
        obj.setCellAt(row1, 1, "hello1")
        obj.setCellAt(row2, 1, "hello2")
        obj.swapRows(row1, row2)
        if obj.getCellAt(row1, 1).getValue() == "hello2" \
            and obj.getCellAt(row2, 1).getValue() == "hello1":
            print("swap rows passed")
        else:
            print("swap rows failed")
    except ValueError:
        print("swap rows passed")

test_swap_rows(test_sp, 1, 2)

def test_swap_columns(obj : sp.Spreadsheet, col1, col2):
    obj.setCellAt(1, col1, "hello1")
    obj.setCellAt(1, col2, "hello2")
    obj.swapColumns(col1, col2)
    if obj.getCellAt(1, col1).getValue() == "hello2" and \
            obj.getCellAt(1, col2).getValue() == "hello1":
        print("swap cols passed")
    else:
        print("swap cols failed")

test_swap_columns(test_sp, 1, 2)






