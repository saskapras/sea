# === Stage 60: Добавь финальную справку по командам и примеры использования ===
# Project: SupportQueue
import sys

def main():
    if len(sys.argv) < 2:
        print("Использование: python support_queue.py <команда> [аргументы]")
        print()
        print("Доступные команды:")
        print("  add --priority <1-3> --status <новый> --message <текст> [--ticket <id>] [--customer <имя>]")
        print("  list [--status <статус>] [--priority <1-3>] [--unassigned]")
        print("  show <ticket_id>")
        print("  assign <ticket_id> --agent <имя>")
        print("  respond <ticket_id> --message <текст> [--priority <1-3>]")
        print("  close <ticket_id>")
        print("  sla <ticket_id>")
        print("  help")

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    if command == "help" or command == "--help" or command == "-h":
        main()
    elif command == "add":
        print("Добавление заявки (пример):")
        print("  python support_queue.py add --priority 2 --status new \\")
        print("    --message \"Проблема с оплатой\" --customer Иванов")
        print()
        print("Приоритеты: 1 = низкий, 2 = средний, 3 = высокий")
    elif command == "list":
        print("Пример вывода списка:")
        print("  python support_queue.py list")
        print("  python support_queue.py list --status open")
        print("  python support_queue.py list --unassigned")
    elif command == "show":
        print("Показать детали заявки:")
        print("  python support_queue.py show 1001")
    elif command == "assign":
        print("Назначить ответственного:")
        print("  python support_queue.py assign 1001 --agent Мария")
    elif command == "respond":
        print("Добавить ответ с пересчётом SLA:")
        print("  python support_queue.py respond 1001 \\")
        print("    --message \"Спасибо, работаем над этим\" --priority 3")
    elif command == "close":
        print("Закрыть заявку:")
        print("  python support_queue.py close 1001")
    elif command == "sla":
        print("Показать статус SLA для заявки:")
        print("  python support_queue.py sla 1001")
    else:
        print(f"Неизвестная команда: {command}")
        print("Введите 'help' для списка команд.")

if __name__ == "__main__":
    main()
