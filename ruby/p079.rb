def analyze(passcodes)
  answer = []
  while true
    number = 0.upto(9).select { |number|
      not answer.include?(number) and passcodes.none? { |passcode|
        passcode.to_s[1..-1].include? number.to_s
      } and passcodes.any? { |passcode|
        passcode[0] == number.to_s
      }
    }.first

    answer << number

    passcodes = passcodes.map { |passcode|
      if passcode[0] == number.to_s
        passcode[1..-1]
      else
        passcode
      end
    }.select { |passcode|
      passcode.length != 0
    }

    if passcodes.all? { |passcode| passcode.empty? }
      break
    end
  end

  answer.join ""
end

puts analyze(File.read("txt/p079").split.uniq)
