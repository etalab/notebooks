# Export PDF des données de https://aides-entreprises.data.gouv.fr/

## Install

### Python dependencies

```
pip install -r requirements.txt
```

### LaTeX + XeTeX

cf https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex

On Mac OS:

```
brew cask install mactex
# add binaries to path (add to shell.rc)
eval "$(/usr/libexec/path_helper)"
```

### Pandoc

Required by nbconvert to convert markdown to PDF.

On Mac OS:

```
brew install pandoc
```

### Orca

Required by plotly to export graphs as images (could be avoided if using matplotlib I guess).

On Mac OS:

```
brew cask install orca
```

Then launch Orca.app, it will install the binary in the PATH.

## Run

```
jupyter nbconvert aides-entreprises.ipynb --to pdf --no-input
```