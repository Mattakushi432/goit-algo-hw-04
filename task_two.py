def get_cats_info(path):
    try:
        cats_list = []

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue

                parts = cleaned_line.split(',')
                if len(parts) == 3:
                    cat_info = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats_list.append(cat_info)
                else:
                    print(f"Некоректний формат рядка, рядок пропущено: {cleaned_line}")
        return cats_list
    except FileNotFoundError:
        print(f"Помилка: файл за шляхом {path} не знайдено!")
        return []
    except Exception as e:
        print(f"Сталося помилка при читанні файлу: {e}")
        return []


cats_info = get_cats_info("cats_list.txt")
print("[")
for cat in cats_info:
    print(f"    {cat},")
print("]")
