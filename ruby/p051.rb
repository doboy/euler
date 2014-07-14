require 'prime'
require 'set'

def prime_digit_replacements(n)
  hash = Hash.new{ Set.new }
  digits = 1

  Prime.each do |p|
    p_s = p.to_s
    if p_s.length > digits
      hash = Hash.new{ Set.new }
      digits = p_s.length
    end

    0.upto(p_s.length - 3).each do |i|
      (i + 1).upto(p_s.length - 2).each do |j|
        (j + 1).upto(p_s.length - 1).each do |k|
          if p_s[i] == p_s[j] and  p_s[j] == p_s[k]
            new_p_s = String.new(p_s)
            new_p_s[i] = new_p_s[j] = new_p_s[k] = "*"
            primes = hash[new_p_s] = hash[new_p_s].add(p)
            if primes.length >= n
              return primes.min
            end
          end
        end

        if p_s[i] == p_s[j]
          new_p_s = String.new(p_s)
          new_p_s[i] = new_p_s[j] = "*"
          primes = hash[new_p_s] = hash[new_p_s].add(p)
          if primes.length >= n
            return primes.min
          end
        end
      end
    end
  end
end

puts prime_digit_replacements 8
