# In the homework directory you can find the directory arg_parser_homework where you can find 2020_june_mini.csv file.
#
# 1. Create a script with arguments:
#
# exp; required: false; default: min(exp)
# current_job_exp; required: false; default: max(current_job_exp)
# sex; required: false
# city; required: false
# position; required: false
# age; required: false
# path_to_source_files; required: true;
# destination_path; required: false; default: .
# destination_filename; required: false; default: f"2020_june_mini.csv".
# The script should read the .csv file and get the information based on your input and generate a new .csv
# file with that info
#
# Example of input:
# -exp 3 -sex female -position DevOps -city Kyiv --path_to_source_files . ...

import argparse
import csv


parser = argparse.ArgumentParser(description=f"The script should read the .csv file "
                                             f"and get the information based on your input"
                                             f" and generate a new .csv file with that info")


parser.add_argument("--path_to_source_files", "-t", required=True)
parser.add_argument("--exp", "-e", required=False, default="min(exp)")
parser.add_argument("--current_job_exp", "-j", required=False, default="max(current_job_exp)")
parser.add_argument("--sex", "-s", required=False)
parser.add_argument("--city", "-c", required=False)
parser.add_argument("--position", "-p", required=False)
parser.add_argument("--age", "-a", required=False)
parser.add_argument("--destination_path", "-d", required=False, default="")
parser.add_argument("--destination_filename", "-f", required=False, default=f"2020_june_mini.csv")
args = parser.parse_args()

titles_for_filter = {}
if args.sex:
    titles_for_filter.update({"Пол": args.sex})
if args.city:
    titles_for_filter.update({"Город": args.city})
if args.position:
    titles_for_filter.update({"Должность": args.position})
if args.age:
    titles_for_filter.update({"Возраст": args.age})

with open(args.path_to_source_files, "r") as file:
    reader = csv.DictReader(file)
    head = reader.fieldnames
    output = []
    for el in reader:
        if args.exp == "min(exp)":
            if output != []:
                if el["exp"] > output[-1]["exp"]:
                    continue
                elif el["exp"] < output[-1]["exp"]:
                    output = []
        else:
            if el["exp"] != args.exp:
                continue
        if args.current_job_exp == "max(current_job_exp)":
            if output != []:
                if el["current_job_exp"] < output[-1]["current_job_exp"]:
                    continue
                elif el["current_job_exp"] > output[-1]["current_job_exp"]:
                    output = []
        else:
            if el["current_job_exp"] != args.current_job_exp:
                continue
        check = True
        for title, value in titles_for_filter.items():
            if el[title] != value:
                check = False
                break
        if check:
            output.append(el)

with open(args.destination_path + args.destination_filename, "w") as file:
    writer = csv.DictWriter(file, fieldnames=head)
    writer.writerows(output)


