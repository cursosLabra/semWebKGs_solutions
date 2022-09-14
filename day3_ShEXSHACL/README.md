# Information

These are the solutions to the exercises [proposed for day 3](https://github.com/cursosLabra/semWebKGs/raw/main/slides/35_Exercises_ShExSHACL.pdf)

The first step is to merge the Turtle files. We used Apache Jena's command line tool [turtle](https://jena.apache.org/documentation/tools/) with the following command inside the day_1 folder:

```
turtle --output turtle e2.ttl e3.ttl e4.ttl e5.ttl e6.ttl > merged.ttl
```

and moved the `merged.ttl` file to this folder.