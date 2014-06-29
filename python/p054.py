# see: http://projecteuler.net/problem=54

from collections import defaultdict

TEN, JACK, QUEEN, KING, ACE = 10, 11, 12, 13, 14

VALUE_TO_STR_MAP = {
  ACE: "A",
  KING: "K",
  QUEEN: "Q",
  JACK: "J",
  TEN: "T"
}

STR_TO_VALUE_MAP = { v:k  for k, v in VALUE_TO_STR_MAP.iteritems() }

class Card:
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit

  @staticmethod
  def parse(a_str):
    value, suit = a_str
    value = int(STR_TO_VALUE_MAP.get(value, value))

    return Card(value=value, suit=suit)

  def __str__(self):
    value = str(VALUE_TO_STR_MAP.get(self.value, self.value))

    return "%s%s" % (value, self.suit)

class Hand:
  def __init__(self, cards):
    self.cards = cards

  def _get_high_card(self):
    single_cards = self._get_cards_with_occurance(1)
    if single_cards:
      return max(card.value for card in single_cards)

  def _get_cards_with_occurance(self, occurance):
    value_map = self._get_value_map()
    count_distribution = self._get_count_distribution()
    return tuple([
        card for card in self.cards
        if value_map[card.value] == occurance])

  def _get_values_with_occurance(self, occurance):
    return tuple(sorted([
        card.value for card in self._get_cards_with_occurance(occurance)]))

  def _get_lowest_card(self):
    return min(card.value for card in self.cards)

  def _get_value_map(self):
    value_map = defaultdict(int)
    for card in self.cards:
      value_map[card.value] += 1

    return value_map

  def _get_count_distribution(self):
    value_map = self._get_value_map()

    count_distribution = defaultdict(int)
    for value, occurance in value_map.iteritems():
      count_distribution[occurance] += 1

    return count_distribution

  def is_one_pair(self):
    count_distribution = self._get_count_distribution()
    return (count_distribution[2] == 1)

  def is_two_pairs(self):
    count_distribution = self._get_count_distribution()
    return (count_distribution[2] == 2)

  def is_full_house(self):
    count_distribution = self._get_count_distribution()
    return (count_distribution[2] == 2 and
            count_distribution[3] == 1)

  def is_three_of_a_kind(self):
    count_distribution = self._get_count_distribution()
    return (count_distribution[3] == 1)

  def is_four_of_a_kind(self):
    count_distribution = self._get_count_distribution()
    return (count_distribution[4] == 1)

  def is_flush(self):
    return len(set(card.suit for card in self.cards)) == 1

  def is_straight(self):
    sorted_cards = sorted(self.cards, key=lambda x: x.value)
    current_card_value = self._get_lowest_card()
    for card in sorted_cards:
      if card.value != current_card_value:
        return False

      current_card_value += 1

    return True

  def is_straight_flush(self):
    return self.is_flush() and self.is_straight()

  def is_royal_flush(self):
    return self._get_high_card() == ACE and self.is_straight_flush()

  def is_two_pair(self):
    return set(card.value for card in self.cards) < 2

  def __cmp__(self, other):
    if self.get_hand_rank() < other.get_hand_rank():
      return -1
    elif self.get_hand_rank() > other.get_hand_rank():
      return 1
    elif self.get_hand_rank() == other.get_hand_rank():
      return 0
    else:
      raise ValueError

  def get_hand_rank(self):
    high_card = self._get_high_card()

    if self.is_royal_flush():
      return (10,)

    elif self.is_straight_flush():
      return (9, high_card)

    elif self.is_four_of_a_kind():
      four_rank = self._get_values_with_occurance(4)
      return (8, four_rank, high_card)

    elif self.is_full_house():
      three_rank = self._get_values_with_occurance(3)
      two_rank = self._get_values_with_occurance(2)
      return (7, three_rank, two_rank)

    elif self.is_flush():
      return (6, high_card)

    elif self.is_straight():
      return (5, high_card)

    elif self.is_three_of_a_kind():
      three_rank = self._get_values_with_occurance(3)
      return (4, high_card, three_rank)

    elif self.is_two_pairs():
      return (3, high_card)

    elif self.is_one_pair():
      two_rank_lower, two_rank_higher = self._get_values_with_occurance(2)
      return (2, two_rank_higher, two_rank_lower, high_card)

    else:
      return (1, high_card)

  def __str__(self):
    return "%s" % map(Card.__str__, self.cards)

def main():
  total = 0
  for line in open( "txt/p054" ):
    card_strs = line.strip().split()
    if not card_strs:
      continue
    cards = map(Card.parse, card_strs)
    hand1, hand2 = Hand(cards[:5]), Hand(cards[5:])
    if hand1 > hand2:
      total += 1
  return total

print main()
