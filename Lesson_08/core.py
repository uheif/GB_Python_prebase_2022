import os
import shutil
import datetime


def file_exist_error(name):
    if name in os.listdir():
        raise FileExistsError('Файл с таким именем уже существует')


def list_files(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [folder for folder in os.listdir() if os.path.isdir(folder)]
    print(result)


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except:
        FileExistsError(print('Папка с таким именем уже существует'))


def delete(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except:
        FileNotFoundError(print('Такого файла или папки не существует'))


def copy(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except:
            FileNotFoundError(print('Такой папки не существует'))
    else:
        try:
            shutil.copy(name, new_name)
        except:
            FileNotFoundError(print('Такого файла не существует'))


def change_dir(dir_pass):
    try:
        os.chdir(dir_pass)
    except:
        FileNotFoundError(print('Такой папки не существует'))


def log(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')

def help():
    print('help')


if __name__ == '__main__':
    log('test')
    os.rename('task_1.py', 'core.py')
    # create_file('test.txt', 'test')
    # create_folder('new_folder')
    # delete('test.txt')
    # change_dir('new_folder')
    # change_dir('new_folder')
    # create_folder('new_folder')
    # delete('new_folder')
    # list_files()
