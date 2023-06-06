import zipfile

with zipfile.ZipFile('vehicle-claim-fraud-detection.zip', 'r') as zip_ref:#Введите другое имя файла если скачаете другой файл
    zip_ref.extractall('.')
