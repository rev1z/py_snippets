import functools

class RetryException(Exception):
    pass

def retry_decorator(f=None, *, retries=5):
    if f is None:
        return functools.partial(retry_decorator,
                                 retries=retries)

    @functools.wraps(f)
    def inner(*args, **kwargs):
        call = ",".join([str(s) for s in args] + [f'{k}={v}' for k, v in kwargs])
        exception = None
        tries = retries+1
        for i in range(retries+1):
            tries -= 1
            try:
                ret = f(*args, **kwargs)
                return ret
            except Exception as e:
                exception = e
                print(f"somthig wrong: \n {e.__class__.__name__}: {e}\n {tries} tries last")

        if exception:
            sleep(0.1)
            msg = f"Unnable to re-run function {f.__name__}({call}). \n last exception:\n{exception.__class__.__name__}:{exception}"
            raise RetryException(msg)

    return inner




@retry_decorator(retries=10)
def er(a=0):
    if a < 4:
        raise RuntimeError("POOF! TRACEBACK")
    return True


er()
