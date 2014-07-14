def pentagon(n)
  n * (3 * n - 1) / 2
end

def square?(n)
  sqrt = Math.sqrt(n)
  return sqrt == sqrt.to_i
end

def pentagon?(n)
  determinant = 1 + 4 * 3 * 2 * n
  square?(determinant) and (1 + Math.sqrt(determinant)) % 6 == 0
end

def main
  current_diffs = {
    1 => 4
  }

  current_idxs = {
    1 => 1
  }

  while true
    curr_diff, idx = current_diffs.map{ |k, v| [v, k]}.min
    current_idx = current_idxs[idx]
    curr_sum = pentagon(current_idx) + pentagon(current_idx + idx)

    if pentagon?(curr_sum) and pentagon?(curr_diff)
      return curr_diff
    end

    new_idx = current_idx + 1
    new_diff = pentagon(new_idx + idx) - pentagon(new_idx)
    while not pentagon?(new_diff)
      new_idx += 1
      new_diff = pentagon(new_idx + idx) - pentagon(new_idx)
    end

    current_idxs[idx] = new_idx
    current_diffs[idx] = new_diff

    max_key = current_diffs.keys.max
    curr_pent = pentagon(max_key + 1)
    while new_diff > curr_pent
      max_key += 1
      current_diffs[max_key] = curr_pent - 1
      current_idxs[max_key] = 1
      curr_pent = pentagon(max_key + 1)
    end
  end
end

puts main
