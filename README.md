# Ontology Pipeline

## Requirements
- [docker](https://www.docker.com/), [podman](https://podman.io/), or a compatible container engine
- [task](https://taskfile.dev/)
- [copier](https://copier.readthedocs.io/)

## How to use

Go to an existing ontology repository or create a new one.
Execute

```
copier copy ssh://git@gitlab.eccenca.com:8101/devops/ontology-pipeline.git .
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


## TODO
- Shape generation
  - get combined ontology/ontology with all imports
  - shapes from ontology
  - shapes from instances
- Shape documentation
- Ontology Visualization
- Entity Map
- Analyze Shapes and Ontology
  - overlapping terms

## Out if Scope
- Get DI projects
