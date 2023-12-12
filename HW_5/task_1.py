'''Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.'''


def get_file_info(path):
    global extension
    last_slash = path.rfind('/')
    file_path = path[:last_slash]
    last_dot = path.rfind('.')
    if last_dot == -1:
        file_name = path[last_slash + 1:]
        extention = ''
    else:
        file_name = path[last_slash + 1:last_dot]
        extention = path[last_dot + 1:]

    return file_path, file_name, extention


print(get_file_info('/home/user/data/file'))

def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)