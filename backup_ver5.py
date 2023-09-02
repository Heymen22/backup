import os
import time
import zipfile

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\Users\\anime\\Documents', 'C:\\Code']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'E:\\Backup'  # Подставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0:  # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today)  # создание каталога
    print('Каталог успешно создан', today)


with zipfile.ZipFile(target, "w") as outzip:
    for path in source:
        for subdir, dirs, files in os.walk(path):
            for file in files:
                # Read file
                srcpath = os.path.join(subdir, file)
                dstpath_in_zip = os.path.relpath(srcpath, start=path)
                with open(srcpath, 'rb') as infile:
                    # Write to zip
                    outzip.writestr(dstpath_in_zip, infile.read())
# try:
#     # Создаем архив если его нет и открываем его на запись
#     with zipfile.ZipFile(target, mode='x') as archive:
#         for path in source:
#             # Записываем файлы в архив
#             archive.write(path)
#
# except FileExistsError as e:
#     print('Такой архив уже существует!')
# except Exception as e:
#     print('Создание резервной копии НЕ УДАЛОСЬ')
#     print('Ошибка:', e)
# else:
#     print('Резервная копия успешно создана в', target)
