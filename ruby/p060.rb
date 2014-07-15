# require 'prime'
# require 'set'

# def prime_pair_sets set_length
#   prime_sets = Set.new
#   Prime.each do |new_p|
#     new_prime_sets = prime_sets.map { |prime_set|
#       if prime_set.all? { |p|
#           (Prime.prime? ((p.to_s + new_p.to_s).to_i) and
#             Prime.prime? ((new_p.to_s + p.to_s).to_i))
#         }

#         new_set = Set.new(prime_set.to_a + [new_p])

#         if new_set.length == set_length
#           return new_set
#         end

#         new_set
#       end
#     }.keep_if { |_| _ }

#     new_prime_sets.each { |prime_set|
#       prime_sets.add(prime_set)
#     }

#     prime_sets.add(Set.new([new_p]))
#   end
# end

# puts prime_pair_sets(5).to_a
