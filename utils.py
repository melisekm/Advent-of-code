import timeit


def aoc_part(part_idx):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = timeit.default_timer()
            result = func(*args, **kwargs)
            elapsed_time = timeit.default_timer() - start_time
            print(result)
            print(f"Total time pt{part_idx}: {elapsed_time:.3f} sec")
            return result

        return wrapper

    return decorator
