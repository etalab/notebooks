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
