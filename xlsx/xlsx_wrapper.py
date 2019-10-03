import xlsxwriter
import os.path
from tabulate import tabulate

def generate_output(output, name, content, append=None):
    if output == "cli":
        print(tabulate(content, headers=["Id", "Number"]))
    elif output == "xlsx":
        create_xlsx_sheet(content, name, append)
    else:
        print("Only CLI and XLSX is available as output types at the moment")


def file_exists(name):
    return os.path.exists(name)


def get_available_file_name(name):
    fsCount = 1
    original_name = name
    name = name + '.xlsx'
    while file_exists(name):
        name = original_name + '-' + str(fsCount) + '.xlsx'
        fsCount += 1

    return name


def create_xlsx_sheet(content, name, append=None):
    if append:
        name = get_available_file_name(name)

    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet()

    row = 0

    for col, data in enumerate(content):
        worksheet.write_row(row, 0, data)
        row += 1

    workbook.close()