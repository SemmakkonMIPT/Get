def max_meetings(n, start, end):
    meetings = [(start[i], end[i], i) for i in range(n)]
    meetings.sort(key=lambda x: x[1])

    last_end = meetings[0][1]
    selected_meetings = [meetings[0][2]]

    for i in range(1, n):
        if meetings[i][0] > last_end:
            selected_meetings.append(meetings[i][2])
            last_end = meetings[i][1]

    return len(selected_meetings)


if __name__ == '__main__':
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(max_meetings(n, start, end))

'''
6
1.txt 3 0 5 8 5
2 4 6 7 9 9
'''