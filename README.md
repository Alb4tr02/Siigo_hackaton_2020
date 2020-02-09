# Siigo_hackaton_2020
Para poder crear un objeto en alguna de las tablas se debe hacer de la siguiente manera (debido a las foreign keys):
crear_ac_tenant -> crear_customer -> crear_ac_invoices -> crear_ac_products -> crear_ac_invoice_items

Para utilizar la api con curl se debe hacer de la siguiente manera:
## Lista toda la tabla escogida
curl *:5000/api/v1/table_name
## Lista un id especifico en una tabla designada
curl *:5000/api/v1/table_name/id=id_especifico
## Crea un nuevo registro en una tabla
curl -d "param1=val1&param2=val2&..." -H "Content-Type: application/x-www-form-urlencoded" -X POST http://localhost:5000/api/v1/table_name
## Borrar una fila en una tabla determinada
curl -X DELETE *:5000/api/v1/<table_name>/id=<id>

## Actualizar parametros escogidos en un id y tabla especificos
curl -d "param1=val1&param2=val2&..." -H "Content-Type: application/x-www-form-urlencoded" -X PUT  *:5000/api/v1/<table_name>/id=<id>