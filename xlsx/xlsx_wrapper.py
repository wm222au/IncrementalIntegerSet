import xlsxwriter
import os.path
from tabulate import tabulate
import pandas as pd


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


def append_existing_xlsx(name, content):
    xl = pd.ExcelFile(name)
    existing_data_frame = xl.parse()
    additional_data_frame = pd.DataFrame(content)

    frames = [existing_data_frame, additional_data_frame]

    concat_data_frame = pd.concat(frames)

    concat_data_frame.to_excel(name, index=False)


def write_clean_xlsx(name, content):
    new_data_frame = pd.DataFrame(content)
    new_data_frame.to_excel(name, index=False)


def create_xlsx_sheet(content, name, append=None):
    full_path = name + '.xlsx'
    if append:
        if file_exists(full_path):
            append_existing_xlsx(full_path, content)
        else:
            write_clean_xlsx(full_path, content)

    else:
        generated_name = get_available_file_name(name)
        write_clean_xlsx(generated_name, content)
