class CSP(object):
  def __init__(self, board):
    self.board = board

  def recursive_backtrack(self, domain=None):
    if not domain:
      domain = self.calculate_domain()

    if self.board.is_solved():
      yield self.board.copy()

    else:
      position = self.position_with_lowest_remaining_value_possible(domain)
      for possible_value in domain[position]:
        self.apply_assignment(position, possible_value)

        new_domain = self.calculate_domain()
        results = self.recursive_backtrack(new_domain)

        for result in results:
          yield result

      self.unapply_assignment(position)

  def position_with_lowest_remaining_value_possible(self, full_domain):
    best_so_far = None
    lowest_so_far = None

    for position, value in self.board.items():
      domain = full_domain.get(position)

      if value:
        continue

      elif best_so_far is None:
        best_so_far = position
        lowest_so_far = len(domain)

      elif len(domain) < lowest_so_far:
        best_so_far = position
        lowest_so_far = len(domain)

    return best_so_far

  def apply_assignment(self, position, possible_value):
    self.board.set(position, possible_value)

  def unapply_assignment(self, position):
    self.board.unset(position)

class Magic5gonRingCSP(CSP):
  def __init__(self, board, sum_total):
    CSP.__init__(self, board)
    self.sum_total = sum_total

  def calculate_domain(self):
    sum_total = self.sum_total
    full_domain = {}
    used_values = set(self.board.assigments.values())
    assigments = self.board.assigments
    for position, value in assigments.items():
      if value:
        domain = set()
      else:
        domain = set(xrange(1, 11)) - used_values
        if position == 0:
          neighbors = [[5, 6]]
        elif position == 1:
          neighbors = [[7, 6]]
        elif position == 2:
          neighbors = [[7, 8]]
        elif position == 3:
          neighbors = [[9, 8]]
        elif position == 4:
          neighbors = [[9, 5]]
        elif position == 5:
          neighbors = [[9, 4], [6, 0]]
        elif position == 6:
          neighbors = [[1, 7], [5, 0]]
        elif position == 7:
          neighbors = [[1, 6], [8, 2]]
        elif position == 8:
          neighbors = [[3, 9], [7, 2]]
        elif position == 9:
          neighbors = [[3, 8], [4, 5]]
        else:
          raise

        for neighbor_set in neighbors:
          n1, n2 = neighbor_set
          if assigments[n1] and assigments[n2]:
            domain = domain & set([sum_total - assigments[n1] - assigments[n2]])
          else:
            domain = domain & set(number for number in domain if
                                  number <= sum_total - assigments[n1] - assigments[n2])

      full_domain[position] = set(domain)

    return full_domain

class Magic5gonRingBoard(object):
  # 0 5 6, 1 6 7, 2 7 8, 3 8 9, 4 9 5
  #  v0
  #     v5  v1
  #   v9   v6
  # v4 v8 v7 v2
  #      v3
  def __init__(self):
    self.assigments = { k: 0 for k in xrange(0, 10) }

  def copy(self):
    result = Magic5gonRingBoard()
    result.assigments = {k: v for k, v in self.assigments.items()}
    return result

  def items(self):
    return self.assigments.items()

  def set(self, position, value):
    self.assigments[position] = value

  def unset(self, position):
    self.assigments[position] = 0

  def get(self, position):
    return self.assigments[position]

  def is_solved(self):
    return all(self.assigments.values())

  def __str__(self):
    lines = [
      (self.assigments[0], self.assigments[5], self.assigments[6]),
      (self.assigments[1], self.assigments[6], self.assigments[7]),
      (self.assigments[2], self.assigments[7], self.assigments[8]),
      (self.assigments[3], self.assigments[8], self.assigments[9]),
      (self.assigments[4], self.assigments[9], self.assigments[5])]

    starting_line = min(lines)

    result = ''
    for i in xrange(5):
      for item in lines[(lines.index(starting_line) + i) % len(lines)]:
        result += str(item)

    return result

def main():
  boards = []
  for sum_total in xrange(16):
    board = Magic5gonRingBoard()
    csp = Magic5gonRingCSP(board, sum_total)
    boards += list(csp.recursive_backtrack())

  print max(map(str, boards))

if __name__ == '__main__':
  main()
