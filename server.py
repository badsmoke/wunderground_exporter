from flask import Flask, make_response

import os
import json
import urllib.request
import time


app = Flask(__name__)


def generateMetrics():

    import json
    #check empty env vars
    if "ENV_STATION_ID" in os.environ:
        stationID=os.environ["ENV_STATION_ID"].split(',')
    else:
        stationID=["IDRESDEN521"]
    if "ENV_API_KEY" in os.environ:
        apiKey=os.environ["ENV_API_KEY"]
    else:
        apiKey="9066f4110ae4488aa6f4110ae4588a87"

    print(apiKey,stationID)

    output_list= []

    for station in stationID:
        #fetch_url="https://api.weather.com/v2/pws/observations/current?stationId="+station+"&format=json&units=m&apiKey="+apiKey+""
        fetch_url="https://api.weather.com/v2/pws/observations/current?apiKey="+apiKey+"&stationId="+station+"&format=json&numericPrecision=decimal&units=m"
        print(fetch_url)
        try:
            resp = urllib.request.urlopen(fetch_url)
        except Exception:
            print("Could not send GET request to given URL. Check url parameter!")
            exit(1)

        #check response code
        print(resp.code)
        if resp.code == "401":
            print("Invalid apiKey")
            exit(1)
        
        elif resp.code == 200:
            print("all right")
            # Successful call
        else:
            print("Web request returned unhandled HTTP status code " + str(resp.code) + ". Please open an issue at GitHub "                                                                               "with further details.")
            exit(1)

        resp_json = json.loads(resp.read().decode('utf-8'))['observations'][0]



        print(json.dumps(resp_json))
        json_dict = {     
        "observations_solarRadiation" : str(resp_json["solarRadiation"]),
        "observations_lon" : str(resp_json["lon"]),
        "observations_realtimeFrequency" : str(resp_json["realtimeFrequency"]),
        "observations_epoch" : str(resp_json["epoch"]),
        "observations_lat" : str(resp_json["lat"]),
        "observations_uv" : str(resp_json["uv"]),
        "observations_winddir" : str(resp_json["winddir"]),
        "observations_humidity" : str(resp_json["humidity"]),
        "observations_qcStatus" : str(resp_json["qcStatus"]),
        "metric_temp" : str(resp_json["metric"]["temp"]),
        "metric_heatIndex" : str(resp_json["metric"]["heatIndex"]),
        "metric_dewpt" : str(resp_json["metric"]["dewpt"]),
        "metric_windChill" : str(resp_json["metric"]["windChill"]),
        "metric_windSpeed" : str(resp_json["metric"]["windSpeed"]),
        "metric_windGust" : str(resp_json["metric"]["windGust"]),
        "metric_pressure" : str(resp_json["metric"]["pressure"]),
        "metric_precipRate" : str(resp_json["metric"]["precipRate"]),
        "metric_precipTotal" : str(resp_json["metric"]["precipTotal"]),
        "metric_elev" : str(resp_json["metric"]["elev"])
        }


        stationID = str(resp_json["stationID"])
        obsTimeUtc = str(resp_json["obsTimeUtc"])
        #obsTimeLocal = str(resp_json["obsTimeLocal"]).replace(" ","T")
        neighborhood = str(resp_json["neighborhood"]).replace(" ","")
        softwareType = str(resp_json["softwareType"])
        country = str(resp_json["country"])

        print(json_dict)
        labels="{stationID=\""+stationID+"\",neighborhood=\""+neighborhood+"\",softwareType=\""+softwareType+"\",country=\""+country+"\"}"
        
        for key in json_dict:
            if json_dict[key] != "None":
                print(json_dict[key])
                prom_type = "# TYPE wunderground_"+key+" gauge"+"\n"
                prom_metric = "wunderground_"+key+labels+" "+json_dict[key]+"\n"
                output_list.append(prom_type)
                output_list.append(prom_metric)

    output = ''.join(output_list)
    print(output)
    return output



@app.route('/metrics')
def metrics2():
    response = make_response(generateMetrics(), 200)
    response.mimetype = "text/plain"
    return response


@app.route('/metrics2')
def metrics():
    return generateMetrics()



if "ENV_PORT" in os.environ:
    SERVER_PORT=os.environ["ENV_PORT"]
else:
    SERVER_PORT="9122"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=SERVER_PORT)
