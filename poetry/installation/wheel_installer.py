from typing import BinaryIO
from typing import Optional

from poetry.utils.env import Env

from .wheel.installer import Decision
from .wheel.installer import Installer
from .wheel.installer import SchemeDecisionHandler
from .wheel.record import Record
from .wheel.wheel import Wheel


class DecisionHandler(SchemeDecisionHandler):
    def __init__(self, env: Env) -> None:
        self._env = env

    def handle_decision(self, decision: Decision, io: BinaryIO) -> Optional[Record]:
        scheme = decision.scheme
        destination = self._env.paths[scheme.value]
        print(decision.path, destination)

        return


class WheelInstaller:
    def __init__(self, env: Env) -> None:
        self._env = env
        self._installer = Installer("poetry")
        self._decision_handler = DecisionHandler(self._env)

    def install(self, wheel: Wheel) -> None:
        self._installer.install(wheel, self._decision_handler)
