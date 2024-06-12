from flask import request

def status():
    return {
        'message': 'I am alive'
        }, 200

def income_tax(country: str):
    if country != 'UK':
        return {'message': 'country not supported!'}, 400
    income_range =[
        ['Personal allowance',	0, 12570, 0],
        ['Starting rate for savings',	12571, 17570, 0],
        ['Basic rate', 	12571, 50270,	20],
        ['Higher rate',	50271, 125140,	40],
        ['Additional rate', 125140, 999999999, 45]]
    json_req = request.json
    if (json_req['currency'] != 'eur' and
        json_req['currency'] != 'EUR'):
        return {'message': 'currency not supported!'}, 400
    for ir in income_range:
        if(json_req['income'] >= ir[1] and
           json_req['income'] <= ir[2]):
            return {'message': ir[0], 'tax_rate': ir[3]}, 200
    return {'message': 'income value out of bounds'}, 400
           
    
