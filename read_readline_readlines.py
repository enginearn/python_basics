target_file_txt = "target_file.txt"
sep = "=="
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
