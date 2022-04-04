from core import list_files, create_file, create_folder, delete, change_dir, copy, log, help
import sys

print('file manager')
log('start')
try:
    command = sys.argv[1]
except:
    IndexError(help())
else:
    if command == 'new_file':
        try:
            name = sys.argv[2]
        except:
            IndexError()
        else:
            create_file(name)
    elif command == 'new_folder':
        try:
            name = sys.argv[2]
        except:
            IndexError()
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except:
            IndexError()
        else:
            delete(name)
    elif command == 'ch_dir':
        try:
            name = sys.argv[2]
        except:
            IndexError()
        else:
            change_dir(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except:
            IndexError()
        else:
            copy(name, new_name)
    elif command == 'list':
        list_files()
    else:
        help()

log('end')