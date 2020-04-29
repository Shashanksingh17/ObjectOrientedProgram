import json

# a Python object (dict):
Rices = {
  "properties name": "vashmati",
  "weight": 30,
  "price": "100"
}

Pulces = {
  "properties name": "Arhar",
  "weight":50,
  "price": "90",
}
Wheats = {
  "properties name": "patanjali",
  "weight": 20,
  "price": "120",
}

rice= json.dumps(Rices)
pulces=json.dumps(Pulces)
wheats=json.dumps(Wheats)
print(rice)
print(pulces)
print(wheats)