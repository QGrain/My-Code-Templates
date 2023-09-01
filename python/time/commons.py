import re
from random import randint
from time import time


def time2sec(t):
    '''
    input: t, str: XdXhXmXs
    return: s, int: YYY 
    '''
    days, hours, minutes, seconds = 0, 0, 0, 0
    if 'd' in t:
        days = int(t.split('d')[0])
        t = t.split('d')[1]
    if 'h' in t:
        hours = int(t.split('h')[0])
        t = t.split('h')[1]
    if 'm' in t:
        minutes = int(t.split('m')[0])
        t = t.split('m')[1]
    if 's' in t:
        seconds = int(t.split('s')[0])
    
    total_seconds = (days * 24 * 3600) + (hours * 3600) + (minutes * 60) + seconds
    return total_seconds


def time2sec_re(t):
    '''
    input: t, str: XdXhXmXs
    return: s, int: YYY 
    '''
    match = re.match(r'(\d+d)?(\d+h)?(\d+m)?(\d+s)?', t)
    
    days = int(match.group(1)[:-1]) if match.group(1) else 0
    hours = int(match.group(2)[:-1]) if match.group(2) else 0
    minutes = int(match.group(3)[:-1]) if match.group(3) else 0
    seconds = int(match.group(4)[:-1]) if match.group(4) else 0
    
    total_seconds = (days * 24 * 3600) + (hours * 3600) + (minutes * 60) + seconds
    return total_seconds


def sec2time(s):
    '''
    input: s, int: YYY
    return: t, str: XdXhXmXs
    '''
    days, seconds = divmod(s, 24 * 3600)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    time_str = ''
    if days > 0:
        time_str += f'{days}d'
    if hours > 0:
        time_str += f'{hours}h'
    if minutes > 0:
        time_str += f'{minutes}m'
    if seconds > 0 or not time_str:
        time_str += f'{seconds}s'

    return time_str


if __name__ == '__main__':
    t0 = time()
    test_num = 100000
    test_t = [sec2time(randint(0, 10*86400)) for i in range(test_num)]
    t1 = time()
    print('[Cost %.6fs] %d testcase generation done'%(t1-t0, test_num))
    for t in test_t:
        s = time2sec(t)
    t2 = time()
    print('[Cost %.6fs] time2sec done'%(t2-t1))
    for t in test_t:
        s = time2sec_re(t)
    t3 = time()
    print('[Cost %.6fs] time2sec_re done'%(t3-t2))
    
    if (t2-t1) < (t3-t2):
        print('[+] Conclusion: time2sec() is faster than time2sec_re()')
    else:
        print('[+] Conclusion: time2sec_re() is faster than time2sec()')
    
    