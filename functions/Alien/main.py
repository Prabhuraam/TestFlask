import json
import zcatalyst_sdk
import logging
from flask import Request, make_response, jsonify
tableName = 'AlienCity'  
columnName = 'CityName'
def handler(request: Request):
    try:
        app = zcatalyst_sdk.initialize()
        logger = logging.getLogger()
        if request.path == "/alien" and request.method == 'POST':
            req_data = request.get_json()
            name = req_data.get('city_name')
            rowid = getAlienCountFromCatalystDataStore(name)
            if len(rowid) == 0:
                logger.info("Alien alert!")
                datastore_service = app.datastore()
                table_service = datastore_service.table(tableName)
                row_data = {
                    columnName:name
                    }
                table_service.insert_row(row_data)
                response = make_response(jsonify({
                "message": "Thanks for reporting!"
            }), 200)
            else:
                response = make_response(jsonify({
                "message": "Looks like you are not the first person to encounter aliens in this city! Someone has already reported an alien encounter here!"
            }), 200)
            return response
        elif request.path == "/alien" and request.method == 'GET':
            name = request.args.get('city_name')
            rowid = getAlienCountFromCatalystDataStore(name)
            if len(rowid) == 0:
                response = make_response({
                    "message": "Hurray! No alien encounters in this city yet!",
                    "signal": "negative"
                }, 200)
            else:
                response = make_response(jsonify({
                "message":  "Uh oh! Looks like there are aliens in this city!",
                "signal": "positive"
            }), 200)
            return response    
        else:
            response = make_response("Error. Invalid Request")
            response.status_code = 404
            return response
    except Exception as err:
        logger.error(f"Exception in AlienCityAIO :{err}")
        response.status_code = 404
        return response
def getAlienCountFromCatalystDataStore(cityname):
        app = zcatalyst_sdk.initialize()   
        zcql_service = app.zcql()
        query = f"SELECT * FROM {tableName} WHERE {columnName} = {cityname}"
        output = zcql_service.execute_query(query)
        return output