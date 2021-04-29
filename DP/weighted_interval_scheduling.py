class Interval:
    def __init__(self, start, finish, weight=1):
        assert finish > start
        self.start = start
        self.finish = finish
        self.weight = weight

    def __str__(self):
        return "[{},{}]({})".format(self.start, self.finish, self.weight)


# Given an sorted array of the finishing time and start time.
# Return the index of the largest finishing time in the array that is no larger than the start time
# Return -1 if there is no such finish time
def _largest_comp_interval(time_lst, start_time):
    if len(time_lst) == 0:
        return -1
    if time_lst[0] > start_time:
        return -1
    left, right = 0, len(time_lst) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_time = time_lst[mid]
        if mid_time > start_time:
            right = mid - 1
        if mid_time <= start_time:
            if mid + 1 <= right and time_lst[mid + 1] <= start_time:
                left = mid + 1
            else:
                return left
    return left


def largest_comp_interval(sorted_interval):
    p = []
    for i in range(len(sorted_interval)):
        prev_finish_lst = [interval.finish for interval in interval_lst[:i]]
        query_start = sorted_interval[i].start
        p.append(_largest_comp_interval(prev_finish_lst, query_start))
    return p


def bottom_up(intervals):
    n = len(intervals)
    sorted_interval = sorted(intervals, key=lambda interval: interval.finish)
    print("Interval Lists:")
    for interval in sorted_interval:
        print(interval)
    p = largest_comp_interval(sorted_interval)
    opt = {-1: 0}
    interval_set = {-1: []}
    for i in range(n):
        opt[i] = max(opt[i - 1], opt[p[i]] + sorted_interval[i].weight)
        if opt[i] == opt[i - 1]:
            interval_set[i] = interval_set[i - 1]
        else:
            interval_set[i] = interval_set[p[i]]
            interval_set[i].append(intervals[i])
    print("========================================")
    print("Previous compatible list", p)
    print("Interval Schedules:")
    for interval in interval_set[n - 1]:
        print(interval)
    print("OPT Table: ", opt)
    return opt[n - 1]


if __name__ == '__main__':
    interval_lst = [Interval(0, 5, 2), Interval(7, 9, 9), Interval(4, 8, 12), Interval(1, 6, 11), Interval(7, 9, 3),
                    Interval(10, 11, 9)]
    print(bottom_up(interval_lst))
