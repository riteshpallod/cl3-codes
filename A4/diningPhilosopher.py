import threading
import random
import time

'''
This solution avoids deadlock by never waiting for a fork while having one in hand.
If a philosopher acquires one fork but can't acquire the second,he releases the first
fork before waiting to acquire the other (which then becomes the first fork acquired).
'''

# Dining philosophers, 5 Phillies with 5 forks. Must have two forks to eat.
# Deadlock is avoided by never waiting for a fork while holding a fork (locked)
# Procedure is to do block while waiting to get first fork, and a nonblocking
# acquire of second fork.  If failed to get second fork, release first fork,
# swap which fork is first and which is second and retry until getting both.


'''
forks are lock objects.
    locks are acquired using .acquire() and a locked lock is released using .released(). Wow.
'''

class Philosopher(threading.Thread):

    running = True

    def __init__(self, xname, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while(self.running):
            #philospher is thinking (but is really sleeping)
            time.sleep(random.uniform(3,13))
            print('%s is hungry. ' %self.name)
            self.dine()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        while self.running:
            fork1.acquire(True)
            '''
            When invoked with the blocking argument set to True (the default),
            block until the lock is unlocked, then set it to locked and return True.
            '''

            #now TRY TO acquire second lock
            locked = fork2.acquire(False)
            '''
            When invoked with the blocking argument set to False, do not block.
            If a call with blocking set to True would block, return False immediately;
            otherwise, set the lock to locked and return True.
            '''
            #so if locked is true, then we have acquired the lock! break from the loop
            #abhi jab break maarte tab we don't we execute the code from else loop
            if locked:
                break

            #we are not supposed to hold one lock while waiting for another
            fork1.release()

            print('%s swaps forks' % self.name)
            fork1, fork2 = fork2, fork1
        else:
            return

        #we have both the forks now, we have both locks now.
        self.dining()
        #we release them now
        fork2.release()
        fork1.release()

    def dining(self):
        print('%s starts eating' %self.name)
        #abhi so raha because eating. thread so raha, but apna philospher is eating. in theory
        time.sleep(random.uniform(1,10))
        print('%s fininshes eating and leaves to think. ' %self.name)


def diningPhilosphers():
    #five forks for five philos
    forks = [threading.Lock() for n in range(5)]

    philosopherNames = ('Ritesh', 'Sumire', 'Tengo', 'Kafka', 'Miu')

    philosophers = []   

    for i in range(5):
        philosophers.append(Philosopher(philosopherNames[i], forks[i%5], forks[(i+1)%5]))

    random.seed(507129)
    Philosopher.running = True

    for philosopher in philosophers:
        philosopher.start()

    #100 seconds tak karo run
    time.sleep(50)

    Philosopher.running = False
    print('done eating.')

diningPhilosphers()