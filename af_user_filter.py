import os
import argparse
from util import write_csv_to_file
from util import load_data_from_csv
from util import read_xlsx

parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', default='data/input')
parser.add_argument('--output_dir', default='data/output')
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
            path = os.path.join(root, file)
            # skip office temp file
            if file.startswith('~$'):
                continue
            if file.endswith('.xlsx'):
                t = read_xlsx(path)
            elif file.endswith('.csv'):
                (header, t) = load_data_from_csv(path)
            else:
                continue

            for row in t:
                if ns.dv_id in row:
                    b.add(row[ns.dv_id])

    for root, subdirs, files in os.walk(dv_root):
        for file in files:
            # if '.' not in file or not file.endswith('.csv'):
            #     continue

            # skip office temp file
            if file.startswith('~$'):
                print("skip office temp file : {}".format(file))
                continue
            path = os.path.join(root, file)

            if file.endswith('.xlsx'):
                a = read_xlsx(path)
                header = [ns.af_id]
                output_path = os.path.join(os.path.join(root.replace(
                    'input', 'output'), file.replace('.xlsx', '_output.csv')))
            elif file.endswith('.csv'):
                output_path = os.path.join(os.path.join(root.replace(
                    'input', 'output'), file.replace('.csv', '_output.csv')))
                header, a = load_data_from_csv(path)
            else:
                continue
            if not a:
                print("Warning: file {} is empty or unreadable".format(path))
                continue
            a = [row for row in a if ns.af_id in row and row[ns.af_id] not in b]

            write_csv_to_file(output_path, header, a)
            print("original:{}, target:{}".format(path, output_path))
