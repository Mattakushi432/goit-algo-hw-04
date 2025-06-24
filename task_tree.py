import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


def display_directory_tree(directory_path: Path, prefix: str = ""):
    """ Рекурсивно обходить директорію та виводить її структуру з кольоровими форматуваннями. """

    try:
        items = sorted(list(directory_path.iterdir()), key=lambda x: x.is_file())
    except PermissionError:
        print(f"{prefix}┣━━ {Fore.RED}Відмовлено у доступі{Style.RESET_ALL}")
        return

    pointers = ["┣━━"] * (len(items) - 1) + ["┗━━"]

    for pointer, item in zip(pointers, items):
        if item.is_dir():
            print(f"{prefix}{pointer} {Fore.BLUE}{item.name}{Style.RESET_ALL}")

            extension = "┃   " if pointer == "┣━━" else "    "
            display_directory_tree(item, prefix=prefix + extension)
        else:
            print(f"{prefix}{pointer} {Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main():
    """ Головна функція запуска скрипта з командного рядка! """

    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: Вкажіть шлях до директорії.")
        print(f"Приклад викоритсання: python {sys.argv[0]} /шлях/до/директорії.")
        sys.exit(1)

    root_path = Path(sys.argv[1])

    if not root_path.exists():
        print(f"{Fore.RED}Помилка: Вказаний шлях {root_path} не існує.")
        sys.exit(1)

    if not root_path.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний шлях {root_path} не є директорією.")
        sys.exit(1)

    print(f"{Fore.YELLOW}Структура директорі {root_path}:")
    display_directory_tree(root_path)


if __name__ == "__main__":
    main()
