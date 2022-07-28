import sys
f = sys.argv[1]

def check_file_extension(f):
    if len(sys.argv) > 1:
        given_file_name = sys.argv[1]
        file_extension = given_file_name.split(".")[2]
    else:
        print("No files...")
    return file_extension

result1 = check_file_extension(f)
result2 = check_file_extension(sys.argv[1])
print(result1)
print(result2)
