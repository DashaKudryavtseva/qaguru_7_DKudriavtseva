import csv
from zipfile import ZipFile
import pytest
from openpyxl import load_workbook


@pytest.fixture
def archiving_files():
    files_for_pack = ["file_example_XLSX_10.xlsx", "sample.pdf", "username.csv"]
    with ZipFile("Simple.zip", mode="w") as zip_file:
        for file in files_for_pack:
            zip_file.write(file)


def xlsx_content_check(file):
    print("пришли")
    xl_file = load_workbook((file))
    s = xl_file.active
    name_s = xl_file.sheetnames
    assert len(name_s) == 1
    assert name_s[0] == "Sheet1"
    assert s.max_row == 10
    assert s.max_column == 8
def csv_content_check(file):
    with open(file) as csv_file:
        csv_file = csv.reader(csv_file)
        for r in csv_file:
            print(r)
        row_count = sum(1 for row in csv_file)
        assert row_count == 6
        for r in csv_file:
            print(r)


def test_check_zip_xlsx():
    with ZipFile("Simple.zip") as check_zip:
        name_files = check_zip.namelist()
        for file in name_files:
            if ".xlsx" in file:
                assert file == "file_example_XLSX_10.xlsx"
                xlsx_content_check(file)


def test_check_zip_csv():
    with ZipFile("Simple.zip") as check_zip:
        name_files = check_zip.namelist()
        for file in name_files:
            if ".csv" in file:
                assert file == "username.csv"
                csv_content_check(file)

