
numbers = {}
cd = []
paths = []

with open("data.txt", "r") as file:
    for line in file:
        data = line.strip().split(" ")

        if data[1] == "cd":
            if data[2] == "..":
                del cd[-1]
            else:
                cd.append(data[2])
            path = "_".join(cd)
            if path not in numbers.keys():
                numbers[path] = 0
                paths.append(path)

        if data[0].isnumeric():
            numbers[path] += int(data[0])

    paths.sort(key=len)
    paths.reverse()

    for el in paths:
        add_to = el
        if len(el) != 1:
            el = el.split("_")
            el = el[:-1]
            to_add = "_".join(el)
            numbers[to_add] += int(numbers[add_to])

    total = sum([value for value in numbers.values() if value <= 100000])

    space_required = 30000000 - (70000000 - numbers["/"])

    l = []
    for el in numbers.values():
        if space_required - el < 0:
            l.append(el)

    ans = min(l)

    print(ans)
