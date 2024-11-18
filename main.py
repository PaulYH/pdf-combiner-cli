import argparse
from pypdf import PdfWriter
from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser(description='CLI tool for PDF merging')
parser.add_argument('files', type=str, nargs='+', help='PDF file names')

raw_list = parser.parse_args().files
file_list = []

if '.' in raw_list:
    files_in_dir = [f for f in listdir('.') if isfile(join('.', f))]
    file_list = list(filter(lambda file : file.endswith('.pdf'), files_in_dir))
else:
    file_list = list(filter(lambda file : file.endswith('.pdf'), raw_list))

try:
    merger = PdfWriter()

    print('MERGING:')
    for pdf in file_list:
        print(f"   {pdf}")
        merger.append(pdf)

    merger.write('combinepdf.pdf')
    merger.close()
except Exception as e:
    merger.close()
    print(f"ERROR: {e}")
    exit(code=1)

parser.exit("\nFiles merged successfully!")

exit(code=0)