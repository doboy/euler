class SuDoKuPosition(object):
  def __init__(self, row, col):
    self.row = row
    self.col = col

  def __eq__(self, other):
    return (self.same_row(other) and
            self.same_col(other))

  def __str__(self):
    return str((self.row, self.col))

  def __hash__(self):
    return hash((self.row, self.col))

  def same_square(self, other):
    self_square_index = (self.row // 3) * 3 + (self.col // 3)
    other_square_index = (other.row // 3) * 3 + (other.col // 3)
    return self_square_index == other_square_index

  def same_row(self, other):
    return self.row == other.row

  def same_col(self, other):
    return self.col == other.col

class SuDoKuBoard(object):
  def __init__(self, rows):
    self.rows = rows

  def is_solved(self):
    return all(value for position, value in self.items())

  def items(self):
    for i, row in enumerate(self.rows):
      for j, value in enumerate(row):
        yield SuDoKuPosition(i, j), value

  def get(self, position):
    return self.rows[position.row][position.col]

  def set(self, position, value):
    self.rows[position.row][position.col] = value

  def unset(self, position):
    self.rows[position.row][position.col] = 0

class CSP(object):
  def __init__(self, board):
    self.board = board

  def recusrive_backtrack(self, domain=None):
    if not domain:
      domain = self.calculate_domain()

    if self.board.is_solved():
      return self.board

    position = self.position_with_lowest_remaining_value_possible(domain)
    for possible_value in domain[position]:
      self.apply_assignment(position, possible_value)

      new_domain = self.calculate_domain()
      result = self.recusrive_backtrack(new_domain)

      if result:
        return result

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

class SoDokuCSP(CSP):
  def apply_assignment(self, position, possible_value):
    self.board.set(position, possible_value)

  def unapply_assignment(self, position):
    self.board.unset(position)

  def calculate_domain(self):
    full_domain = {}
    for position, value in self.board.items():
      domain = set()

      if not value:
        domain = set(xrange(1, 10))
        for _position, value in self.board.items():
          if value not in domain:
            continue

          if not value:
            continue

          elif position == _position:
            continue

          elif position.same_square(_position):
            domain.remove(value)

          elif (position.same_row(_position) or
                position.same_col(_position)):
            domain.remove(value)

        full_domain[position] = domain

    return full_domain

def main():
  grid_datas = []
  grid_data = []
  for line in open('txt/p096'):
    line = line.strip()
    if line.startswith('Grid'):
      assert len(grid_data) == 0
    else:
      grid_data.append(map(int, line))
      if len(grid_data) == 9:
        grid_datas.append(grid_data)
        grid_data = []

  final_answer = 0
  for grid_data in grid_datas:
    board = SuDoKuBoard(grid_data)
    csp = SoDokuCSP(board)
    final_board = csp.recusrive_backtrack()
    answer = int('%s%s%s' % (
        final_board.rows[0][0],
        final_board.rows[0][1],
        final_board.rows[0][2]))
    final_answer += answer
  print final_answer

if __name__ == '__main__':
  main()
