# time transformation


- `sec2time`

```python
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
```

Tests:
```bash
sec2time(114514) == '1d7h48m34s'
sec2time(86401) == '1d1s'
sec2time(0) == '0s'
```

- `time2sec`

```python
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

# the re implementation
import re
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
```

Tests:
```bash
time2sec('1d1m1s') == 86461
time2sec('32d17h') == 2826000
time2sec('0') == 0
```

After test, time2sec() is faster than time2sec_re().
```bash
python .\python\time\commons.py
[Cost 0.129689s] 100000 testcase generation done
[Cost 0.138655s] time2sec done
[Cost 0.208080s] time2sec_re done
[+] Conclusion: time2sec() is faster than time2sec_re()
```