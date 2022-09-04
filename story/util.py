import csv
import enum


def get_employee_info(db_connector,
                      list_of_employee_no) -> tuple[tuple, list[tuple]]:
    keys = ("従業員番号", "所属部署番号", "日付")
    cursor = db_connector.cursor(prepared=True)
    stmt_formats = ','.join(['?'] * len(list_of_employee_no))
    stmt_employee_info = '''
select
       mid_e_d.emp_no,
       mid_e_d.dept_no,
       mid_e_d.from_date
from dept_manager as mid_e_d
join employees e on mid_e_d.emp_no = e.emp_no
join departments d on mid_e_d.dept_no = d.dept_no
where mid_e_d.emp_no IN (%s)
order by mid_e_d.to_date;
    '''
    cursor.execute(stmt_employee_info % stmt_formats,
                   tuple(list_of_employee_no))
    rows = cursor.fetchall()
    cursor.close()
    return keys, rows


class FileWriteMode(enum.Enum):
    WRITE = 'w'
    APPEND = 'a'


def save_tuple_list_as_csv(tuple_list,
                           file_name_with_csv_extension,
                           mode: FileWriteMode):
    with open(file_name_with_csv_extension, mode.value) as f:
        writer = csv.writer(f)
        for t in tuple_list:
            writer.writerow(list(t))


def add_annotation_to_key_and_data(keys, key_annotation, data, data_annotation):

    ret_keys = keys + (key_annotation,)
    ret_values = []
    for i, value in enumerate(data):
        ret_value = value + (data_annotation,)
        ret_values.append(ret_value)
    return ret_keys, ret_values
