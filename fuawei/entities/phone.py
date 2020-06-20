from fuawei.entities.fuawei_chip import FuaweiChip


class Phone:

    def __init__(self, chip: FuaweiChip):
        if not isinstance(chip, FuaweiChip):
            raise Exception('I cannot work without a properly fuawei chip')
        self.chip = chip

    def __str__(self):
        return 'Hi, I am fuawei phone!'
