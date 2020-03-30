import os

originalLog = 'result.log'
parsedLog = 'record.txt'
num = 999

with open(originalLog, "r", encoding='UTF-8') as origin:
  with open(parsedLog, "r", encoding='UTF-8') as parsed:
      with open("./IDblks.log", "w", encoding='UTF-8') as blks:
        originLines = origin.readlines()
        parsedLines = parsed.readlines()
        blkNum = originLines[0].split('blk')[1].split()[0]
        #print(blkNum)
        for line in range(num):
          #print(line)
          if (line != 0):
            curblkNum = originLines[line].split('blk')[1].split()[0]
            #print(originLines[line])
            if (blkNum != curblkNum):
              print(line)
              print(blkNum)
              print(curblkNum)
              blks.writelines('\n')
              blkNum = curblkNum
          ID = parsedLines[line].split(',')[1][-3:-1]
          blks.writelines(ID + ' ')
blks.close()
parsed.close()
origin.close()
      
