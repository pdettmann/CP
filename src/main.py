import os
from utils.util import run_profiler, send_data

def main():
    try:
        api_key = os.environ.get('INPUT_API_KEY')
        entry_file = os.environ.get('INPUT_ENTRY_FILE')

        profile_data = run_profiler("/github/workspace/" + entry_file)
        send_data(profile_data, api_key)
    except:
        raise SystemExit

if __name__ == "__main__":
    main()
