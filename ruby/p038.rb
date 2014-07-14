require 'set'

def pandigital_multiples? n
  seen_chars = []
  multipler = 1

  while true
    chars = (n * multipler).to_s.chars

    if chars.include? '0'
      return false
    end

    chars.each do |char|
      if seen_chars.include? char
        return false
      end

      seen_chars << char
    end

    if seen_chars.length == 9
      return seen_chars.reduce(:+).to_i
    end

    multipler += 1
  end
end

def main
  best = 0
  1.upto(10000).each{ |n|
    pan = pandigital_multiples?(n)
    if pan and pan > best
      best = pan
    end
  }

  best
end

puts main
