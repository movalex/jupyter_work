import heapq


def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
#     print('heap init:    ', heap)
    heapq.heapify(heap)

    while heap:
        val, list_index, element_index = heapq.heappop(heap)
#         print(heap)

        merged_list.append(val)

        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1],
                          list_index,
                          element_index + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list


if __name__ == '__main__':
#     print(merge([[4, 12, 35], [-12, 5, 11, 42], [1, 2, 63, 111]]))
    test_list = [[4, 12, 35], [-12, 5, 11, 42], [1, 2, 63, 111]]
    assert(merge(test_list) == [-12, 1, 2, 4, 5, 11, 12, 35, 42, 63, 111])
