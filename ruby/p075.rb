# require 'fiber'

# def singular_integar_right_triangles(length)
#   2
# end

# right_triangle_generator = Fiber.new do
#   c = 5
#   while true
#     1.upto(c - 1).each do |b|
#       1.upto(b - 1).each do |a|
#         if a ** 2 + b ** 2 == c ** 2
#           Fiber.yield [a, b, c]
#         end
#       end
#     end
#     c += 1
#   end
# end

# while true
#   a, b, c = right_triangle_generator.resume
#   print "#{a} #{b} #{c}\n"
#   if c > 1500000
#     break
#   end
# end
