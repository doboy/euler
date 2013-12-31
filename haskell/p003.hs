primeFactors   :: Integer -> [Integer]
primeFactors n = primeFactors' n 2

primeFactors'        :: Integer -> Integer -> [Integer]
primeFactors' 1 _    = []
primeFactors' n iter
         | (iter * iter > n)    = [n]
         | ((mod n iter) == 0)  = iter : (primeFactors' (quot n (iter * (timesDivides n iter))) (iter+1))
         | otherwise            = primeFactors' n (iter+1)

timesDivides :: Integer -> Integer -> Integer
timesDivides n a
         | ((mod n a) == 0) = 1 + (timesDivides (quot n a) a)
         | otherwise        = 0

main =
     putStr $ show $ last $ primeFactors 600851475143
