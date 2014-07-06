def apply_assignment_or_nil(assignment, word)
  word.chars.map { |char|
    assignment[char]
  }.join.to_i
end

def extract_assignment_or_nil(square, word)
  letter_map = Hash.new
  number_map = Hash.new

  square.to_s.chars.zip(word.chars).each do |number, char|
    if letter_map.include?(char) and letter_map[char] != number
      return
    end

    if number_map.include?(number) and number_map[number] != char
      return
    end

    number_map[number] = char
    letter_map[char] = number
  end

  letter_map
end

def get_max_anagram_square(w1, w2)
  i = 1
  squares = []
  while (i ** 2).to_s.length <= w1.length
    i += 1
    square = i ** 2
    if square.to_s.length == w2.length
      squares << square
    end
  end

  result = 0
  squares.each do |square|
    assignment = extract_assignment_or_nil(square, w1)

    if assignment != nil
      number = apply_assignment_or_nil(assignment, w2)
      if squares.include? number
        result = [result, number, square].max
      end
    end
  end

  result
end

def get_max_anagram_squares(words)
  result = 0
  words.each do |w1|
    words.each do |w2|
      if w1 != w2
        result = [result, get_max_anagram_square(w1, w2)].max
      end
    end
  end

  result
end

def main
  words = File.read('txt/p098').split(',').map { |word| word[1..-2] }

  anagrams = words.group_by do |word|
    word.chars.sort.join
  end

  anagram_keys_by_length = anagrams.keys.group_by { |key| key.length }
  anagram_keys_by_length.keys.sort.reverse.each { |length|
    anagram_keys = anagram_keys_by_length[length]
    max_square = 0
    anagram_keys.each { |anagram_key|
      _anagrams = anagrams[anagram_key]
      if _anagrams.length > 1
        max_square = [max_square, get_max_anagram_squares(_anagrams)].max
      end
    }

    if max_square != 0
      return max_square
    end
  }
end

puts main
