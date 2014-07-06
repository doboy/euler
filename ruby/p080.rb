require 'prime'

def digital_sum_root_100(n)

  digits = Math.sqrt(n).to_i
  target = n

  while digits.to_s.length < 110 do
    target = target * 100

    below = 0.upto(9).take_while { |num|
      (digits * 10 + num) ** 2 <= target
    }

    next_digit = below.last

    digits = digits * 10 + next_digit
  end

  digits
end

def two_factors(n)
  2.upto(n).each { |num|
    if n % num == 0
      return [n / num, num]
    end
  }
end

def main
  hash = Hash.new

  squares = 2.upto(9).map { |x|
    hash[x * x] = x
    x * x
  }

  2.upto(99).each { |num|
    if Prime.prime? num
      result = digital_sum_root_100(num)
    else
      result = two_factors(num).map { |factor|
        hash[factor]
      }.reduce(1, :*)
    end

    hash[num] = result
  }


  2.upto(99).select{ |num|
    not squares.include? (num)
  }.map { |num|
    hash[num].to_s[0..99].chars.inject(0) {
      |a, b| a.to_i + b.to_i
    }
  }.reduce(0, :+)
end

puts main
