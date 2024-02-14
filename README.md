# Ontology Pipeline

[![version][version-shield]][changelog] [![copier][copier-shield]][copier] [![eccenca Corporate Memory][cmem-shield]][cmem]

## Requirements

To initialize an ontology repository with the ontology pipeline and update it you need:
- [Copier](https://copier.readthedocs.io/) (minimum 6.0.0, better use 7.0.1 or higher; runs on Python 3)

To execute the ontology pipeline you need:
- [Task](https://taskfile.dev/)
- [Docker](https://www.docker.com/), [Podman](https://podman.io/), or a compatible container engine
- [Python 3](https://www.python.org/)

## How to use

1. Go to an existing git repository with your ontology or simply create a new git repository (e.g. `git init my-ontology`).

2. In the ontology repository execute:

```
copier copy gh:eccenca/ontology-pipeline-template .
```

3. Answer the questions.

Copier will overwrite your `README.md` if you had one already. Adjust the `README.md` according to your needs. Make sure to go through the `TODO` section.
Add all of the newly created files to the repository and push it.
You can now execute the ontology pipeline:

- `task ci` - to execute the continuous integration
- `task ci cd` - to execute the continuous integration and continuous delivery
- `task update` - to update the ontology pipeline, it will ask all questions again but they are already entered with your previous answers. (Make sure to perform a `task dist-clean` and commit all changes on the repository before an update.)
- `task clean` - remove temporary files, that are created during a pipeline run
- `task dist-clean` - the same as `task clean` + also removing the generated artifacts

If you have selected a CI option, your CI should execute the ontology pipeline.

## What it does

Basically it fetches your ontology from cmem, commits it to the repo, does some steps on it, commits the results and then imports the resulting ontology to cmem again.


## Configuration and Customization

The execution of the ontology pipeline can be further configured by queries and variables.

### Queries
In the directory `resources/queries/` you can add files with [SPARQL 1.1 Construct](https://www.w3.org/TR/sparql11-query/#construct) queries to extract data from your cmem instance during the run.

### Variables

Many variables are already set with the values you have given to copier in the `.copier-answers.env` file.
Don't edit this file since it might be overwritten when running `copier update` resp. `task update`.
To overwrite variable or set additional variables create a file `.env` in the root of the repository.

| Variable Name         | Step              | Description                                                                    | Default                        |
|-----------------------|-------------------|--------------------------------------------------------------------------------|--------------------------------|
| `GIT_PUSH`            | cd                | If it is not `False` a `git push` will be executed at the end of the `cd` task | `True` |
| `CMEMC_DOCKER_PARAMS` | shape_generation  | Configure additional docker parameters for the execution of cmemc              | `-v $PWD/cmemc.ini:/cmemc.ini` |


## Trouble shooting

### Migrate from a different template remote

Open your `.copier-answers.yml` and change the current `_src_path` to `_src_path: gh:eccenca/ontology-pipeline-template`.

### Connect to a local CMEM orchestration

If you are running your CMEM orchestration locally you need to connect cmemc to the docker/podman network of your orchestration.
To achieve that create a file called `.env` in your repository.
In it define the variable `CMEMC_DOCKER_PARAMS="-v $PWD/cmemc.ini:/cmemc.ini --network conmtainer:<container_id>"`, where `<container_id>` is the container id of the apache2 container in your cmem orchestration.

## Development Setup

To get a development setup you need to checkout this `ontology-pipeline-template` repository and create a second repository with an ontology using the copier template.
To initialize your ontology repository with your build environment run.
```
copier copy --vcs-ref HEAD path/to/template/repository path/to/ontology/repository
```

To simply switch your ontology repository to the latest development state of this repository run

```
copier copy --vcs-ref main update
# or
copier copy --vcs-ref HEAD update
```

To switch the remote template repository check out [Trouble shooting](#trouble-shooting) > [Migrate from a different template remote](#migrate-from-a-different-template-remote).

## TODO
- Initial generation of turtle files
- How to deal with `.gitignore` and similar files updated and used by multiple tools
- Resolve prefixes entered during copier run (is this possible with copier?)
- Shape generation
  - get combined ontology/ontology with all imports
  - shapes from ontology
  - shapes from instances
- Shape documentation
- Ontology Visualization
- Entity Map
- Analyze Shapes and Ontology
  - overlapping terms
- Integrate workflow for contribution to the ontology via the repository as well
- Support multiple cmem instances to sync to. (Maybe this should be the task of something like github action environment, maybe it should be independent of github, …)

## Out if Scope
- Get DI projects

[version-shield]: https://img.shields.io/github/v/tag/eccenca/ontology-pipeline-template?label=version&sort=semver
[changelog]: https://github.com/eccenca/ontology-pipeline-template/blob/main/CHANGELOG.md
[github-actions]: https://github.com/eccenca/ontology-pipeline-template/actions
[build-shield]: https://github.com/eccenca/ontology-pipeline-template/actions/workflows/check.yml/badge.svg
[copier]: https://copier.readthedocs.io/
[copier-shield]: https://img.shields.io/badge/made%20with-copier-orange
[cmem]: https://documentation.eccenca.com
[cmem-shield]: https://img.shields.io/badge/made%20for-Corporate%20Memory-blue
