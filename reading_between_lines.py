# ファイル内の文書のn-m行目の内容を表示する

import sys
file_name = sys.argv[1]
line_start = sys.argv[2]
line_goal = sys.argv[3]

line_start_num = int(line_start) - 1
line_goal_num = int(line_goal) + 1


def file_reading(fp):
    for mail in fp:
        mail_str = mail.rstrip()
        lines.append(mail_str)


def main():
    with open(file_name, 'r') as fp:
        lines = []
        file_reading(fp)
        last_num = len(lines)
        if ((line_start_num <= line_goal_num)and(line_goal_num<last_num)):
            print(lines[line_start_num:line_goal_num])
        elif ((line_start_num > line_goal_num)and(line_goal_num<last_num)):
            print(lines[line_goal_num:])
            print(lines[:line_start_num])
        else:
            print("error!")
            
            
if __name__ == '__main__':
    main()
