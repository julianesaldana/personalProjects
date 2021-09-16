from openpyxl import load_workbook


def main():
    # loading excel file
    workbook = load_workbook(filename="sample.xlsx")

    # opening workbook
    sheet = workbook.active

    # modifying the desired cell
    sheet["D13"] = 120
    sheet["D14"] = 50
    sheet["D15"] = 30

    workbook.save(filename="sample.xlsx")


main()
