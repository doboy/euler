-- WIP

-- smallestMultiple :: Integer -> Integer
-- smallestMultiple n = smallestMultiple' n 2 1

-- smallestMultiple' :: Integer -> Integer -> Integer -> Integer
-- smallestMultiple' n iter curr
--   | ((n == iter) && ((mod curr iter) == 0)) = curr
--   | ((n == iter) && ((mod curr iter) /= 0)) = curr * iter
--   | ((mod curr iter) == 0)                  = smallestMultiple' n (iter + 1) curr
--   | otherwise                               = smallestMultiple' n (iter + 1) (curr * iter)

-- main =
--      putStrLn $ show $ smallestMultiple 10
main = putStrLn $ show $ 10