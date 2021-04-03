# 2. Create a script with arguments:
#
# source_file_path; required: true;
# start_salary; required: false; help: starting point of salary;
# end_salary; required: false; help: the max point of salary;
# position; required: false; help: position role
# age; required: false; help: Age of person
# language; required: false; help; Programming language
#
# Based on this info generate a new report of average salary.

import argparse
import csv


parser = argparse.ArgumentParser(description=f"The script should read the .csv file "
                                             f"and get the information based on your input"
                                             f" and generate a new .csv file with that info")


parser.add_argument("--source_file_path", "-f", required=True)
parser.add_argument("--start_salary", "-s", required=False, help="starting point of salary")
parser.add_argument("--end_salary", "-e", required=False, help="the max point of salary")
parser.add_argument("--position", "-p", required=False, help="position role")
parser.add_argument("--age", "-a", required=False, help="Age of person")
parser.add_argument("--language", "-l", required=False, help="Programming language")
args = parser.parse_args()

titles_for_filter = {}
if args.position:
    titles_for_filter.update({"Должность": args.position})
if args.age:
    titles_for_filter.update({"Возраст": args.age})
if args.language:
    titles_for_filter.update({"Язык.программирования": args.language})

salaries = []
with open(args.source_file_path, "r") as file:
    reader = csv.DictReader(file)
    for el in reader:
        salary = int(el["Зарплата.в.месяц"])
        check = True
        for key, value in titles_for_filter.items():
            if el[key] != value:
                check = False
                break
        if not check:
            continue
        if args.start_salary:
            if salary < int(args.start_salary):
                continue
        if args.end_salary:
            if salary > int(args.end_salary):
                continue
        salaries.append(salary)

result = None
if salaries != []:
    result = sum(salaries) / len(salaries)

print(result)

