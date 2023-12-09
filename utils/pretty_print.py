from tabulate import tabulate


def pprint(day, challenges):
    print(
        tabulate(
            challenges,
            headers=[day, "Example", "Input", "Time (ms)"],
            tablefmt="fancy_grid",
        )
    )
