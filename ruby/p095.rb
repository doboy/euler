def chains_under(n)
  seen = Hash.new
  next_hash = Hash.new
  largest_chain_so_far = 0
  smallest_element_of_largest_chain = nil

  1.upto(n) do |num|
    puts num

    if seen.include? num
      next
    end

    starting_element = num
    current_element = num
    elements = []

    begin
      elements << current_element
      if not next_hash.include? current_element
        next_element = next_element(current_element)
        next_hash[current_element] = next_element
      end

      current_element = next_hash[current_element]
      seen[current_element] = true
    end while not elements.include? current_element and current_element != 0 and current_element < n

    if current_element == 0 or current_element > n
      next
    end

    chain = elements[elements.index(current_element)..elements.length]
    if chain.length > largest_chain_so_far
      largest_chain_so_far = chain.length
      smallest_element_of_largest_chain = chain.min
    end
  end

  [smallest_element_of_largest_chain, largest_chain_so_far]
end

def next_element(num)
  1.upto(num - 1).select {|n| num % n == 0}.reduce(0, :+)
end

# puts chains_under(1000000)
