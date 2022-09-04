import story.util as util

key_annotation = "データ種別"
data_annotation = "給料の履歴が10件以上の従業員情報"
stmt_most_salary_changed_emp_no_list = '''
select e.emp_no from dept_manager as mid_e_d
join employees e on mid_e_d.emp_no = e.emp_no
join departments d on mid_e_d.dept_no = d.dept_no
join salaries s on e.emp_no = s.emp_no
group by e.emp_no
having count(s.salary) > 10
order by count(s.salary) desc;
'''


def get_salary_employee_no(db_connectror):
    cursor = db_connectror.cursor(prepared=True)
    cursor.execute(stmt_most_salary_changed_emp_no_list)
    rows = cursor.fetchall()
    most_salary_changed_emp_no_list = []
    for row in rows:
        most_salary_changed_emp_no_list.append(row[0])
    cursor.close()
    return most_salary_changed_emp_no_list


def save_salaryman(db_connector):
    csv_name = "salaryman.csv"
    nums = get_salary_employee_no(db_connector)
    keys, data = util.get_employee_info(db_connector, nums)

    keys, data = util.add_annotation_to_key_and_data(keys,
                                                     key_annotation,
                                                     data,
                                                     data_annotation)
    ret = [keys] + data

    util.save_tuple_list_as_csv(ret, csv_name, util.FileWriteMode.WRITE)
