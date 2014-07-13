require 'set'

def main(count, top)
  h = Hash.new { Set.new }
  seq = []
  seen_sets = Set.new

  2.upto(top) do |i|
    if h[i].length >= 5
      next
    end

    if h[i].length == 0
      h[i] = h[i].add(i)
    end

    if not seen_sets.include?(h[i])
      i.step(top, i) { |ii|
        h[ii] = h[ii].merge(h[i])
      }
    end

    if h[i].length == count
      if seq[-1] and seq[-1] + 1 == i
        seq << i
      else
        seq = [i]
      end

      if seq.length == count
        return seq
      end
    end

    seen_sets.add(h[i])
  end

  return
end

puts main(4, 1000000)[0]
