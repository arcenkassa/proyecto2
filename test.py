

diccionario={"nombre":{},
            "apellido":"apellido1"
}
value1= diccionario.get("apellido","")
value2=diccionario.get("nombre",value1)

print(value2)