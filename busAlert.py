import time
import requests
from datetime import datetime, timedelta
from google.transit import gtfs_realtime_pb2



url = "https://api.carrismetropolitana.pt/v2/vehicles.pb"

linha_desejada = "4422_0"
parada_desejada = "160441"

inicio_hora = 16
inicio_min = 38

fim_hora = 16
fim_min = 45

# -------- dormir até 11:59 --------

agora = datetime.now()

inicio = agora.replace(hour=inicio_hora, minute=inicio_min, second=0, microsecond=0)

# se já passou hoje, agenda para amanhã
if agora > inicio:
    inicio += timedelta(days=1)

segundos_espera = (inicio - agora).total_seconds()

print(f"Dormindo até {inicio}")

time.sleep(segundos_espera)

# -------- loop principal --------

while True:

    agora = datetime.now()

    fim = agora.replace(hour=fim_hora, minute=fim_min, second=0, microsecond=0)

    # se passou das 12:10 termina
    if agora > fim:
        print("Janela de monitoramento terminou.")
        break

    try:

        r = requests.get(url)

        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(r.content)

        for entity in feed.entity:

            if entity.HasField('vehicle'):
                vehicle = entity.vehicle

                if (
                    vehicle.trip.route_id == linha_desejada
                    and vehicle.stop_id == parada_desejada
                    and vehicle.position.speed > 0 
                ):
                    
                    print(vehicle)

                
                    print("Sair de casa")
                    
                    exit()

    except Exception as e:
        print("Erro:", e)

    time.sleep(30)


    """
    trip {
  trip_id: "[68VF1]4422_0_1|1300|1600"
  schedule_relationship: SCHEDULED
  route_id: "4422_0"
}
position {
  latitude: 38.5276718
  longitude: -8.90449142
  bearing: 209
  speed: 7.5
}
current_status: IN_TRANSIT_TO
timestamp: 1773419964
stop_id: "160441"
vehicle {
  id: "44|12079"
  label: "12079"
  license_plate: "BD-11-QU"
}
    """