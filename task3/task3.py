#! python3.7
import argparse
import json


default_report_file = "report.json"


def insert_values(tests_json_obj_values, values_to_insert: dict):
    for elem in tests_json_obj_values:
        if "value" in elem:
            elem["value"] = values_to_insert.get(elem["id"], "")
        if "values" in elem:
            elem["values"] = insert_values(elem["values"], values_to_insert)

    return tests_json_obj_values


def values_to_dict(values_json_obj) -> dict:
    values_dict = {}
    for elem in values_json_obj["values"]:
        values_dict[elem["id"]] = elem["value"]
    return values_dict


def run(file_tests: str, file_values: str, file_report: str = default_report_file):
    with open(file_tests, 'r') as ft:
        tests = json.load(ft)

    with open(file_values, 'r') as fv:
        values = json.load(fv)

    values = values_to_dict(values)
    report = insert_values(tests_json_obj_values=tests["tests"], values_to_insert=values)

    with open(file_report, 'w') as fr:
        json.dump({"tests": report}, fp=fr, indent=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='task3')
    parser.add_argument('tests', type=str, help='tests.json file')
    parser.add_argument('values', type=str, help='values.json file')
    parser.add_argument('--report', '-r', type=str, default=default_report_file, help='file to save a report json')
    args = parser.parse_args()

    run(file_tests=args.tests, file_values=args.values, file_report=args.report)