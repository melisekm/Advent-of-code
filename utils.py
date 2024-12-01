import math
import timeit


def aoc_part(name, out=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = timeit.default_timer()
            result = func(*args, **kwargs)
            elapsed_time = timeit.default_timer() - start_time
            if out:
                print(result)
            print(f"Time for{' part' if isinstance(name, int) else ''} {name}: {_format_time(elapsed_time)}")
            return result

        return wrapper

    return decorator


# https://github.com/ipython/ipython/blob/main/IPython/core/magics/execution.py
def _format_time(timespan, precision=3):
    """Formats the timespan in a human readable form"""

    if timespan >= 60.0:
        parts = [("d", 60 * 60 * 24), ("h", 60 * 60), ("min", 60), ("s", 1)]
        time = []
        leftover = timespan
        for suffix, length in parts:
            value = int(leftover / length)
            if value > 0:
                leftover = leftover % length
                time.append(u'%s%s' % (str(value), suffix))
            if leftover < 1:
                break
        return " ".join(time)

    units = [u"s", u"ms", u'\xb5s', "ns"]
    scaling = [1, 1e3, 1e6, 1e9]

    if timespan > 0.0:
        order = min(-int(math.floor(math.log10(timespan)) // 3), 3)
    else:
        order = 3
    return "%.*g %s" % (precision, timespan * scaling[order], units[order])


def _linspace(start, stop, num, endpoint=True):
    num = int(num)
    start *= 1.
    stop *= 1.

    if num == 1:
        yield stop
        return
    if endpoint:
        step = (stop - start) / (num - 1)
    else:
        step = (stop - start) / num

    for i in range(num):
        yield start + step * i


def linspace(start, stop, num, endpoint=True, integer=True):
    if integer:
        return list(map(int, _linspace(start, stop, num, endpoint)))
    else:
        return list(_linspace(start, stop, num, endpoint))


def generic_parallel_execution(func, data, *fn_args, workers=4, executor="process", add_pbar=False, **fn_kwargs):
    from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

    if executor == "process":
        executor_type = ProcessPoolExecutor
    elif executor == "thread":
        executor_type = ThreadPoolExecutor
    else:
        raise Exception(f"Executor {executor} not supported")
    space = linspace(0, len(data), workers + 1)
    with executor_type(max_workers=workers) as executor:
        futures = set()
        for i in range(workers):
            if add_pbar:
                fn_kwargs["pbar_position"] = i
            future = executor.submit(func, data[space[i]: space[i + 1]], *fn_args, **fn_kwargs)
            print(f"Starting worker {future}")
            futures.add(future)

    results = []
    for future in as_completed(futures):
        try:
            results.append(future.result())
        except Exception as e:
            print(f"{future} generated an exception: {e}")
        else:
            print(f"Joining worker {future}")
    return results


def timer(func):
    def wrapper(*args, **kwargs):
        print(f"Starting '{func.__qualname__}'...")
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print(f"Task: '{func.__qualname__}' done. Runtime: {end_time - start_time:.2f}s")
        return result

    return wrapper
