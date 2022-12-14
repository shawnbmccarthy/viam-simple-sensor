"""
simple sensor examples

Using the viam sdk to extend the viam server to support custom sensors
which the base server might not support
"""
from typing import Optional, Mapping, Any

from viam.components.sensor import Sensor


class StaticSensor(Sensor):
    """
    A simple static sensor that does nothing exciting
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)

    async def get_readings(
            self,
            *,
            extra: Optional[Mapping[str, Any]] = None,
            timeout: Optional[float] = None,
            **kwargs
    ) -> Mapping[str, Any]:
        """
        get readings will be called by clients & services which access the robot

        :param extra:
        :param timeout:
        :param kwargs:
        :return:
        """
        return {'static_msg': 'hello world'}


class IncrementSensor(Sensor):
    """
    A simple increment sensor which holds a count of how many times it was called
    """
    def __init__(self, name: str) -> None:
        self.n = 0
        super().__init__(name)

    async def get_readings(
            self,
            *,
            extra: Optional[Mapping[str, Any]] = None,
            timeout: Optional[float] = None,
            **kwargs
    ) -> Mapping[str, Any]:
        data = {'current_value': self.n}
        self.n += 1
        return data
