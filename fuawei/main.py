from fuawei.fuawei_with_interfaces import Fuawei
from fuawei.tech_provider_factory import TechProviderFactory

# from fuawei.fuawei_without_interfaces import Fuawei

if __name__ == '__main__':
    provider = TechProviderFactory.get_tech_provider()

    fuawei = Fuawei(provider)

    # fuawei = Fuawei()
    phone = fuawei.create_phone()

    print(phone)
