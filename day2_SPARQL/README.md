# Information

These are the solutions to the exercises [proposed for day 2](https://github.com/cursosLabra/semWebKGs/raw/main/slides/25_Exercises_SPARQL.pdf)

The first step is to merge the Turtle files. We used Apache Jena's command line tool [turtle](https://jena.apache.org/documentation/tools/) with the following command inside the day_1 folder:

```
turtle --output turtle e2.ttl e3.ttl e4.ttl e5.ttl e6.ttl > merged.ttl
```

and moved the `merged.ttl` file to this folder.

The SPARQL queries can be run using:

```
sparql --query query.sparql --data merged.ttl
```