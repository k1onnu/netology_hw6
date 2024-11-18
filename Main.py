import csv

def process_files(visit_log_file_path, purchases_file_path, output_file_path):
    # Загружаем данные о покупках в словарь
    purchases = {}
    with open(purchases_file_path, mode='r', encoding='utf-8') as purchases_file:
        purchases_reader = csv.reader(purchases_file)
        for row in purchases_reader:
            user_id = row[0]
            category = row[1]
            purchases[user_id] = category

    # Открываем файл visit_log.csv и funnel.csv
    with open(visit_log_file_path, mode='r', encoding='utf-8') as visit_log_file, \
            open(output_file_path, mode='w', encoding='utf-8', newline='') as funnel_file:
        visit_log_reader = csv.reader(visit_log_file)
        funnel_writer = csv.writer(funnel_file)
        funnel_writer.writerow(['user_id', 'source', 'category'])

        # Обрабатываем каждую строку в visit_log.csv
        for visit_row in visit_log_reader:
            user_id = visit_row[0]
            source = visit_row[1]
            if user_id in purchases:
                category = purchases[user_id]
                funnel_writer.writerow([user_id, source, category])


if __name__ == "__main__":
    visit_log_file_path = input("Введите путь к файлу visit_log.csv: ")
    purchases_file_path = input("Введите путь к файлу purchases.csv: ")
    output_file_path = input("Введите путь к выходному файлу funnel.csv: ")
    process_files(visit_log_file_path, purchases_file_path, output_file_path)
