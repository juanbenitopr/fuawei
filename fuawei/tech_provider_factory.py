from fuawei.providers.fuawei_tech_factory import FuaweiTechProvider
from fuawei.tech_provider import TechProvider


class TechProviderFactory:

    @staticmethod
    def get_tech_provider() -> TechProvider:
        return FuaweiTechProvider()
