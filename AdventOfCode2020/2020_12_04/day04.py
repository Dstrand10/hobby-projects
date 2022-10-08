import re

class Passport:
    def __init__(self):
        self.byr = None  # (Birth Year)
        self.iyr = None  # (Issue Year)
        self.eyr = None  # (Expiration Year)
        self.hgt = None  # (Height)
        self.hcl = None  # (Hair Color)
        self.ecl = None  # (Eye Color)
        self.pid = None  # (Passport ID)
        self.cid = None  # (Country ID)

    def set_val(self, field, val):
        if field == "byr":
            self.byr = val
        elif field == "iyr":
            self.iyr = val
        elif field == "eyr":
            self.eyr = val
        elif field == "hgt":
            self.hgt = val
        elif field == "hcl":
            self.hcl = val
        elif field == "ecl":
            self.ecl = val
        elif field == "pid":
            self.pid = val
        elif field == "cid":
            self.cid = val

    def valid(self):
        return self.byr_valid() and self.iyr_valid() and self.eyr_valid() and self.hgt_valid() and self.hcl_valid() \
               and self.ecl_valid() and self.pid_valid() and self.cid_valid()

    def byr_valid(self):
        return self.byr is not None and len(self.byr) == 4 and 1920 <= int(self.byr) <= 2002

    def iyr_valid(self):
        return self.iyr is not None and len(self.iyr) == 4 and 2010 <= int(self.iyr) <= 2020

    def eyr_valid(self):
        return self.eyr is not None and len(self.eyr) == 4 and 2020 <= int(self.eyr) <= 2030

    def hgt_valid(self):
        tmp_hgt_valid = False
        if self.hgt is not None and "cm" in self.hgt:
            nbr_hgt, _ = str(self.hgt).split("cm")
            if 150 <= int(nbr_hgt) <= 193:
                tmp_hgt_valid = True
        elif self.hgt is not None and "in" in self.hgt:
            nbr_hgt, _ = str(self.hgt).split("in")
            if 59 <= int(nbr_hgt) <= 76:
                tmp_hgt_valid = True
        return self.hgt is not None and tmp_hgt_valid

    def hcl_valid(self):
        tmp_hcl_valid = False
        if self.hcl is not None and "#" in self.hcl:
            _, hcl_color_code = str(self.hcl).split("#")
            search = re.compile(r'[^a-f0-9.]').search
            if len(hcl_color_code) == 6 and not bool(search(hcl_color_code)):
                tmp_hcl_valid = True
        return self.hcl is not None and tmp_hcl_valid

    def ecl_valid(self):
        valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.ecl is not None and self.ecl in valid_eye_colors

    def pid_valid(self):
        return self.pid is not None and len(self.pid) == 9

    def cid_valid(self):
        return True


def sol1(passports):
    count_valid_password = 0

    for passport in passports:
        passport_parsed = []
        passport_rows = passport.split("\n")
        for passport_row in passport_rows:
            infos = passport_row.split(" ")
            for info in infos:
                passport_field, passport_data = info.split(":")
                if passport_data != "":
                    passport_parsed.append((passport_field, passport_data))
        if len(passport_parsed) == 8 or (len(passport_parsed) == 7 and "cid" not in list(map(lambda x: x[:][0], passport_parsed))):
            count_valid_password += 1
    return count_valid_password


def sol2(passports):
    count_valid_password = 0
    for passport in passports:
        passport_obj = Passport()
        passport_rows = passport.split("\n")
        for passport_row in passport_rows:
            infos = passport_row.split(" ")
            for info in infos:
                passport_field, passport_data = info.split(":")
                if passport_data != "":
                    passport_obj.set_val(passport_field, passport_data)
        if passport_obj.valid():
            count_valid_password += 1
    return count_valid_password


def main():
    with open('input.txt', "r") as f:
        passports = str(f.read()).split("\n\n")

        sol_1 = sol1(passports)
        print(f"Solution 1: {sol_1}")

        sol_2 = sol2(passports)
        print(f"Solution 2: {sol_2}")


if __name__ == "__main__":
    main()
