# Jordy Mukania
# ECE 241 Hw#1 time converter
# Aug 30, 2020

class Hw1Q1:
    @staticmethod
    def timeConvert(input_second):     # Converts seconds to days, hours, mins, seconds
        #Function variables for conversions

        spday = 86400  # Seconds/days
        sphrs = 3600  # Seconds/hours
        spmin = 60  # Seconds/min
        input = input_second            # Original input
        day = 0
        hour = 0
        min = 0
        sec = 0

        # Placers for strings at output
        d = ''
        h =''
        m = ''
        s = ''

        if input_second >= spday:   # Checks how many days
            day = input_second // spday
            input_second = input_second % spday
            # Checks for grammar
            if day == 1:
                d = str(day) + ' day'
            else:
                d = str(day) + ' days'

        if input_second < spday and input_second >= sphrs:  # Checks how many hours
            hour = input_second // sphrs
            input_second = input_second % sphrs
            # Checks for grammar
            if hour == 1:
                h = str(hour) + ' hour'
            else:
                h = str(hour) + ' hours'

        if input_second < sphrs and input_second >= spmin:  # Checks how many minutes
            min = input_second // spmin
            input_second = input_second % spmin
            # Checks for grammar
            if min == 1:
                m = str(min) + '  minute'
            else:
                m = str(min) + ' minutes'
        # Remainder is seconds left
        sec = input_second
        # Checks for grammar
        if input == 0:
            s = str(sec)+ ' seconds'
        elif sec == 1:
            s = str(sec)+ ' second'
        elif sec > 1:
            s = str(sec)+ ' seconds'
        else: s = ''

        # Commas and spacing
        ls =''
        lm = ''
        lh = ''

        if sec > 0 and (min or day or hour  > 0):
            ls = ', '
        if min > 0 and (day or hour  > 0):
            lm =', '
        if hour > 0 and day > 0:
            lh = ', '

        return d +lh+ h +lm+ m +ls+ s

print(Hw1Q1.timeConvert(100000))