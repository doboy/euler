# mods = 0.upto(9).group_by do |n|
#   n * n % 10
# end

# def find_square_root(digits, result_so_far)
#   square = result_so_far ** 2

#   if digits[-1] == '_'
#   else
#     last_digit = digits[-1]
#     last_digit[mods].each do |n|
#       next_result_so_far = n * (Math.log10(result_so_far).to_i + 1) ** 10 + result_so_far
#       result = find_square_root(digits, next_result_so_far)
#       if result
#         return result
#       end
#     end
#   end
# end

# puts find_square_root ([
#                          1, '_',
#                          2, '_',
#                          3, '_',
#                          4, '_',
#                          5, '_',
#                          6, '_',
#                          7, '_',
#                          8, '_',
