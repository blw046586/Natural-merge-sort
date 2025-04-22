class NaturalMergeSorter:
    def get_sorted_run_length(self, lst, start_index):
        if start_index >= len(lst):
            return 0

        run_length = 1
        for i in range(start_index + 1, len(lst)):
            if lst[i] >= lst[i - 1]:
                run_length += 1
            else:
                break
        return run_length

    def merge(self, lst, left_start, left_end, right_end):
        merged = []
        i = left_start
        j = left_end + 1

        while i <= left_end and j <= right_end:
            if lst[i] <= lst[j]:
                merged.append(lst[i])
                i += 1
            else:
                merged.append(lst[j])
                j += 1

        while i <= left_end:
            merged.append(lst[i])
            i += 1

        while j <= right_end:
            merged.append(lst[j])
            j += 1

        for idx, val in enumerate(merged):
            lst[left_start + idx] = val

    def natural_merge_sort(self, lst):
        while True:
            i = 0
            merged = False

            while i < len(lst):
                left_start = i
                left_len = self.get_sorted_run_length(lst, left_start)
                if left_len == len(lst):
                    return

                right_start = left_start + left_len
                if right_start >= len(lst):
                    break

                right_len = self.get_sorted_run_length(lst, right_start)
                self.merge(lst, left_start, right_start - 1, right_start + right_len - 1)

                i = right_start + right_len
                merged = True

            if not merged:
                break
