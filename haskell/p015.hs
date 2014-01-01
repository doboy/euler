import Control.Monad.State
import qualified Data.Map as M

ways :: Integer -> Integer -> State (M.Map (Integer, Integer) Integer) Integer
ways w h = do
    hash <- get
    if M.member (w, h) hash
        then return (hash M.! (w, h))
        else do
             if (w == 1 || h == 1)
                 then return 1
             else do val_1 <- (ways w (h - 1))
                     val_2 <- (ways (w - 1) h)
                     let val = val_1 + val_2
                     modify (M.insert (w, h) val)
                     return val

main = putStrLn $ show $ evalState (ways 21 21) M.empty