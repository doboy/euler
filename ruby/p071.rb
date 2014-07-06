def ordered_fraction_left_of (d, left_of)
  num = 0
  dem = 1.0
  max_num_and_dem_so_far = num, dem
  max_value_so_far = num / dem

  while dem < d
    if num / dem < left_of
      while num / dem < left_of
        num += 1
      end
      num -= 1
    else
      while num / dem > left_of
        num -= 1
      end
    end

    if is_coprime(num, dem) and (num / dem) > max_value_so_far
      max_num_and_dem_so_far = num, dem
      max_value_so_far = num / dem
    end

    dem += 1.0
  end

  max_num_and_dem_so_far
end

def is_coprime(num, dem)
  gcd(num, dem) == 1
end

def gcd(a, b)
  if b == 0
    a
  else
    gcd(b, a % b)
  end
end

puts ordered_fraction_left_of(1000000, 3/7.0)[0]
