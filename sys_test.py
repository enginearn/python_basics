import sys

def check_file_extension(file_extension):
    if len(sys.argv) > 1:
        given_file_name = sys.argv[1]
        file_extension = given_file_name.split(".")[2]
    else:
        pass
    return file_extension
