from indeed import get_last_page, extract_job
import json

last_indeed_page = get_last_page()

indeed_jobs = extract_job(last_indeed_page)

f = open("F:/VSCODE_STUDY/nomadcoders_python/2_Building_a_job_scrapper/indeed_result.json", 'w')  # 쓰기 모드로 파일 열기
f.write(json.dumps(indeed_jobs, indent=4, sort_keys=True))
f.close()
