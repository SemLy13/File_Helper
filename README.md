#File Management
Проект реализован на python с помощью фреймворка Flask, также понадобились несколько файлом HTML

####Возможности :
- загрузка датасетов с Kaggle в формате csv
- Получение списка файлов с информацией о колонках
- Возможность получения данных из конкретного файла с опциональными фильтрацией и сортировкой по одному или нескольким столбцам
- Покрытие исходного кода тестами
- Авторизация пользователя
---
####Из чего состоит проект:
- main.py основной файл для запуска программы, который содержит код Flask-приложения, которое позволяет загрузить CSV файлы на сервер, просмотреть их и сортировать данные в этих файлах
- base.html файл от которого наследуются последующие html файлы (file.html, files.html, upload.html). Нужен чтобы закрепить кнопки в верхней части экрана
- test_app.py файл для покрывающий исходный код тестами
- MyUnzip.py файл для распаковки зиповских файлов полученных с kaggle
---
####Перед запуском программы
#####1. В терминале прописать несколько команд:
    pip install Flask
    pip install Flask-HTTPAuth
    pip install pandas
    pip install pytest Flask-Testing
    pip install kaggle

Для запуска тестов пропишите(но сначала запустите программу и добавьте туда CAR.csv):

    python test_app.py

---
###Kaggle
В терминале можно прописать

    kaggle datasets list -s 'ключевые слова для поиска датасетов'
    kaggle datasets download -d 'имя из найденых датасетов для загрузки'

Лично я нашёл и распокавал это:

    kaggle datasets list -s 'fraud detection
    kaggle datasets download -d 'shivamb/vehicle-claim-fraud-detection'
Вы можете найти и скачать другой, в целом это не играет никакой роли. Также изначально имеется файл CAR.csv, это заранее скачанный мой файл, который я использовал для обучения ML.

---

###Работа с сайтом
1. После запуска программы перейдите по ссылке http://127.0.0.1:5000 

2. Далее вам нужно ввести:
    - Имя пользователя 'adm'
    - Пороль 'psw'

3. Затем выбираете файл csv и нажимаете кнопку upload для загрузки файла
4. После загрузки вас перекинет на http://127.0.0.1:5000/files где будут написаны имена скачанных файлов и название столбцов
5. Сортировка
http://127.0.0.1:5000/file?filename=CAR.csv&sort=name:asc
В этом запросе:

    - filename=CAR.csv указывает на файл, который нужно отсортировать.
    - sort=name:asc указывает на сортировку. Данные будут отсортированы по полю name в порядке возрастания (asc), для убывания (desc).

6. Сортировка по нескольким столбцам
http://127.0.0.1:5000/file?filename=CAR.csv&sort=name:asc,selling_price:desc
В этом запросе:
    - filename=CAR.csv указывает на файл, который нужно отсортировать.
    - sort=name:asc,selling_price:desc указывает на сортировку. Сначала данные будут отсортированы по полю name в порядке возрастания (asc), а затем - по полю selling_price в порядке убывания (desc).
7. После загрузки файла CAR.csv запустите тесты
в терминале :
`python test_app.py`



    
