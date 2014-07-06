def sub_squares(n, m)
  answer = 0
  1.upto(n) do |n_|
    1.upto(m) do |m_|
      answer += (m - m_ + 1) * (n - n_ + 1)
    end
  end

  answer
end

def binary_search_squares(n, target)
  high = 2

  while sub_squares(n, high) < target
    high *= 2
  end

  low = high / 2
  while low + 1 != high
    mid = (low + high) / 2
    squares = sub_squares(n, mid)
    if squares > target
      high = mid
    else
      low = mid
    end
  end

  if sub_squares(n, low) > target
    below = low - 1
    above = low
  else
    below = low
    above = low + 1
  end

  if (sub_squares(n, below) - target).abs < (sub_squares(n, above) - target).abs
    below
  else
    above
  end
end

def main
  two_mil = 2000000

  # find the square that is closes to two mill
  max_n = 1
  while sub_squares(max_n, max_n) < two_mil
    max_n += 1
  end

  closest_squares_so_far = two_mil
  closest_area_so_far = two_mil

  max_n.downto(1) do |n|
    m = binary_search_squares(n, two_mil)
    abs = (two_mil - sub_squares(n, m)).abs
    if abs < closest_squares_so_far
      closest_squares_so_far = abs
      closest_area_so_far = n * m
    end
  end

  closest_area_so_far
end

puts main
