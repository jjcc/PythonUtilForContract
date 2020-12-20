import os



def pywalker(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file_ in files:
            ignore = True
            #for ext in (".pdf",".zip",".doc",".txt"):
            for ext in (".jpg",".@@@"):
                if file_.endswith(ext):
                    ignore = False
                    break
            if ignore:
                continue

            file_with_path = os.path.join(root, file_)
            size_of_file = os.path.getsize(file_with_path)
            total_size += size_of_file
            print("%s  %d"%(file_with_path,total_size))


if __name__ == '__main__':
    dir_to_check = 'C:'
    pywalker(dir_to_check)