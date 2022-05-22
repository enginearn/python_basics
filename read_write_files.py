import csv
import json
import sys
from tokenize import group

given_file = ""
detect_file_extension = ""
target_file_txt = "target_file.txt"
sep = "=="

target_file_json = "target_file.json"
target_file_csv = "target_file.csv"

output_file_txt = "requirements.txt"
output_file_json = "requirements_from_json.txt"
output_file_csv = "requirements_from_csv.txt"

# ファイルから読み込まない場合
targets = [
    "ansible==5.8.0",
    "ansible-core==2.12.5",
    "cffi==1.15.0",
    "cryptography==37.0.2",
    "Jinja2==3.1.2",
    "MarkupSafe==2.1.1",
    "packaging==21.3",
    "pycparser==2.21",
    "pyparsing==3.0.9",
    "PyYAML==6.0",
    "resolvelib==0.5.4"
]

print(f"リスト内包表記: \n", [target.split("==")[0] for target in targets])

# read(), readline(), readlines()の動作を確認
with open(target_file_txt, "r") as tf:
    data = tf.read()
    print(f"read(): {type(data)}")
    print(f"txtの中身: \n{data}")
    print([target.split(sep)[0] for target in list(data)])

with open(target_file_txt, "r") as tf:
    data = tf.readline()
    print(f"readline(): {type(data)}")
    print([target.split(sep)[0] for target in list(data)])

with open(target_file_txt, "r") as tf:
    data = tf.readlines()
    print(f"readlines(): {type(data)}")
    print([target.split(sep)[0] for target in list(data)])

def check_file_extension(given_file):
    if len(sys.argv) > 1 :
        given_file = sys.argv[1]
        given_file_name = given_file.split(".")[1]
        file_extension = given_file.split(".")[2]
        print(f"拡張子: {file_extension}")
        return file_extension
        
# テキストファイル読み込みと書き出し用にそれぞれを関数化
def read_and_sep(target_file_txt):
    if target_file_txt or detect_file_extension == "txt":
        with open(target_file_txt, "r") as tf:
            data = tf.readlines()
            results_txt = [target.split(sep)[0] for target in list(data)]
            print(f"results_txt: {type(results_txt)}\nread_and_sep関数のresults_txtの中身: {results_txt}")
        return results_txt

def out_file(results_txt):
    with open(output_file_txt, "w", newline="") as of:
        for result in results_txt:
            of.write(result + "\n")

# JSONファイルの読み出しと書き出し関数
def json_read(target_file_json):
    if target_file_json or detect_file_extension == "json":
        with open(target_file_json, "r") as jf:
            read_json = jf.read()
            json_file = json.dumps(read_json)
            json_file = json.loads(read_json)
            results_json = [k["name"] for k in json_file]
        return results_json

def json_out(results_json):
    with open(output_file_json, "w") as jw:
        for result_json in results_json:
            jw.writelines(result_json + "\n")

# CSVファイルの読み出しと書き出し関数
def csv_read(target_file_csv):
    if target_file_csv or detect_file_extension == "csv":
        with open(target_file_csv, "r") as cf:
            data = csv.reader(cf, delimiter=" ")
            header = [next(data) for _ in range(2)]
            results_csv = [d[0] for d in data]
        return results_csv

def csv_out(results_csv):
    with open(output_file_csv, "w") as co:
        for d in results_csv:
            co.write(d + "\n")

def main():

    detect_file_extension = check_file_extension(given_file)

    results = read_and_sep(target_file_txt)
    out_file(results)

    results = json_read(target_file_json)
    json_out(results)

    results = csv_read(target_file_csv)
    csv_out(results)

if __name__ == "__main__":
    main()
