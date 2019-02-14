"""
Complexity Project 2018/19.
R.K. Kamath
01209729
rkk216@ic.ac.uk
"""
import numpy as np  #some obvious imports
import matplotlib.pyplot as plt


class aval:

    """
    Initialise a system with a length L
    """

    def __init__(self, length):
        self.z = np.zeros(length)
        #self.zthresh = np.ones(length)
        self.zthresh = np.random.randint(1,2,size = length)
        self.crossover = False
        self.height = np.sum(self.z)
        self.s = []


    def zval(self):
        """Returns the slope values for every element in the array"""
        return (self.z)

    def zthreshval(self):
        """"Returns the threshold slope values for every element in the array"""
        return self.zthresh

    def drive(self):
        """ Adds one grain to the leftmost part of the sandpile"""
        self.z[0] = self.z[0] + 1
        self.height = self.height + 1
        return

    def relax(self, p = 0.5):
        """ Frankie says grain drops if the slope is greater than the threshold slope"""
        i = 0
        j = 0
        crossover = False
        while i < np.size(self.z):
            if self.z[i] > self.zthresh[i]:
                self.zthresh[i] = np.random.choice([1,2],1, [p,1-p])
                j = j + 1
                if i == 0: #If you're on the leftmost part
                    self.z[i] = self.z[i] - 2
                    self.z[i + 1] = self.z[i + 1] + 1
                    self.height = self.height - 1
                elif i == np.size(self.z) - 1: #if you're on the rightmost part
                    self.z[i] = self.z[i] - 1
                    self.z[i - 1] = self.z[i - 1] + 1
                    self.crossover = True
                    i = i - 1 #checks the one immidiately before because a relaxation changes the slope
                else: #if you're malcolm in the middle
                    self.z[i + 1] = self.z[i + 1] + 1
                    self.z[i] = self.z[i] - 2
                    self.z[i - 1] = self.z[i - 1] + 1
                    i = i - 1
            else:
                i = i + 1 #done

        if self.crossover == True:
            self.s.append(j)
        return

    def checkrelax(self):
        """ Just in case you don't believe my code."""
        for i in range(np.size(self.z)):
            if self.z[i] > self.zthresh[i]:
                print("oops")
        return

    def add(self, p = 0.5):
        """ Add one grain, and then relax the system, check if it's relaxed."""
        self.drive()
        self.relax(p)
        self.checkrelax()
        return

    def heightarray(self):
        """ Finds the height of each pile in the array"""
        heightarray = np.zeros(np.size(self.z))
        heightarray[0] = self.height
        for i in range(1,np.size(self.z)):
            heightarray[i] = heightarray[i-1] - self.z[i-1]
        return heightarray

def sandpile(avalsize,grains,p = 0.5):

    """ Plots a bar graph of the actual sandpile"""

    aval1 = aval(avalsize)
    for i in range(grains):
        aval1.add(p)
        plt.bar(range(np.size(aval1.heightarray())), aval1.heightarray())
        plt.ylim(0,10)
        plt.show()
    return

def avalheight(t, L):
    """ Plots the height of the array as a function of grains (or time) and crossover time"""
    aval1 = aval(L)
    heightarray = []
    tcross = 0
    checker = False
    for i in range(t):
        aval1.add()
        heightarray.append(aval1.height)
        if aval1.crossover == True and checker == False:
            tcross = i
            checker = True
    return [heightarray, tcross]


def meanz(t, L):
    aval1 = aval(L)
    zarray = []
    tcross = 0
    checker = False
    for i in range(t):
        print(i)
        #print(L)
        aval1.add()
        if aval1.crossover == True:
            for i in aval1.z:
                zarray.append(i)
    zmean =  np.average(zarray)
    zstddv = np.std(zarray)
    return [zmean,zstddv]
    
    
    
def smoothheight(t, L, M):
    A = avalheight(t,L)
    height1 = A[0]
    tcross = [A[1]]
    for i in range(M - 1):
        height1 = np.add(height1, avalheight(t,L)[0])
        tcross.append(avalheight(t, L)[1])
    return ([(height1/M),np.average(tcross)])

def heightextractor(heightarray,tcross):
    tcrossint = np.int(tcross)
    A = heightarray[tcrossint:]
    print(np.average(A))
    print(np.std(A))
    return

def stableheightarray(heightarray,tcross):
    tcrossint = np.int(tcross)
    A = heightarray[tcrossint:]
    return A

def avalsize(t,L):
    aval1 = aval(L)
    heightarray = []
    tcross = 0
    checker = False
    for i in range(t):
        print(i)
        aval1.add()
    return aval1.s



"""

             .--.            .--.
            ( (`\\."--``--".//`) )
             '-.   __   __    .-'
              /   /__\ /__\   \
             |    \ 0/ \ 0/    |
             \     `/   \`     /
              `-.  /-" "-\  .-`           ._-.
                /  '.___.'  \            //';\\
                \     I     /           //  ;//
                 `;--'`'--;`            \\_;//
                   '.___.'               //-`
                  ___| |___           ."`-.
               .-`  .---.  `-.       /     )
              /   .'     '.   \     /      )
             /  /||       ||\  \   /  /`""`
            /  / ||       || \  \ /  /
           /  /  ||       ||  \  /  /
          /  (___||___.-=--.   \   /
         (                -;    '-' 
          `-----------.___~;
                 ||       ||
                 ||       ||
                 ||       ||
                 ||       ||
                 ||       ||
                 |'.     .'|
                 ;  `'--`  (
(`-.            /           \
 '-.`\         /  ,  .-'"`\  \
    \ \       / /^|  |     \  \
     | |     / /  |  |      \  \
     | |    / /   |  |       \  \
     | |   | |    |  |       /  /
      \ \  | |    |  |     /` /`
       \ \ | |    |  |   /` /`
       | | \ \    |  | /` /`
       | |  \ \   |  /` /`
       | |   | |  |/` /`
       \ \   / /_/` /|
        \ `-` /`    ||
         '--'`|     ||
              |     \'--------.
              |  \ \ \     \ \ \
               \__\_\_\----'-'-'

"""