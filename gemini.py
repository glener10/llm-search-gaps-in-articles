from dotenv import load_dotenv
import datetime

from common.pdf import read_pdf

start_time = datetime.datetime.now()
load_dotenv()

print(f"🚀 Starting process at {start_time}")

end_time = datetime.datetime.now()
total_time = end_time - start_time
print(f"⏱️ execution finished. Total time: {total_time}")
