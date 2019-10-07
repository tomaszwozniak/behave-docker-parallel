#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys


def update_allure_feature_name(results_dir: str, prefix: str):
    """Make Allure JSON results unique by pre-pending a prefix to: name, historyId & uuid.

    Use it when not all of the test results show up in the Allure report.
    This is because tests from different workers can actually have the same: historyId & uuid values.

    You can use e.g. browser name as the prefix.
    """
    results_dir_path = os.path.join(".", results_dir)
    update_count = 0
    for filename in os.listdir(results_dir_path):
        if filename.endswith(".json"):
            result_file = os.path.join(results_dir_path, filename)
            with open(result_file, "r") as json_file:
                report = json.loads(json_file.read())
                report["name"] = f"{prefix} - {report['name']}"
                report["historyId"] = f"{prefix}{report['historyId']}"
                report["uuid"] = f"{prefix}{report['uuid']}"
            with open(result_file, "w") as json_file:
                json.dump(report, json_file, indent=2, ensure_ascii=False)
                update_count += 1
    print(f"Updated {update_count} JSON reports")


if __name__ == "__main__":
    update_allure_feature_name(results_dir=sys.argv[1], prefix=sys.argv[2])
