#!/usr/bin/env bash
for j in `seq 1 1 100`
do
    curl -d "id=$j&name=nata$j" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://localhost:5000/api/v1/ac_tenant
done
for i in `seq 1 1 600`
do
    curl -d "id=$i&tenant_id=2&name=papas_saladas&description=lol probando probando 123&list_price=1234.5" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://localhost:5000/api/v1/ac_products
done
