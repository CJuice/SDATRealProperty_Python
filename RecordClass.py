class RecordClass():
    def __init__(self, presplit_record):
        self.county_code_digit = presplit_record[0]
        self.district = presplit_record[1]
        self.account_number = presplit_record[2]
        self.county_code_4character = ""
        self.town_code = 0
        self.finder_url = ""
        self.google_url = r""
        self.latitude = 0.0
        self.longitude = 0.0
        self.jurscode = ""
        self.account_id_from_SDAT_concat_no_leading_zeros = ""
        self.resityp = ""
        self.address = ""
        self.strtunt = ""
        self.addrtyp = ""
        self.city = ""
        self.zipcode = ""
        self.legal_1 = ""
        self.sdat_web_adr = r""
        self.existing = ""

    @property
    def account_id_from_SDAT_concat_no_leading_zeros(self):
        return self.__account_id
    @account_id_from_SDAT_concat_no_leading_zeros.setter
    def account_id_from_SDAT_concat_no_leading_zeros(self, val):
        concatenated_values = "{}{}{}".format(self.county_code_digit, self.district, self.account_number)
        if self.county_code_digit.startswith('0'):
            self.__account_id = concatenated_values[1:]
        else:
            self.__account_id = concatenated_values
