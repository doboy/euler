from utils import balls_and_bins

" Increasing numbers + Decreasing numbers - Steady numbers "
print sum( balls_and_bins( balls=digits, bins=9 ) +
           balls_and_bins( balls=digits, bins=10 ) - 10
           for digits in xrange( 1, 101 ) )
