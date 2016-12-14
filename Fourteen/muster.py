from collections import defaultdict
from hashlib     import md5


def main():

   data = "yjdafjpo"


   idx = 0

   hashes = []
   threes = defaultdict(list)

   while not (len(hashes) > 64 and (idx - hashes[-1][0]) > 1000):
      value = md5("%s%s" % (data, idx)).hexdigest()
      for _ in xrange(2016):
         value = md5(value).hexdigest()

      match = matchesFive(value)

      if match is not None:
         for (m_idx, value) in threes[match]:
            if (idx - m_idx) <= 1000:
               hashes.append((m_idx, value))
               print "Found hash:", m_idx
         hashes.sort()
         threes[match] = []

      match = matchesThree(value)

      if match is not None:
         threes[match].append((idx, value))

      idx += 1

   print len(hashes)
   print "Last hash:", hashes[63]



def matchesThree(value):
   for idx in xrange(len(value) - 2):
      if len({value[idx + i] for i in xrange(3)}) == 1:
         return value[idx]
   return None

def matchesFive(value):
   for idx in xrange(len(value) - 4):
      if len({value[idx + i] for i in xrange(5)}) == 1:
         return value[idx]
   return None


if __name__ == "__main__":
   main()