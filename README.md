!! only works with files that are executed with the python command!!



example:
on: [push]

jobs:
  profiler-job:
    runs-on: ubuntu-latest
    name: profiler job
    steps:
      - uses: actions/checkout@v3
      - name: Profiler action step
        id: profile
        uses: pdettmann/ammonite-profiler@main
        with:
          entry_file: <entry file>
          api_key: <api_key as github secret>
