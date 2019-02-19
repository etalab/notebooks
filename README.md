## Workflow

### Exécution ponctuelle

- git -> papermill -> [s3, commuter]

### Exécutions cycliques

- `./dags/` contient la description des graphes d'exécution qui seront fourni à une instance [airflow](https://airflow.apache.org)
- accès à l'instance airflow avec un tunnel ssh

## Bonnes pratiques

### Synchroniser les notebooks sans leurs sorties

https://github.com/kynan/nbstripout

```
$ pip install --upgrade nbstripout
$ nbstripout --install
```

`enum34` peut poser problème. Dans quel cas :

```
$ pip uninstall enum34
```

### Diff lisibles

https://nbdime.readthedocs.io

```
$ pip install nbdime
$ nbdime config-git --enable
```
