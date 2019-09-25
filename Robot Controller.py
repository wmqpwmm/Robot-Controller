import sys, io, helper
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8-sig')
env_data = helper.fetch_maze()

# 任务1在如下代码中，请写代码获得:模拟环境的长和宽,模拟环境中第3行第6列元素
# 1模拟环境的行数
rows = len(helper.MAZE)
# 2模拟环境的列数
columns = len(helper.MAZE[0])
# 3取出模拟环境第三行第六列的元素
row_3_col_6 = helper.MAZE[2][5]
print("迷宫共有", rows, "行", columns, "列，第三行第六列的元素是", row_3_col_6)

# 任务2在如下代码中，请计算模拟环境中，第一行和第三列的障碍物个数
# 4计算模拟环境中，第一行的的障碍物个数。
number_of_barriers_row1 = helper.MAZE[0].count(2)
# 5计算模拟环境中，第三列的的障碍物个数。
number_of_barriers_col3 = 0
for i in range(len(helper.MAZE)):
    if helper.MAZE[i][2] == 2:
        number_of_barriers_col3 += 1
print("迷宫中，第一行共有", number_of_barriers_row1, "个障碍物，第三列共有", number_of_barriers_col3, "个障碍物。")

%run -i -e test.py RobotControllortTestCase.test_cal_barriers
