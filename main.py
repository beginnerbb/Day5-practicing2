
from indeed import extract_indeed_pages, extract_indeed_jobs
from save import save_to_file

a=extract_indeed_pages()

jobs=extract_indeed_jobs(a)

save_to_file(jobs)