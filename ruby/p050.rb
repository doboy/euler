require 'prime'

def main top
  primes = Prime.take_while { |p| p < top }
  result = 0
  conexc = 0
  ii, jj = 0, 0

  # partial_sums maps idx -> sum of primes[0..idx]
  partial_sums = Hash.new{ 0 }
  primes.each_with_index { |prime, idx|
    partial_sums[idx] = partial_sums[idx - 1] + prime
  }

  0.upto(partial_sums.length) { |i|
    (i + 1).upto(partial_sums.length).take_while { |j|
      partial_sums[j] - partial_sums[i] < top
    }.each { |j|
      if Prime.prime?(partial_sums[j] - partial_sums[i])
        if j - i > conexc
          result = partial_sums[j] - partial_sums[i]
          conexc = j - i
          ii = i
          jj = j
        end
      end
    }
  }

  result
end

puts main 1000000
