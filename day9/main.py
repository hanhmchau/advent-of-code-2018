import operator
from collections import deque

def read(file):
    f = open(file, 'r')
    contents = f.read()
    parts = contents.split()
    return int(parts[0]), int(parts[6])

class Marble:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self
    
    def add(self, marble):
        if marble % 23 == 0:
            marble_to_remove = self
            for i in range(7):
                marble_to_remove = marble_to_remove.prev
            marble_to_remove.next.prev = marble_to_remove.prev
            marble_to_remove.prev.next = marble_to_remove.next
            return marble_to_remove.next, marble_to_remove.value + marble
        else:
            new_marble = Marble(marble)
            one_after = self.next
            two_after = self.next.next

            one_after.next = new_marble
            new_marble.prev = one_after

            new_marble.next = two_after
            two_after.prev = new_marble
            return new_marble, 0

def play(player_count, last_marble):
    players = [ 0 ] * player_count
    current_player = 0
    current_marble = Marble(0)
    marbles = [ last_marble - i for i in range(last_marble)]
    while len(marbles):
        marble = marbles.pop()
        current_marble, score_earned = current_marble.add(marble)
        players[current_player] += score_earned
        current_player = (current_player + 1) % player_count
    return max(players)
from collections import deque, defaultdict

player_count, last_marble = read('day9/main.txt')
high = play(player_count, last_marble * 100)
print(high)