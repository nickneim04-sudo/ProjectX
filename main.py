from models.transaction import Transaction
from models.category import Category


def main():
    """Точка входа в приложение Personal Finance Assistant."""

    # Создание категорий
    food = Category("Food", "expense")
    salary = Category("Salary", "income")

    # Создание транзакций
    t1 = Transaction(500, food.name, "2023-10-25", "expense")
    t2 = Transaction(3000, salary.name, "2023-10-24", "income")

    # Вывод данных в консоль
    print("Категории:")
    print(food)
    print(salary)

    print("\nТранзакции:")
    print(t1)
    print(t2)


if __name__ == "__main__":
    main()
