import requests
from requests import RequestException

from fuawei.entities.fuawei_chip import FuaweiChip
from fuawei.entities.phone import Phone


class Fuawei:

    def create_phone(self) -> Phone:
        try:
            fansung_chip_data = requests.get('http://fuawei-chips/web-service').json()
        except RequestException:
            fansung_chip_data = {}
        fansung_specification_parsed = self.parse_fansung_specification(fansung_chip_data)
        return Phone(self.create_fuawei_chip(fansung_specification_parsed))

    def parse_fansung_specification(self, data):
        # Many lines to parse from fansum format to any more friendly format
        return {}

    def create_fuawei_chip(self, data) -> FuaweiChip:
        # Many lines to build from our friendly format to FuaweiChip
        return FuaweiChip()
