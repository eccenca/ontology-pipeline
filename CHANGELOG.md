# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

TODO: add at least one Added, Changed, Deprecated, Removed, Fixed or Security section

### Add

### Fixed

- Fix `task test` to also have a default project name
- Fix `init.defaultBranch` configuration in `task test`
- Fix user and email variables for `task test`

### Changed

## [0.2.1] 2024-02-14

### Add

- Update README, add some development instructions

### Fixed

- Fix typo in questions
- Remove trailing hash from vocabulary documentation file base name
- Add trailing slash to default instances graph
- Fix behaviour to latest copier version by calling `copier copy …`

## [0.2.0] 2023-01-31

### Fixed

- Remove whitespace
- Improve documentation in README and README template
- Skip deployment of shapes if shapes are disabled

### Changed

- Rename `CMEMC_PARAMS` to `CMEMC_DOCKER_PARAMS`

## [0.1.4] 2023-01-25

### Add

- Add a trouble shooting section to the `README`
- Add shields to the `README`
- Clarify setup process in the `README`
- Add `.gitignore` file to the template

### Fixed

- Ensure prefixes are terminated by a colon `:`
- Fix conditional execution of cmemc_env_overwrite
- Fix conditional prompt for instances file
- Don't put two todos on one line in the `README` template

### Changed

- Move the template repository to https://github.com/eccenca/ontology-pipeline-template

## [0.1.3] 2023-01-18

### Changed

- Remove shape generation containers per default

## [0.1.2] 2023-01-11

### Add

- Add list of generated artifacts to the `README` template

## [0.1.1] 2023-01-11

### Changed

- Add documentation to the `cmemc_env_overwrite.py` script
- Rename `cmem_id` to `cmemc_config_id`
- Update `README` template, clarify `.gitignore` and requirements
- Update `README`, add TODOs and requirements

## [0.1.0] 2023-01-10

### Fixed

- Fix file names for graph files in `README`

### Changed

- Update `CHANGELOG`
- Quote git username in env file

## [0.0.5] 2023-01-10

### Fixed

- Set rdfunit test file volumes for docker with absolute paths

## [0.0.4] 2023-01-10

### Fixed

- Set cmemc config file volumes for docker with absolute paths

## [0.0.3] 2023-01-10

### Fixed

- Set the `cmem_id` key correctly

## [0.0.2] 2023-01-10

### Add

- A tool to overwrite the `cmemc.ini` with values from the environment

## [0.0.1] 2023-01-10

### Add

- The whole pipeline

## [0.0.0] 2022-11-14

### Add

- `CHANGELOG` ;-)
- Setup the project
