import time
import json
import os
import shutil


def info(fn):
    def wrapper(n):
        start = time.clock()
        fn(n)
        print('function name: ', fn.__name__)
        end = time.clock()
        print('processing time: ', end-start)
        return fn(n)
    return wrapper


@info
def process(file):
    lst = json.loads(file.read())
    return sum(lst)


def check_dir(s, r, e):
    return os.path.isdir(s) and os.path.isdir(r) and os.path.isdir(e)


def monitor(source, results, errors):
    if check_dir(source, results, errors):
        txt_filenames = [f for f in os.listdir(source) if f[-3:] == 'txt']
        txt_files = list(map(lambda x: open(os.path.join(source, x), 'r'), txt_filenames))
        kv_files = dict(zip(txt_filenames, txt_files))

        for filename, file in kv_files.items():
            try:
                result = process(file)
                with open(os.path.join(results, filename), 'w') as result_file:
                    result_file.write(str(result))
            except Exception:
                shutil.copy(os.path.join(source, filename), errors)
            finally:
                file.close()
                if os.path.exists(os.path.join(source, filename)):
                    os.remove(os.path.join(source, filename))