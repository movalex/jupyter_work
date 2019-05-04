import multiprocessing


def spawn(num):
    """simple multiprocessing example
    :returns: TODO

    """
    return f"spawned {num}!"


# if __name__ == "__main__":
#     for i in range(55):
#         p = multiprocessing.Process(target=spawn, args=(i,))
#         p.start()
#         p.join()  # spawn and wait till complete do not create many processes


if __name__ == "__main__":
    Pool = multiprocessing.Pool(processes=10)
    result = [Pool.apply(spawn, args=(111111,)) for _ in range(100100)]
    print(result)
