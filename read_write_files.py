import csv
import json
import sys

EXPECTED_FILE_EXTENSION = ["txt", "csv", "json"]
target_file = ""

target_file_txt = "target_file.txt"
sep = "=="
target_file_json = "target_file.json"
# target_file_csv = "target_file.csv"
target_file_csv = ""

output_file_txt = "requirements.txt"
output_file_json = "requirements_from_json.txt"
output_file_csv = "requirements_from_csv.txt"

# ファイル拡張子を判定
def detect_file_extension(give_file):
    if len(sys.argv) > 1:
        print(f"check give_file: {target_file}")
        given_file_name = target_file.split(".")[1]
        file_extension = target_file.split(".")[2].lower()

        if file_extension in EXPECTED_FILE_EXTENSION:
            return file_extension, give_file

        else:
            raise ValueError(f"拡張子: {file_extension}は、わかりません...")

    else:
        pass

# テキストファイル読み込みと書き出し用にそれぞれを関数化
def read_and_sep(target_file = target_file_txt, file_extension = "txt"):
    if  target_file or file_extension == "txt":
        with open(target_file, "r") as tf:
            data = tf.readlines()
            results_txt = [target.split(sep)[0] for target in list(data)]
            print(f"read_sep func results_txt: {type(results_txt)}\nread_and_sep関数のresults_txtの中身: {results_txt}")
        return results_txt

def out_file(results_txt):
    with open(output_file_txt, "w", newline="") as of:
        print(f"results_txt: {results_txt}")
        for result in results_txt:
            of.write(result + "\n")

# JSONファイルの読み出しと書き出し関数
def json_read(target_file = target_file_json, file_extension = "json" ):
    if target_file or file_extension == "json":
        with open(target_file, "r") as jf:
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
def csv_read(target_file, file_extension = "csv"):
    if target_file or file_extension == "csv":
        print(f"csv_read: {file_extension}")

        with open(target_file, "r") as cf:
            data = csv.reader(cf, delimiter=" ")
            header = [next(data) for _ in range(2)]
            results_csv = [d[0] for d in data]
            print(f"csv_read func results_csv: {type(results_csv)}\ncsv_read関数のresults_txtの中身: {results_csv}")
        return results_csv

def csv_out(results_csv):
    print(f"csv_out results_csv: {results_csv}")
    with open(output_file_csv, "w") as co:
        for d in results_csv:
            co.write(d + "\n")

def main():
    print("main called!")
    detect_file_extension(sys.argv[1])
    print(f"main(): {type(target_file)}")

    results = read_and_sep(target_file = target_file_txt)
    out_file(results)

    results = json_read(target_file = target_file_json)
    json_out(results)

    results = csv_read(target_file)
    csv_out(results)

if __name__ == "__main__":
    main()
