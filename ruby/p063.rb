def best_binary_search(lower, upper, n, target)
  while true
    mid = (lower + upper) / 2
    if (mid ** n).to_s.length > target
      upper = mid
    else
      lower = mid
    end

    if lower + 1 == upper
      return [lower, upper]
    end
  end
end

def powerful_digit_counts(n)
  # do an exponential search to find the limit
  lower = 0
  upper = 1
  while (upper ** n).to_s.length <= n
    if (upper ** n).to_s.length < n
      lower = upper
    end

    upper *= 2
  end

  a, b = best_binary_search(lower, upper, n, n - 0.5)
  c, d = best_binary_search(lower, upper, n, n + 0.5)
  d - b
end

def main
  n = 1
  result = 0
  while true
    count = powerful_digit_counts(n)
    if count == 0
      return result
    end
    result += count
    n += 1
  end
end

puts main
