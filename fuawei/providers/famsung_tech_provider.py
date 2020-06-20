import requests

from fuawei.entities.fuawei_chip import FuaweiChip
from fuawei.tech_provider import TechProvider


class FamsungTechProvider(TechProvider):

    def ask_chip(self) -> FuaweiChip:
        return self._build_fuawei_chip(requests.get('http://fuawei-chips/web-service').json())

    def _build_fuawei_chip(self, data) -> FuaweiChip:
        # On these lines you would have a lot of parse work in order to extract all the necessary information to
        # build your fuawei chip

        return FuaweiChip()
