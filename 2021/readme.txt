!!! use CIRCMATRIXGENERATOR.html , from this folder 2021, it much faster, less lags/freeze cpu chance. 10000 easy, plus stuff changed, to better template.
2021 folder VERSION CHANGED DEFAULT INDICES, to new names

!!! use wxm , because maxima fail with wxmx, in same time wxMaxima gui work done.

general way:
- copy _ with needed namenumber
- add to each of 5 folders the batchStuff.txt, generated using CIRCMATRIXGENERATOR
- run.sh
- wait, while completed x5
- check that no holes and last indices is correct, or manually drop failed matrices , and continue again, with nomer: beginned matrix number
- when all completed, run max.py to calculate maximum value closer to pi


use terminal way from wxm level:
- maxima --very-quiet --batch=runme.wxm
or this
- terminal "maxima"
- batch("file.wxm");
or will fail output size etc after 500+ matrix, etc.


-matrix prepared using *CIRCMATRIXGENERATOR.html generator

-summary present 3 000 000+ unique matrices with last scheme

... recalculation of all possible matrices


next idea, possibly for 3d inside sphere, but sphere can be remastered from 2d  3 4 5 sphere primitives

`using-python` folder is trying produce solid flow, without preparing before every partion of calculation.  
Much slower than wxMaxima, and used option `check=False` for sympy solver. Matrix indices in flow python3 vs wxMaxima now looks different. But python code looks more clear.