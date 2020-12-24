from datetime import datetime
import os


def is_num(st):
    if st.find(".") != -1 and st.count(".") == 1 and st.find(".") != len(st) - 1:
        st1 = st.replace(".", "1")
        if st1.isdigit():
            return True
    if st.isdigit():
        return True
    return False


def calculate(exp):
    ops = ["+", "-", "*", "/", "add", "sub", "mul", "div"]
    stack_for_num = []
    for item in exp[:: -1]:
        if is_num(item):
            stack_for_num.append(float(item))
        elif item in ops:
            num1 = stack_for_num.pop()
            num2 = stack_for_num.pop()
            if item == "+" or item == "add":
                stack_for_num.append(num1 + num2)
            elif item == "-" or item == "sub":
                stack_for_num.append(num1 - num2)
            elif item == "*" or item == "mul":
                stack_for_num.append(num1 * num2)
            elif item == "/" or item == "div":
                stack_for_num.append(num1 / num2)
        else:
            return "Invalid expression"
    return stack_for_num.pop()


def rep_run():
    exp_ans = input("Please, input your expression: ")
    exp = exp_ans.split(" ")
    result = calculate(exp)
    report_dir = {"Datetime": datetime.now(), "Input parameters": exp_ans}
    if result == "Invalid expression":
        report_dir["ERROR"] = "Invalid Expression"
    else:
        report_dir["Result"] = result
    abs_path = os.getcwd()
    with open(os.path.join(abs_path, "logs", "logging.txt"), "w") as report:
        for keys, values in report_dir.items():
            report.write(f'{keys}: {values} \n')
    with open(os.path.join(abs_path, "logs", "logging.txt"), "r+") as report:
        context = report.read()
        report.write(f'Report: Info - {context.count("Input parameters")} Error - {context.count("ERROR")}')


rep_run()

