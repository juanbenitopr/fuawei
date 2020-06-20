import grpc

from fuawei.entities.fuawei_chip import FuaweiChip
from fuawei.tech_provider import TechProvider


class FuaweiTechProvider(TechProvider):

    def ask_chip(self) -> FuaweiChip:
        try:
            fuawei_service = grpc.insecure_channel('fuawei/web-service')
        except Exception:
            pass
        # Communication to the gRPC service of the Fuawei Provider
        return FuaweiChip()

