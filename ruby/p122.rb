# def multiplication_count(memo, exp_1, exp_2, used)
#   count = 1

#   if exp_1 == exp_2
#     if (used & (1 << exp_1)) == 0
#       count += minimum_multiplications(memo, exp_1, used)
#     end
#   else
#     if (used & (1 << exp_1)) == 0
#       count += minimum_multiplications(memo, exp_1, used | (1 << [exp_1, exp_2].min))
#     end

#     if (used & (1 << exp_2)) == 0
#       count += minimum_multiplications(memo, exp_2, used | (1 << [exp_1, exp_2].min))
#     end
#   end

#   count
# end

# def minimum_multiplications(memo, exp, used)
#   if exp == 1
#     return 0
#   end

#   if memo[exp] and memo[exp][used]
#     return memo[exp][used]
#   end

#   min_count = 1.upto(exp / 2).map { |exp_1|
#     exp_2 = exp - exp_1
#     multiplication_count(memo, exp_1, exp_2, used)
#   }.min

#   if not memo.include? exp
#     memo[exp] = Hash.new
#   end

#   memo[exp][used] = min_count

#   min_count
# end

# def main
#   memo = Hash.new
#   1.upto(200).map { |num|
#     puts num
#     minimum_multiplications(memo, num, 0)
#   }.reduce(:+)
# end

# puts main
