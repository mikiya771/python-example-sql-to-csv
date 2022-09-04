import os

import dotenv
import mysql.connector

import story.salaly_employee_no as story1


def get_connector(host, port, user, password, database: str):
    return mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )


def main():
    dotenv.load_dotenv(dotenv_path="test.env", override=True)
    print(os.getenv("MYSQL_HOST"))
    main_database = get_connector(
        os.getenv("MYSQL_HOST", "localhost"),
        os.getenv("MYSQL_TCP_PORT", 3306),
        "root",
        os.getenv("MYSQL_ROOT_PASSWORD", "test"),
        "employees"
    )
    story1.save_salaryman(main_database)
    main_database.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
