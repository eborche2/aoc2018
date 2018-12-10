from collections import deque, defaultdict
def playRound(circle, current_round, current_marble, scores, player, flip, t_rounds):

    where = circle.index(current_marble)
    if where == 1 and current_round > t_rounds / 2:
        flip = True
    if current_round % 23 == 0:
        scores[player] += current_round
        scores[player] += circle[where - 7]
        current_marble = circle[where -6]
        circle = circle[:where-7] + circle[where-6:]
        return circle, current_round + 1, current_marble, scores, player + 1
    else:
        if where + 7 % 23 == 0:

        if where + 2 == len(circle):
            circle.append(current_round)
        elif where + 1 == len(circle):
            circle = circle[:1] + [current_round] + circle[1:]
        else:
            circle = circle[:where + 2] + [current_round] + circle[where + 2:]
        if flip and where > 100:
            circle = circle[80:]
        return circle, current_round + 1, current_round, scores, player + 1

check = False
players = 424
o_scores = [0 for each in range(players)]
o_circle = [0]
rounds = 71482
o_current_round = 3
o_current_marble = 2
o_circle.append(1)
o_circle = o_circle[:1] + [2] + o_circle[1:]
o_player = 3
while o_current_round <= rounds:
    o_circle, o_current_round, o_current_marble, o_scores, o_player = playRound(o_circle, o_current_round, o_current_marble, o_scores, o_player, check, rounds)
    if o_player == players:
        o_player = 0
    #if o_current_round % 999 == 0:
     #   import pdb; pdb.set_trace()
print(max(o_scores))# Part 1, could definitely make this faster, took about a minute.


def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

print(play_game(424, 7148200))#Part 2, I had to sit down and study the print outs of a few hundred lines to catch this.



