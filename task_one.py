def total_salary(path):
    try:

        total_salary_sum = 0
        developer_count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                total_salary_sum += int(parts[1])
                developer_count += 1

        if developer_count == 0:
            return 0, 0

        average_salary = total_salary_sum / developer_count
        return total_salary_sum, average_salary

    except FileNotFoundError:
        print(f" Файл за шляхом {path} не знайдено.")
        return 0, 0
    except (ValueError, IndexError) as e:
        print(f"Файл пошкоджено фбо має невірний формат. {e}")
        return 0, 0


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, середня заробітна плата: {int(average)}")