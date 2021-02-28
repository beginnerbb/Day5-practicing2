
from indeed import extract_indeed_pages, extract_indeed_jobs

a=extract_indeed_pages()

indeed_jobs=extract_indeed_jobs(a)

print(indeed_jobs)
print(len(indeed_jobs))