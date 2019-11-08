import os
import argparse
from util import write_csv_to_file
from util import load_data_from_csv
from util import read_xlsx

parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', default='input')
parser.add_argument('--output_dir', default='output')
parser.add_argument('--datavisor_dir_name', default='datavisor')
parser.add_argument('--af_dir_name', default='af')
parser.add_argument('--dv_id', default='user_id')
parser.add_argument('--af_id', default='AppsFlyer ID')
ns = parser.parse_args()

if __name__ == '__main__':
    # create dirs
    client_root = os.path.join(ns.input_dir, ns.datavisor_dir_name)
    dv_root = os.path.join(ns.input_dir, ns.af_dir_name)
    for root, subdirs, files in os.walk(dv_root):
        try:
            os.mkdir(root.replace('input', 'output'))
        except FileExistsError as e:
            pass

    # establish b
    b = set()
    for root, subdirs, files in os.walk(client_root):
        for file in files:
            if '.' not in file:
                continue
            if file.endswith('.xlsx'):
                path = os.path.join(root, file)
                t = read_xlsx(path)
            elif file.endswith('.csv'):
                path = os.path.join(root, file)
                (header, t) = load_data_from_csv(path)
            else:
                continue

            for row in t:
                if ns.dv_id in row:
                    b.add(row[ns.dv_id])

    for root, subdirs, files in os.walk(dv_root):
        for file in files:
            if '.' not in file or not file.endswith('.csv'):
                continue
            path = os.path.join(root, file)
            opath = os.path.join(path.replace('input', 'output'))
            header, a = load_data_from_csv(path)
            a = [row for row in a if ns.af_id in row and row[ns.af_id] not in b]
            write_csv_to_file(opath, header, a)
