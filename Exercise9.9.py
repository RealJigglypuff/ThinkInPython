'''
Here’s another Car Talk Puzzler you can solve with a search (http://www.cartalk.com/content/puzzlers):
“Recently I had a visit with my mom and we realized that the two digits
that make up my age when reversed resulted in her age. For example, if she’s 73, I’m 37.
We wondered how often this has happened over the years but we got
sidetracked with other topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been
reversible six times so far. I also figured out that if we’re lucky
it would happen again in a few years, and if we’re really lucky it would
happen one more time after that. In other words, it would have happened 8
times over all. So the question is, how old am I now?”
Write a Python program that searches for solutions to this Puzzler.
Hint: you might find the string method zfill useful.
'''

def reversible() :
    count = 0
    save = ''
    for diff in range(10, 70):
        for baby in range(0, 90):
            if str(baby + diff) == str(baby).zfill(len(str(baby + diff)))[::-1]:
                count += 1
                print baby, baby+diff, count
                if count == 6 :
                    save = str(baby + diff) + str(diff)
            if count == 8 :
                print 'The current mother age is : ', int(save[:2])
                print 'The current daughter/son age is : ', int(save[:2]) - int(save[2:])
                return
        count = 0


import time
start = time.time()
reversible()
end = time.time()
print(end - start)

'''
This is the book's solution : http://www.greenteapress.com/thinkpython/code/cartalk3.py
And after measuring the performance I found my code is more efficient
'''