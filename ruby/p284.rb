# def convert_base_14_single(n)
#   if n < 10
#     n.to_s
#   else
#     {
#       10 => 'a',
#       11 => 'b',
#       12 => 'c',
#       13 => 'd'
#     }[n]
#   end
# end

# def convert_base_14(n)
#   result = []
#   while n > 0
#     digit = n % 14
#     result << convert_base_14_single(digit)
#     n /= 14
#   end

#   result.reverse.join
# end

# def main
#   results = []
#   1.upto(10000) do |n|
#     if convert_base_14(n * n).end_with? convert_base_14(n)
#       results << n
#     end
#   end

#   convert_base_14(results.reduce(:+))
# end

# puts main
