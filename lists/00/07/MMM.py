def mean(values):
    return sum(values)/len(values)


def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0


def mode(thelist):
  counts = {}
  for item in thelist:
    counts[item] = counts.get(item, 0) + 1
  maxcount = 0
  maxitem = None
  for k, v in counts.items():
    if v > maxcount:
      maxitem = k
      maxcount = v
  if maxcount == 1:
    print "All values only appear once"
  elif counts.values().count(maxcount) > 1:
    print "List has multiple modes"
  else:
    print "Mode of list:", maxitem
