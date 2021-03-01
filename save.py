import csv

def save_to_file(jobs):
  file=open("jobs.csv",mode="w")
  write=csv.writer(file)
  write.writerow(["title","company"])
  print(jobs)
  return