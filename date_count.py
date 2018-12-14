#_*_coding:utf-8_*_
__author__ = 'Chrislee'

class Date_count():
    def __init__(self):
        self.date=input()
        self.month=int(self.date[4:6])
        self.day =int(self.date[6:])
        self.part_one = 31
        self.month_dict={
                3:self.March(),
                4:self.April(),
                5:self.May(),
                6:self.June(),
                7:self.July(),
                8:self.August(),
                9:self.September(),
                10:self.October(),
                11:self.November(),
                12:self.December()
        }

    def March(self):
        return 0

    def April(self):
        return 90 - 59

    def May(self):
        return 120 - 59

    def June(self):
        return 151 - 59

    def July(self):
        return 181 - 59

    def August(self):
        return 212 - 59

    def September(self):
        return 243 - 59

    def October(self):
        return 273 - 59

    def November(self):
        return 304 - 59

    def December(self):
        return 334 - 59

    def date_count(self):
        date=self.date
        month=self.month
        day =self.day
        part_one = 31
        if month <= 2:
            part_one= 31
            result = part_one + day
        else:
            part_one = 59
            part_two= self.month_dict.get(month)
            result = part_one+part_two+day
        print(result)

if __name__=="__main__":
    Day=Date_count()
    Day.date_count()
