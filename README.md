# ammonite-profiler

Ammonite-profiler is a GitHub action to benchmark your Python code.

## Requirements
* Python3
* The part of your project you would like to benchmark must be run using the python3 command (no frameworks like flask etc.).

## Inputs
* `entry-file` **(required)** is the file that you use to run your Python project with the `python3` command.
* `api_key` is the API key for your project registered on the [ammonite profiler website]. Please add this in your repository GitHub secrets.

## Example Usage

```yml
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
            entry_file: <your entry file>
            api_key: ${{ github.API_KEY }} # add in GitHub Secrets
```

You can check out an example repository using this action [here].

[ammonite profiler website]: <https://ammonite-profiler.xyz>
[here]: <https://github.com/pdettmann/python_test_app>
