
# wunderground_exporter
prometheus exporter for weather underground station




## docker image

https://hub.docker.com/repository/docker/badsmoke/wunderground_exporter


### arch:
```
-amd64
```



# environment vars

ENV_STATION_ID default:IDRESDEN521   multiple ids are possible, comma separated "IDRESDEN521,IDRESDEN522 "

ENV_API_KEY 

ENV_PORT default:9122


# Docker run / docker-compose

### docker run:
```
docker run -e "ENV_STATION_ID=IDRESDEN521" -e "ENV_API_KEY=1234f5670ae8910aa6f4110ae4588a87" -p 9122:9122 badsmoke/wunderground_exporter
```


### docker-compose:
```
version: '2'
services:
  wunderground_exporter:
    image: badsmoke/wunderground_exporter
    ports:
        - 9122:9122
    environment:
        - "ENV_STATION_ID=IDRESDEN521"
        - "ENV_API_KEY=1234f5670ae8910aa6f4110ae4588a87"


```


# Dockerfile:
```
FROM python:3-slim-buster

MAINTAINER badsmoke <dockerhub@badcloud.eu>


WORKDIR /usr/src/app



COPY ./server.py ./server.py
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python","-u","/usr/src/app/server.py" ]



```


# sample output

```
# TYPE wunderground_observations_lon gauge
wunderground_observations_lon{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 13.691622
# TYPE wunderground_observations_epoch gauge
wunderground_observations_epoch{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 1609774570
# TYPE wunderground_observations_lat gauge
wunderground_observations_lat{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 51.044556
# TYPE wunderground_observations_winddir gauge
wunderground_observations_winddir{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 203
# TYPE wunderground_observations_humidity gauge
wunderground_observations_humidity{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 99
# TYPE wunderground_observations_qcStatus gauge
wunderground_observations_qcStatus{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 1
# TYPE wunderground_metric_temp gauge
wunderground_metric_temp{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 1
# TYPE wunderground_metric_heatIndex gauge
wunderground_metric_heatIndex{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 1
# TYPE wunderground_metric_dewpt gauge
wunderground_metric_dewpt{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 1
# TYPE wunderground_metric_windChill gauge
wunderground_metric_windChill{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 0
# TYPE wunderground_metric_windSpeed gauge
wunderground_metric_windSpeed{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 5
# TYPE wunderground_metric_windGust gauge
wunderground_metric_windGust{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 6
# TYPE wunderground_metric_pressure gauge
wunderground_metric_pressure{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 1000.34
# TYPE wunderground_metric_precipRate gauge
wunderground_metric_precipRate{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 0.0
# TYPE wunderground_metric_precipTotal gauge
wunderground_metric_precipTotal{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 2.03
# TYPE wunderground_metric_elev gauge
wunderground_metric_elev{stationID="IDRESDEN521",obsTimeUtc="2021-01-04T15:36:10Z",neighborhood="Stollestr.Dach",softwareType="myAcuRite",country="DE"} 132

```
