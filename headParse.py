__author__ = 'maxh'


class xl2array():
    def __init__(self, entry):
        assert (entry.count(':') == 2)
        s_entry = entry.split(':')
        self.elem = s_entry[0]
        self.value = s_entry[1]
        self.action = s_entry[2]

if __name__ == '__main__':
    a = xl2array('name:feeSettlePeriod:click_value')
    print(a.elem)
    print(a.value)
    print(a.action)