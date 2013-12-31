fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

main =
     putStrLn $ show $ sum $ filter even $ takeWhile (\x -> x < 4000000) fibs
