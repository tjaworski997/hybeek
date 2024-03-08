# Hybeek ![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)

Hybrid data search engine

[<img src="./res/images/logo.png" width="75" />](image.png)

### Description:

In our applications, we often face the need to deliver users with data they want and need. I often struggle with quickly
reaching a single entry,
remembering only the context, sometimes a word. I have decided to tackle the task of preparing a universal search engine
that can operate on data from any application,
providing the ability to search for data based on both their semantics and content.

I want to base the solution on three open-source engines:

    Qdrant - vector search engine
    Elasticsearch - text search engine
    Postgres - database engine

For generating text vectors, I want to use open-source language models.

### Todo:

    [X] qdrant - installation
    [X] implementing creation of text vector representation using open-source language models
    [X] importing data from files
    [X] verification of search, checking if the results are satisfactory
    [X] deciding whether it's worth developing the project:-)
    [X] postgres - data writing service
    [ ] qdrant - data writing service
    [ ] postgres - full-text search recognition for postgres
    [ ] API
    [ ] handling semantic queries using qdrant
    [ ] elasticsearch - installation
    [ ] elasticsearch - integration



