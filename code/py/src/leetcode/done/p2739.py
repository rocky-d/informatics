from rockyutil.leetcode import *


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return 10 * (mainTank + min(additionalTank, ceil((mainTank - 4) / 4)))

#        (main+x)//5 = x
#     0 < (main+x)-5*x <= 4
#     0 <   main-4*x   <= 4
#   4*x <     main     <= 4+4*x
# 4*x-4 <    main-4    <= 4*x
#   x-1 <  (main-4)/4  <= x
