# require 'Set'

# def triangle n
#   n * (n + 1) / 2
# end

# def square n
#   n * n
# end

# def pentagon n
#   n * (3 * n - 1) / 2
# end

# def hexagon n
#   n * (2 * n - 1)
# end

# def heptagon n
#   n * (5 * n - 3) /2
# end

# def octagon n
#   n * (3 * n - 2)
# end

# def numbers_between(low, high, fn)
#   result = []
#   i = 0
#   while true
#     val = fn.call(i)
#     if val > high
#       return result
#     end

#     if val >= low
#       result << val
#     end
#     i += 1
#   end
# end

# def satisfies(numbers)
#   numbers_s = numbers.map { |number|
#     number.to_s
#   }

#   numbers_s.each_with_index { |n_s, index|
#     if n_s[0..1] != numbers_s[index - 1][2..4]
#       return false
#     end

#     if n_s[2..4] != numbers_s[(index + 1) % numbers_s.length][0..1]
#       return false
#     end
#   }

#   return true
# end

# def cyclical_figurate_numbers
#   h = Hash.new

#   [:triangle, :square, :pentagon, :hexagon, :heptagon, :octagon].each do |sym|
#     fn = method(sym)
#     h[sym] = numbers_between(1000, 10000, fn)
#   end

#   h[:triangle].each do |a|
#     h[:square].each do |b|
#       h[:pentagon].each do |c|
#         h[:hexagon].each do |d|
#           h[:heptagon].each do |e|
#             h[:octagon].each do |f|
#               if Set.new([a, b, c, d, e, f]).length == 6
#                 [a, b, c, d, e, f].permutation.each do |p|
#                   if satisfies(p)
#                     return p.reduce(:+)
#                   end
#                 end
#               end
#             end
#           end
#         end
#       end
#     end
#   end
# end

# puts cyclical_figurate_numbers
