def square_root_convergents(expansions)
  current_rational = '3/2'.to_r
  count = 0
  1.upto(expansions) do |n|
    current_rational = current_rational + 1
    current_rational = 1 / current_rational
    current_rational = current_rational + 1

    if (current_rational.numerator.to_s.length >
        current_rational.denominator.to_s.length)
      count += 1
    end
  end

  count
end

puts square_root_convergents 1000
