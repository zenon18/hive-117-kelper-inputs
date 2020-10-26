from __future__ import annotations

from datetime import datetime
from typing import Union


class SimTime(int):
    ERROR_MSG = "Unable to parse datetime. Make sure the time is an ISO 8601 string or an epoch integer"

    @classmethod
    def build(cls, value: Union[str, int]) -> Union[IOError, SimTime]:
        if isinstance(value, str):
            try:
                time = datetime.fromisoformat(value)
            except (ValueError, TypeError):
                try:
                    time = datetime.utcfromtimestamp(int(value))
                except (ValueError, TypeError):
                    return IOError(cls.ERROR_MSG)
        elif isinstance(value, int):
            try:
                time = datetime.utcfromtimestamp(value)
            except (ValueError, TypeError):
                return IOError(cls.ERROR_MSG)
        else:
            return IOError(cls.ERROR_MSG)

        if time.tzinfo:
            time = time.replace(tzinfo=None)

        utc_time = (time - datetime(1970, 1, 1)).total_seconds()

        return SimTime(int(utc_time))

    def __new__(cls, value, *args, **kwargs):
        return super(cls, cls).__new__(cls, value)

    def __add__(self, other):
        res = super(SimTime, self).__add__(other)
        return self.__class__(res)

    def __sub__(self, other):
        res = super(SimTime, self).__sub__(other)
        return self.__class__(res)

    def __mul__(self, other):
        res = super(SimTime, self).__mul__(other)
        return self.__class__(res)

    def __repr__(self):
        return datetime.utcfromtimestamp(int(self)).isoformat()

    def __str__(self):
        return datetime.utcfromtimestamp(int(self)).isoformat()

    def as_datetime_time(self) -> datetime.time:
        return datetime.utcfromtimestamp(int(self)).time()
