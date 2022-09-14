from SPARQLWrapper import SPARQLWrapper, JSON
import requests
import sys
import flask
import json
import json2html

app = flask.Flask(__name__)
app.config["DEBUG"] = True

sparql_service_url="http://localhost:3030/testing/sparql"

sparql_query="""
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix ex: <http://www.example.org/>
prefix voc: <http://www.example.org/voc/>
prefix schema: <https://schema.org/>
prefix wiki: <http://www.wikidata.org/entity/>
prefix wdt: <http://www.wikidata.org/prop/direct/>

Select distinct ?player ?value ?wiki ?place_of_birth ?country_name where {
	?observation voc:footballPlayer ?player ;
		schema:measuredValue ?value ;
		voc:wikidataitem ?wiki .

	optional {
		Service <https://query.wikidata.org/sparql> {
			?wiki wdt:P19 ?place .
			?place rdfs:label ?place_of_birth .
			FILTER(LANG(?place_of_birth) = "en")
			?place wdt:P1376|wdt:P17 ?country .
			?country wdt:P31/wdt:P279* wiki:Q6256 .
			?country rdfs:label ?country_name .
			FILTER(LANG(?country_name) = "en")
		}
	}
}"""

sparql = SPARQLWrapper(sparql_service_url, agent="Sparql Wrapper")

@app.route('/', methods=['GET'])
def home():
	sparql.setQuery(sparql_query)
	sparql.setReturnFormat(JSON)
	sparql.setMethod("POST")

	try:
		jsonData = sparql.query().convert();
		items=[]
		for row in jsonData["results"]["bindings"]:
			item={}
			for column in jsonData['head']['vars']:
				value=row[column]
				item[column]=value['value']
			items.append(item);
		print(items)
	except:
		print("Error:", sys.exc_info()[0], file=sys.stderr)

	table = json2html.json2html.convert(json = items, table_attributes="class=\"table table-striped table-hover\"")
	response=("""
		<html>
			<head>
				<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\" crossorigin=\"anonymous\">
			</head>
			<body>"""
				+ json.dumps(items) + """
				</br></br>""" + table + """
			</body>
		</html>""")
	return response

app.run()
