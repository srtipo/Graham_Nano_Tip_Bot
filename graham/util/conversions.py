class BananoConversions():
    # 1 BANANO = 10e29 RAW
    RAW_PER_BAN=100000000000000000000000000000

    @classmethod
    def raw_to_banano(self, raw_amt):
        return raw_amt / self.RAW_PER_BAN

    @staticmethod
    def banano_to_raw(ban_amt):
        expanded = float(ban_amt) * 100
        return int(expanded) * (10**27)

class NanoConversions():
    # 1 RAI = 10e24 RAW
    RAW_PER_RAI=1000000000000000000000000

    @classmethod
    def raw_to_rai(self, raw_amt):
        return raw_amt / self.RAW_PER_RAI

    @staticmethod
    def rai_to_raw(rai_amt):
        expanded = float(rai_amt) * 100
        return int(expanded) * (10**22)