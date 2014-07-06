# TODO: use combinatorics to solve this instead

def chain_under(n)
  hash = Hash.new
  answer = 0

  1.upto(n - 1) do |num|
    sos = sum_of_squares num
    while sos != 1 and sos != 89
      if hash.include? sos
        sos = hash[sos]
      else
        sos = sum_of_squares sos
      end
    end

    if num < 10000
      hash[num] = sos
    end

    if sos == 89
      answer += 1
    end
  end

  answer
end

def get_cache_key(num)
  num
end

def sum_of_squares(num)
  num.to_s.chars.reduce(0) { |memo, num| memo + num.to_i ** 2}
end

puts chain_under 10000000
