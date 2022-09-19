# Ex 9.2 - backpack problem
backpack_max_weight = int(input())

items_number = int(input())
items = dict()
items_list = list()
for i in range(items_number):
    item, weight, cost = input().split()
    weight, cost = int(weight), int(cost)
    items[item] = dict()
    items[item]["cost"] = cost
    items[item]["weight"] = weight
    items_list.append(item)

# create two 2d arrays - for maximal cost and for solution description in words
solution = [[0] * (backpack_max_weight + 1) for i in range(items_number)]
solution_in_words = [[""] * (backpack_max_weight + 1) for i in range(items_number)]

# each item
for i in range(items_number):
    current_item = items_list[i]
    current_cost = items[current_item]["cost"]
    current_weight = items[current_item]["weight"]
    # each possible weight: from 0 to max weight
    for j in range(backpack_max_weight):
        # first item
        if i == 0:
            if current_weight <= j + 1:
                solution[i][j + 1] = current_cost
                solution_in_words[i][j + 1] = current_item
        else:
            # last maximum
            last_max = solution[i - 1][j + 1]
            # cost of current item and cost of lasting space
            current_and_space = solution[i - 1][max(0, j + 1 - current_weight)] + current_cost
            if last_max > current_and_space:
                solution[i][j + 1] = last_max
                solution_in_words[i][j + 1] = solution_in_words[i - 1][j + 1]
            else:
                solution[i][j + 1] = current_and_space
                if solution_in_words[i - 1][j + 1 - current_weight] != "":
                    solution_in_words[i][j + 1] = solution_in_words[i - 1][j + 1 - current_weight] + " + "
                solution_in_words[i][j + 1] += current_item


print(solution[items_number - 1][backpack_max_weight])
print(solution_in_words[items_number - 1][backpack_max_weight])
