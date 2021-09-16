from openpyxl import load_workbook

def main():
    # loading excel file
    workbook = load_workbook(filename="sample.xlsx")

    #opening workbook
    sheet = workbook.active

    # modifying the desired cell
    sheet["A1"] = "Full Name"

main()
