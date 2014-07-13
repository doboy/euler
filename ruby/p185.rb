# class Guess
#   def initialize(number, correct_amount)
#     @number = number
#     @correct_amount = correct_amount
#   end

#   def possible_orientation
#     results = []
#     if @correct_amount == 0
#       result = Hash.new
#       number.chars.each_with_index do |char, idx|
#         result[idx] = char
#       end
#       results << result
#     end

#     if @correct_amount == 1
#       0.upto(15).each do |idx|
#         result = Hash.new
#         number.chars.each_with_index do |char, inner_idx|
#           if idx != inner_idx
#             result[inner_idx] = char
#           end
#         end
#         results << result
#       end
#     end

#     if @correct_amount == 2
#       0.upto(15).each do |idx_1|
#         (idx_1 + 1).upto(15).each do |idx_2|
#           result = Hash.new
#           number.chars.each_with_index do |char, inner_idx|
#             if idx_1 != inner_idx and idx_2 != inner_idx
#               result[inner_idx] = char
#             end
#           end
#           results << result
#         end
#       end
#     end

#     if @correct_amount == 2
#       0.upto(15).each do |idx_1|
#         (idx_1 + 1).upto(15).each do |idx_2|
#           (idx_2 + 1).upto(15).each do |idx_3|
#             result = Hash.new
#             number.chars.each_with_index do |char, inner_idx|
#               if idx_1 != inner_idx and idx_2 != inner_idx and idx_3 != inner_idx
#                 result[inner_idx] = char
#               end
#             end
#             results << result
#           end
#         end
#       end
#     end
#   end
# end

# def try_apply_possible_orientation(possible_orientation, domain)
#   nil
# end

# def recursive_backtrack(guesses, domain)
#   if domain.solved?
#     return domain
#   end

#   for possible_orientation in guesses[0].possible_orientation
#     new_domain = try_apply_possible_orientation(possible_orientation, domain)
#     if not new_domain
#       next
#     end

#     result = recursive_backtrack(guesses[1..-1], new_domain)
#     if result
#       return result
#     end
#   end
# end
