# 4, 8 tests WA

from copy import deepcopy


class FragileDict:

    def __init__(self, d=None):
        self._data = d if d is not None else dict()
        self._lock = False

    def __getitem__(self, key):
        if key not in self._data:
            raise KeyError(key)
        return self._data[key] if self._lock else deepcopy(self._data[key])

    def __enter__(self):
        self._buff = deepcopy(self._data)
        self._lock = True
        return self

    def __setitem__(self, key, value):
        if not self._lock:
            raise RuntimeError('Protected state')
        self._data[key] = value

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock = False
        if exc_type is not None:
            self._data, self._buff = self._buff, self._data
            print('Exception has been suppressed.')
        else:
            self._data = deepcopy(self._data)
        del self._buff
        return True

    def __contains__(self, key):
        return key in self._data
