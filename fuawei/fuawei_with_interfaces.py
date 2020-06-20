from fuawei.entities.phone import Phone
from fuawei.tech_provider import TechProvider


class Fuawei:

    def __init__(self, provider: TechProvider):
        self.provider = provider

    def create_phone(self) -> Phone:
        chip = self.provider.ask_chip()
        return Phone(chip=chip)
