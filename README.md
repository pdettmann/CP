!! only works with files that are executed with the python command!!

insert path to main file
run cprofile command
add language argument to API key
add personalised API key.
export cprofile data to API

example:
inputs:
  file-path:  # id of input
    description: 'Enter the path to your main file'
    required: true
    default: './main.py'
  api-key:
    description: 'Enter your ammonite-profiler apiKey'
    required: true

outputs:
  profile: # id of output
    description: 'Profile of your application'

runs:
  using: "composite"
  steps:
    - run:
      shell: python
