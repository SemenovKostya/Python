a = input('Enter your message: ')
print(a)

D = int(input("Enter the number of difference: "))
G = ''
flag = -1
for i in range (len(a)):
    if a[i] == 'Z' or a[i] == 'z':
        b = ord(a[i])
        c = chr(b - 26 + D)
    if a[i].islower():    
        if ord(a[i]) + D > ord('z'):
            b = ord(a[i])
            c = chr(b + D - 26) # The 26 means lenght of english alphabet
        elif ord(a[i]) + D == ord('z'):
            b = ord(a[i])
            c = chr(b + D - 2)
        else:
            b = ord(a[i])
            c = chr(b + D)
    if a[i].isupper():
        if ord(a[i]) + D > ord('Z'):
            b = ord(a[i])
            c = chr(b + D - 26) # The 26 means lenght of english alphabet
        elif ord(a[i]) + D == ord('Z'):
            b = ord(a[i])
            c = chr(b + D - 2)
        else:
            b = ord(a[i])
            c = chr(b + D)
    if a[i].isspace():
        if ord(a[i]) > flag:
            c = ' '
    if a[i].isdigit():
        c = a[i]
    G += c
print(G)


from datetime import datetime, timedelta, timezone
class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError("Name cannot be empty")
        self.name = name

        if not isinstance(offset_hours, int):
            raise ValueError ("Offset hour must be named")

        if not isinstance(offset_minutes, int):
            raise ValueError ("Offset hour must be named")
        if offset_minutes > 59 or offset_minutes < -59:
            raise ValueError("Offset must be between -59 and 59 (inclusive)")
        offset = timedelta(hours = offset_hours, minutes = offset_minutes)

        if offset < timedelta(hours = -12, minutes = 0) or offset > timedelta(hours = 14, minutes = 0):
            raise ValueError("Timezone offset ")
        self.offset = offset
        self_offset_hours = offset.hours
        self_offset_minutes = offset.minutes

        @property
        def  name (self):
            return self._name

        @property
        def offset(self):
            return self._offset

        def __eq__(self,other):
            return (
                isinstance(other, TimeZone)
                and self._name == other._name
                and self._offset_hours == other._offset_hours
                and self._offset_minutes == other._offset_minutes

            )

        def __repr__(self):
            return (
                f"TimeZone(name = {self._name}, offset_hours = {self._other_hours}, offset_minutes = {self._other_minutes}"
            )