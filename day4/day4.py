import datetime
import re
import operator

def read(file):
    f = open(file, 'r')
    contents = f.read()
    lines = contents.split('\n')
    return lines


WAKE = 'wake'
SLEEP = 'sleep'
BEGIN = 'begin'


def parse_event(line):
    parts = line.split()
    date_parts = parts[0][1:].split('-')
    month = int(date_parts[1])
    day = int(date_parts[2])
    time_parts = parts[1][:-1].split(':')
    hour = int(time_parts[0])
    minute = int(time_parts[1])
    if (parts[2] == 'wakes'):
        event = WAKE
        guard = None
    if (parts[2] == 'falls'):
        event = SLEEP
        guard = None
    if (parts[2] == 'Guard'):
        event = BEGIN
        guard = parts[3]
    return (month, day, hour, minute, event, guard)

def time_value(line):
    return re.search('(?<=\[).+(?=\])', line).group()

def parse_events(lines):
    return [parse_event(line) for line in sorted(lines, key=lambda line: time_value(line))]

def process(events):
    reports = {}
    attendants = {}
    currentGuard = None
    mostRecentSleepTime = 0
    for ev in events:
        month = ev[0]
        day = ev[1]
        hour = ev[2]
        minute = ev[3]
        event = ev[4]
        if event == BEGIN:
            currentGuard = ev[5]
            if currentGuard not in attendants:
                attendants[currentGuard] = 0
        if (month, day) not in reports:
            reports[(month, day)] = (currentGuard, [ None ] * 60)
        if event == SLEEP:
            mostRecentSleepTime = minute
        if event == WAKE:
            attendants[currentGuard] += (minute - mostRecentSleepTime)
            for i in range(mostRecentSleepTime, minute):
                reports[(month, day)][1][i] = SLEEP
    return reports, attendants

def find_sleepiest_guard(attendants):
    return max(attendants.items(), key = operator.itemgetter(1))[0]

def find_minute_guard_sleeps_most(reports, guard):
    freqs = [ 0 ] * 60
    for key in reports:
        month, day = key
        dayGuard = reports[key][0]
        if (guard == dayGuard):
            minutes = reports[key][1]
            for i in range(60):
                if minutes[i] == SLEEP:
                    freqs[i] += 1
    return freqs.index(max(freqs))

def find_most_frequently_asleep_same_minute(reports, attendants):
    freqs = {};
    for guard in attendants:
        freqs[guard] = [ 0 ] * 60
    for key in reports:
        guard = reports[key][0]
        minutes = reports[key][1]
        for min in range(60):
            if minutes[min] == SLEEP:
                freqs[guard][min] += 1

    maxGuard = ''
    maxMinute = 0
    maxFreq = 0
    for guard in freqs:
        freq = max(freqs[guard])
        if freq > maxFreq:
            maxFreq = freq
            maxMinute = freqs[guard].index(freq)
            maxGuard = guard
    return maxGuard, maxMinute

lines = read('day4/day4.txt')
events = parse_events(lines)
reports, attendants = process(events)

# Part 1
# guard = find_sleepiest_guard(attendants)
# minute = find_minute_guard_sleeps_most(reports, guard)

# Part 2
guard, minute = find_most_frequently_asleep_same_minute(reports, attendants)

guardId = int(guard[1:])
print(guardId * minute)
