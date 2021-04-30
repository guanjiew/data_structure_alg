class Interval:
    def __init__(self, start, finish, weight=1):
        assert finish > start
        self.start = start
        self.finish = finish
        self.weight = weight

    def __str__(self):
        return "[{},{}]({})".format(self.start, self.finish, self.weight)


# Given an sorted array of the finishing time and a query start time.
# Return the index of the largest finishing time in the array that is no larger than the start time
# Return -1 if there is no such finishing time in the list
def bst_search_prev_lrgst_compat_idx(sorted_finish_time_lst, query_start_time):
    if len(sorted_finish_time_lst) == 0:
        return -1
    if sorted_finish_time_lst[0] > query_start_time:
        return -1
    left, right = 0, len(sorted_finish_time_lst) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_time = sorted_finish_time_lst[mid]
        if mid_time > query_start_time:
            right = mid - 1
        if mid_time <= query_start_time:
            if mid + 1 <= right and sorted_finish_time_lst[mid + 1] <= query_start_time:
                left = mid + 1
            else:
                return left
    return left


def comp_prev_lrgst_compat_intval_idx(sorted_interval):
    prev_compat_idx = []
    for i in range(len(sorted_interval)):
        prev_intval_finish_lst = [interval.finish for interval in interval_lst[:i]]
        query_interval_start_time = sorted_interval[i].start
        prev_compat_idx.append(bst_search_prev_lrgst_compat_idx(prev_intval_finish_lst, query_interval_start_time))
    return prev_compat_idx


def bottom_up_dp_update_opt_idx_weight(intervals, compat_idx_lst, opt_weight_map,
                                       compat_idx_map):
    num_intervals = len(intervals)
    for i in range(num_intervals):
        prev_opt_weight = opt_weight_map[i - 1]
        prev_compat_opt_weight = opt_weight_map[compat_idx_lst[i]]
        cur_intval_weight = intervals[i].weight
        cur_opt_weight = max(prev_opt_weight, prev_compat_opt_weight + cur_intval_weight)
        opt_weight_map[i] = cur_opt_weight
        if prev_opt_weight == cur_opt_weight:
            compat_idx_map[i] = compat_idx_map[i - 1]
        else:
            compat_idx_map[i] = compat_idx_map[compat_idx_lst[i]]
            compat_idx_map[i].append(intervals[i])


def print_opt_intervals(intervals, compat_idx_lst, opt_weight_map, compat_idx_map):
    print("========================================")
    print("Input Interval Lists:")
    print("========================================")
    for interval in intervals:
        print(interval)
    print("========================================")
    print("Solution Breakdown:")
    print("========================================")
    print("Largest previous compatible index list: ", compat_idx_lst)
    print("Optimal Interval Scheduling:")
    num_intervals = len(intervals)
    for interval in compat_idx_map[num_intervals - 1]:
        print(interval)
    print("Index Optimal weight map: ", opt_weight_map)
    print("Optimal weights: ", opt_weight_map[num_intervals - 1])


def compute_opt_weighted_interval_schedule(intervals, debug_mode):
    intervals_sorted_by_finish = sorted(intervals, key=lambda each_interval: each_interval.finish)
    prev_compat_idx = comp_prev_lrgst_compat_intval_idx(intervals_sorted_by_finish)
    idx_to_opt_weight_map = {-1: 0}
    cur_idx_to_prev_compat_idx_map = {-1: []}
    bottom_up_dp_update_opt_idx_weight(intervals_sorted_by_finish, prev_compat_idx, idx_to_opt_weight_map,
                                       cur_idx_to_prev_compat_idx_map)
    if debug_mode:
        print_opt_intervals(intervals_sorted_by_finish, prev_compat_idx, idx_to_opt_weight_map,
                            cur_idx_to_prev_compat_idx_map)
    return idx_to_opt_weight_map[len(intervals) - 1]


if __name__ == '__main__':
    interval_lst = [Interval(start=0, finish=5, weight=2),
                    Interval(start=7, finish=9, weight=9),
                    Interval(start=4, finish=8, weight=12),
                    Interval(start=1, finish=6, weight=11),
                    Interval(start=7, finish=9, weight=3),
                    Interval(start=10, finish=11, weight=9)]
    compute_opt_weighted_interval_schedule(interval_lst, debug_mode=True)
