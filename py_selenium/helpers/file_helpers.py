import os
import time


def compare_files(actual_file, expected_file):
    files_same = True
    with open(expected_file) as f1, open(actual_file) as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                files_same = False
                break
    return files_same


def compare_files_lines(actual_file, expected_file):
    files_same = True
    num_lines1 = sum(1 for line in open(expected_file))
    num_lines2 = sum(1 for line in open(actual_file))

    if num_lines1 != num_lines2:
        print("Expected file contains lines :" + str(num_lines1))
        print("Actual file contains lines: " + str(num_lines2))
        files_same = False
    return files_same


def compare_attributes(actual_file, expected_file, list):
    files_same = True
    time.sleep(2)
    with open(expected_file) as f1, open(actual_file) as f2:
        for line1, line2 in zip(f1, f2):
            attr1 = line1.split(',')
            attr2 = line2.split(',')
            for i in range(len(attr1)):
                current = attr1[i]
                if compare_numbers(current, attr2[i]) == False and i in list:
                    print("Expected- unmatched attribute:" + current)
                    print("Actual - unmatched attribute:" + attr2[i])
                    files_same = False
    return files_same


def wait_until_file_exists(actual_file, wait_time_in_seconds=20):
    waits = 0
    while not os.path.isfile(actual_file) and waits < wait_time_in_seconds:
        print("sleeping...." + str(waits))
        time.sleep(.5)  # make sure file completes downloading
        waits += .5


def is_number(s):
    try:

        float(s)
        return True
    except ValueError:
        return False


def compare_numbers(exp, act):
    exp = exp.replace('"', '')
    act = act.replace('"', '')
    if is_number(exp) == False and is_number(act) == False and exp != act:
        return False

    if is_number(exp) == True and is_number(act) == True and round(float(exp), 2) != round(float(act), 2):
        return False

    return True
