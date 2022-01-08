

from typing_extensions import final


class talentS:
    def __init__(self, dict: dict) -> None:
        self.__dataDict = dict
        self.__staticLevelAddValue = 192  # Not changing
        self.__staticSomeAddValue = 205  # Not changing
        self.level: int = int(dict['level'])
        self.potential: int = int(dict['potential'])
        self.baseStrength: int = int(dict['baseStrength'])
        self.spiritPercent: float = float(dict['spiritPercent'])
        self.wiseLevel: int = int(dict['wiseLevel'])
        self.auraPercent: int = int(dict['auraPercent'])
        self.teaStrength: int = int(dict['teaStrength'])
        self.itemStrength: int = int(dict['itemStrength'])
        self.soulmatesStrength: str = dict['soulmatesStrength']
        self.soulmatesPercent: str = dict['soulmatesPercent']

    def calculateStrength(self) -> int:
        try:
            a = int(self.level / 50)
            b = a - 1
            c = self.__staticSomeAddValue + 30 * b
            soulmatesPercentSum = 0
            for val in self.soulmatesPercent.replace(' ', '').split(','):
                soulmatesPercentSum += float(val)
            soulmatesStrengthSum = 0
            for val in self.soulmatesStrength.replace(' ', '').split(','):
                soulmatesStrengthSum += int(val)
            e1 = self.spiritPercent + \
                (self.wiseLevel * 10) + self.auraPercent + soulmatesPercentSum
            e2 = soulmatesStrengthSum
            tea = self.teaStrength
            item = self.itemStrength

            finalStrength = self.potential * \
                (192 + a * c) * (1 + e1/100) + tea + \
                e2 + item + self.wiseLevel * 250000

            print(finalStrength)
            return finalStrength
        except ValueError:
            print(ValueError)
            return -1
