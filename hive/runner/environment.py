from __future__ import annotations

from typing import NamedTuple, TYPE_CHECKING, FrozenSet

from hive.reporting.reporter import Reporter

import immutables

if TYPE_CHECKING:
    from hive.model.energy.charger import Charger
    from hive.model.vehicle.mechatronics.mechatronics_interface import MechatronicsInterface
    from hive.config import HiveConfig
    from hive.util.typealiases import ChargerId, MechatronicsId, MembershipId, MembershipMap, ScheduleFunction, \
        ScheduleId


class Environment(NamedTuple):
    """
    Environment of this Hive Simulation.

    """
    config: HiveConfig
    mechatronics: immutables.Map[MechatronicsId, MechatronicsInterface] = immutables.Map()
    chargers: immutables.Map[ChargerId, Charger] = immutables.Map()
    schedules: immutables.Map[ScheduleId, ScheduleFunction] = immutables.Map()
    fleet_ids: FrozenSet[MembershipId] = frozenset()
    vehicle_membership_map: MembershipMap = None

    reporter: Reporter = Reporter()

    def set_reporter(self, reporter: Reporter) -> Environment:
        """
        allows the reporter to be updated after the environment is built.

        :param reporter: the reporter to be used

        :return: the updated environment
        """
        return self._replace(reporter=reporter)

    def set_vehicle_membership_map(self, membership_map: MembershipMap):
        """
        allows the vehicle membership map to be updated after the environment is built.

        :param membership_map: the membership map to be used

        :return: the updated environment
        """
        return self._replace(vehicle_membership_map=membership_map)
