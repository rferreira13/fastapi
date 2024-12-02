# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.


:snake: 

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


```{.py3 hl_lines="1-3" linenums="55" title="arquivo.py"}
def xpto():
    """
    Docstring
    """
    return True
```
## Custom fences
```mermaid
flowchart LR
    A --o B
    B --x C
```


```mermaid
classDiagram
    teste <|-- outro
```

```mermaid
classDiagram
    Pessoa <|-- Eduardo
    class Pessoa{
        +String nome
        +Int idade
        +metodo(self): bool
    }
    class Eduardo{
        
    }
```