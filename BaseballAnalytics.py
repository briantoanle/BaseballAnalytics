YEAR = 0
LEAGUE = 1
TEAM = 2
GAMES_PLAYED = 3
GAMES_WON = 4
GAMES_LOST = 5
WON_WS = 6
RUNS = 7
AT_BAT = 8
HITS = 9
DOUBLES = 10
TRIPLES = 11
HOME_RUNS = 12
ATTENDANCE = 13
NON_INT_COLS = [LEAGUE, TEAM, WON_WS]


def question1_max_home_run(all_data):
    # print("just to test with con for now -- ")
    # print("home run of 1916 Boston is", all_data[0][HOME_RUNS])
    temp = 0
    line = 0
    print("1st time line is", type(line))
    for row in all_data:

        if row[HOME_RUNS] > temp:
            temp = row[HOME_RUNS]
            line = row
    print(line)
    print("2nd time line is", type(line))
    # print(line)
    # print(temp)

'''temp = 0
    count = 0
    for line, row in enumerate(all_data):
        # print(line, "and", row)
        if row[HOME_RUNS] > temp:
            temp = row[HOME_RUNS]
            count = line
            print("trigger at", all_data[count])
'''


    #print(count)
    # print(temp)
    # print(all_data[count])
    #data = all_data[count]
    #print("The team that has the most HR is", data[TEAM], "in year", data[YEAR], "with", data[HOME_RUNS], "home runs")


def main():

    all_data = []
    with open('Teams.csv', 'r') as fh:
        headers = fh.readline()

        for line in fh:
            # print(line)
            data = line.strip().split(',')
            # print("here", data)
            for i in range(len(data)):
                if i not in NON_INT_COLS:
                    data[i] = int(data[i])
                elif i == WON_WS:
                    data[i] = (data[i] == 'Y')

            # print(data)
            all_data.append(data)

    # print(all_data)
    # for row in all_data:
    #    print(row)

    question1_max_home_run(all_data)

main()