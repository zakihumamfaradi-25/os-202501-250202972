def fifo(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]

    return waiting_time, turnaround_time


if __name__ == "__main__":
    processes = [
        ("P1", 5),
        ("P2", 3),
        ("P3", 8),
    ]

    wt, tat = fifo(processes)

    for i in range(len(processes)):
        print(processes[i][0], "WT =", wt[i], "TAT =", tat[i])

