def pow_exp_mod(a, b, mod)
  # a ^ b = (a ^ 2) ^ (b/2)
  result = 1
  a_pow = a

  b = b.to_i
  while b != 0
    if b & 1 != 0
      result = (result * a_pow) % mod
    end

    a_pow = (a_pow ** 2) % mod
    b >>= 1
  end

  result
end

# puts pow_exp_mod(3, 5, 1000)

# 1 000 000 000 000
#   *** *** *xx xxx

# 100
#  *x
def fact_trailing_digits(n, m)
  result = 1
  two_count = 0

  2.upto(10 ** m - 1).each do |number|
    inner_two_count = 0
    inner_five_count = 0
    while number % 2 == 0
      number /= 2
      inner_two_count += 1
    end

    while number % 5 == 0
      number /= 5
      inner_five_count += 1
    end

    two_count += (inner_two_count - inner_five_count) * (10 ** (n - m)).ceil
    b = (10 ** (n - m)).ceil
    exp = pow_exp_mod(number, b, 10 ** m)
    # puts "#{number} ** #{b} = #{exp}"
    result = (result * exp) % (10 ** m)
  end

  exp = pow_exp_mod(2, two_count, 10 ** m)
  result = (result * exp) % (10 ** m)
  result
end

# puts pow_exp_mod( 54939, 10000000, 100000)
# puts pow_exp_mod(5, 249940000000, 100000)
# puts fact_trailing_digits(4, 3)
