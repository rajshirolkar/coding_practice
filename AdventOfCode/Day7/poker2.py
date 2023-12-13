from collections import Counter
from functools import cmp_to_key


def read_file(file_name):
    input_array = []
    with open(file_name, "r") as file:
        for line in file:
            input_array.append(line.strip())
        return input_array


lines = read_file("input.txt")

card_ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

card_ranks_with_Joker = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 11,
    "9": 10,
    "8": 9,
    "7": 8,
    "6": 7,
    "5": 6,
    "4": 5,
    "3": 4,
    "2": 3,
    "J": 2,
}

hands = []
bids = []
for line in lines:
    hands.append(line.split()[0])
    bids.append(line.split()[1])
bids = list(map(int, bids))


print(hands, bids)


# get hand type
def get_hand_type(hand):
    hand_cnt = Counter(hand)
    # print(hand_cnt)

    # five of a kind
    if 5 in hand_cnt.values():
        return 6

    # four of a kind
    elif 4 in hand_cnt.values():
        return 5

    # full house
    elif 3 in hand_cnt.values() and 2 in hand_cnt.values():
        return 4

    # three of a kind
    elif 3 in hand_cnt.values():
        return 3

    # two pair
    elif list(hand_cnt.values()).count(2) == 2:
        return 2

    # one pair
    elif 2 in hand_cnt.values():
        return 1

    # high card
    else:
        return 0


def get_hand_type_with_joker(hand):
        hand_cnt = Counter(hand)
        # print(hand_cnt)

        # five of a kind
        if 5 in hand_cnt.values():
            return 6

        # four of a kind
        elif 4 in hand_cnt.values():
            if "J" in hand_cnt.keys():
                return 6
            return 5

        # full house
        elif 3 in hand_cnt.values() and 2 in hand_cnt.values():
            if "J" in hand_cnt.keys():
                return 6
            return 4

        # three of a kind
        elif 3 in hand_cnt.values():
            if "J" in hand_cnt.keys():
                return 5
            return 3

        # two pair
        elif list(hand_cnt.values()).count(2) == 2:
            if "J" in hand_cnt.keys():
                if hand_cnt["J"] == 2:
                    return 5
                elif hand_cnt["J"] == 1:
                    return 4
            return 2

        # one pair
        elif 2 in hand_cnt.values():
            if "J" in hand_cnt.keys():
                return 3
            return 1

        # high card
        else:
            if "J" in hand_cnt.keys():
                return 1
            return 0


# ranking 2 hands
def rank_hands(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    for i in range(5):
        # print(hand1[i], hand2[i])
        if card_ranks_with_Joker[hand1[i]] > card_ranks_with_Joker[hand2[i]]:
            return 1
        elif card_ranks_with_Joker[hand1[i]] < card_ranks_with_Joker[hand2[i]]:
            return -1
    return 0


def part2(hands, bids):
    hand_types = {i: [] for i in range(7)}

    # put hands into hand_types
    for i, hand in enumerate(hands):
        hand_types[get_hand_type_with_joker(hand)].append((hand, bids[i]))

    # sort each hand type
    for i in range(7):
        # hand_types[i] = sorted(hand_types[i], key=lambda x: card_ranks[x[0][0]], reverse=True)
        hand_types[i] = sorted(hand_types[i], key=cmp_to_key(rank_hands), reverse=True)

    # print(hand_types)
    # calculate score based on bids
    cnt = 1
    ans = 0
    # go through hand types from lowest to highest
    for i in range(7):
        if len(hand_types[i]) > 0:
            # sort through each hand from highest to lowest
            for j in range(len(hand_types[i]) - 1, -1, -1):
                ans += hand_types[i][j][1] * cnt
                print(ans, cnt, hand_types[i][j])
                cnt += 1
    return ans


print(part2(hands, bids))
# print(get_hand_type(hands[0]))
