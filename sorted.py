import os


def count_lines(file):
    file_path_num = os.path.join(file_path, file)
    with open(file_path_num, encoding="utf-8") as f:
        return sum(1 for _ in f)


def sort_files(file_dir, func):
    file_list = os.listdir(file_dir)
    return sorted(file_list, key=func)


def gen_sorted_file(files: list, new_file: str):
    for file in files:
        file_path_num = os.path.join(file_path, file)
        with open(file_path_num, encoding="utf-8") as f, open(new_file, 'a', encoding="utf-8") as fn:
            fn.write(f'{file}\n{count_lines(file)}\n')
            t = f.read()
            fn.write(f'{t}\n')


BASE_PATH = os.getcwd()
FILE_DIR = 'files'
file_path = os.path.join(BASE_PATH, FILE_DIR)

sort_f = sort_files(file_path, count_lines)
gen_sorted_file(sort_f, 'sorted.txt')
