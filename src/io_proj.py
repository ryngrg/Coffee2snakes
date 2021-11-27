def get_input_from_file(infile):
    file_extension = infile.split('.')[-1]
    in_language = lang_from_extension(file_extension)
    if in_language == "":
        print("Unrecognized file format.")
        print("use only .c, .cpp, .java, or .py")
        input_code = []
    else:
        try:
            f = open(r"../input_files/" + infile)
        except OSError as err:
            print("File: " + infile + " not found.")
            print("OS error: {0}".format(err))
            input_code = []
        else:
            input_code = f.readlines()
            f.close()
    return in_language, input_code


def lang_from_extension(file_extension):
    if file_extension == "py":
        return "python"
    elif file_extension == "java":
        return "java"
    elif file_extension == "cpp":
        return "cplusplus"
    elif file_extension == "c":
        return "c"
    else:
        return ""


if __name__ == "__main__":
    lang, code = get_input_from_file("testfile.cpp")
    print("Language:", lang)
    print("Code: ")
    print(code)
