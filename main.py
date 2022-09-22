
def count_batteries_by_usage(cycles):
  #create variables to count for low,mid and high and use simple if else to traverse list and get the count by increment
  countLow=0
  countMedium=0
  countHigh=0
  #another testcase can be to check if the list passed is empty if so return "pass valid cycles"
  for i in cycles:
    if i<=410:
      countLow+=1
    elif i>410 and i<=909:
      countMedium+=1
    elif i>909:
      countHigh+=1
  return {
    "lowCount": countLow,
    "mediumCount": countMedium,
    "highCount": countHigh
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  counts1 = counts_batteries_by_usage([0,101,410,10000,800]) #new test case
  #use assert of to check if the count is correct and print counts1
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print(counts)
  print(counts1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
