from collections import defaultdict


def get_min_time(task_memory, task_type, max_memory):
    n = len(task_memory)
    tasks_by_type = defaultdict(list)  # group tasks by their type

    for index in range(n):
        tasks_by_type[task_type[index]].append(task_memory[index])

    # since we can only run parallely for same tasks. figure out the max time for each type of tasks
    min_time = 0
    for type_ in tasks_by_type:
        memories = tasks_by_type[type_]
        memories.sort()

        left, right = 0, len(memories) - 1
        while left < right:
            # pair the larger task with the shorter task under memory limit
            if memories[left] + memories[right] <= max_memory:
                left += 1

            min_time += 1
            right -= 1

        if left == right:
            min_time += 1

    return min_time


if __name__ == "__main__":
    task_memory = [1, 2, 3, 4, 2]
    task_type = [1, 2, 1, 2, 3]
    max_memory = 4
    print(get_min_time(task_memory, task_type, max_memory))

    task_memory = [1, 2, 5]
    task_type = [1, 2, 3]
    max_memory = 6
    print(get_min_time(task_memory, task_type, max_memory))

    task_memory = [7, 2, 3, 9]
    task_type = [1, 2, 1, 3]
    max_memory = 10
    print(get_min_time(task_memory, task_type, max_memory))
