from openpyxl import *


def main():
    # loading excel file
    workbook = load_workbook(filename="sample.xlsx")

    # opening workbook
    sheet = workbook.active

    total = 0

    for cell in sheet('E'):
        print(cell.value)

    workbook.save(filename="sample.xlsx")


main()
