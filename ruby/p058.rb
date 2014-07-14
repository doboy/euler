require 'prime'

def spiral_gen
end

def spiral_primes(under)
  prime_count = 0
  total_count = 0
  i = 1
  inc = 2
  while true
    1.upto(4) do
      i += inc

      sprial_num = i
      if Prime.prime? sprial_num
        prime_count += 1
      end
      total_count += 1

      if prime_count / total_count.to_f < under
        return inc - 1
      end

    end
    inc += 2
  end
end

puts spiral_primes 0.1
