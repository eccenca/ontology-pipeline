# Ontology Pipeline

## Requirements
- [docker](https://www.docker.com/), [podman](https://podman.io/), or a compatible container engine
- [task](https://taskfile.dev/)
- [copier](https://copier.readthedocs.io/)

## How to use

Go to an existing ontology repository or create a new one.
Execute

```
copier ssh://git@gitlab.eccenca.com:8101/devops/ontology-pipeline.git .
```

Answer the questions.
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
