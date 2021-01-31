# README.md
- Location ceres-v2-test-suites/milestone-03/spc/ec2
- Some notes, documentation, and help for https://github.com/cloud-pi/ceres-v2-test-suites

## Environment
- `bash` scripts for components (ansible, terraform) use vars set in `.envrc`
  - Example: `AWS_DEFAULT_REGION="eu-central-1"` is used in 
- Some vars aren't defined so I think these should be should be set manually before sourcing `.envrc`

## BASH
Some notes about "new-to-me" things

### set option `pipefail`
`set -o pipefail` This setting prevents errors in a pipeline from being masked.
If any command in a pipeline fails, that return code will be used as the return code of the whole pipeline.
By default, the pipeline's return code is that of the last command - even if it succeeds.


# tax
