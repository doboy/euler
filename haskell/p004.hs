isNumPalindrome    :: Integer -> Bool
isNumPalindrome w  = (reverse (show w)) == show w

nums = [100..999]
palindromes = filter isNumPalindrome [a * b | a <- nums, b <- nums]

main =
     putStrLn $ show $ maximum palindromes
