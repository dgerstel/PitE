#!/usr/bin/env python

class AppMgr(object):
  class InputReader(object):
    def __init__(self, fname):
      ''' reads `fname` assuming formating:
          a1 b1 c1
          a2 b2 c2
          where the last column is a free terms vector
      '''
      with open(str(fname)) as f:
        data = f.readlines()
      AppMgr.params = [row.split() for row in data]
      print AppMgr.params

  class InputValidator(object):
    def __init__(self):
      def is_number(s):
        try:
          float(s)
          return True
        except ValueError:
          print "[LOG] At least one of input terms is not a number!!!\n"
          exit()

      AppMgr.params = [[float(elem) if is_number(elem) else None for elem in row] for row in AppMgr.params]
      print AppMgr.params

  class Solver(object):
    def calcDeter(self):
      ''' temporararily assumes 2nd order linear eq. system ONLY 
      '''
      return AppMgr.params[0][0] * AppMgr.params[1][1] - \
             AppMgr.params[0][1] * AppMgr.params[1][0]

    def calcDeterX(self):
      ''' temporararily assumes 2nd order linear eq. system ONLY 
      '''
      return AppMgr.params[0][2] * AppMgr.params[1][1] - \
             AppMgr.params[0][1] * AppMgr.params[1][2]

    def calcDeterY(self):
      ''' temporararily assumes 2nd order linear eq. system ONLY 
      '''
      return AppMgr.params[0][0] * AppMgr.params[1][2] - \
             AppMgr.params[1][0] * AppMgr.params[0][2]

  
    def printResult(self):
      print AppMgr.solMsg
      if AppMgr.sol[0] is not None:
        print AppMgr.sol


    def __init__(self):
      D = self.calcDeter()
      Dx = self.calcDeterX()
      if not D: # either inconsistent or indeterminate
        if not Dx:
          AppMgr.sol = [None, None]
          AppMgr.solMsg = "The system of eqs. is indeterminate"
        else:
          AppMgr.sol = [None, None]
          AppMgr.solMsg = "The system of eqs. is inconsistent"
      else:
        AppMgr.sol = [Dx / D, self.calcDeterY() / D ]
        AppMgr.solMsg = "The solution is:"

      self.printResult()
    

  def __init__(self, DataFile):
    self.DataFile = DataFile
    AppMgr.InputReader(self.DataFile)
    AppMgr.InputValidator()
    AppMgr.Solver()


appMgr = AppMgr("input.txt")
