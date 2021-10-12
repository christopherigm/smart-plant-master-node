from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import serial


# Create your views here.


class SmartPlantTest( APIView ):

    def get( self, request ):
        DEVICE = '/dev/rfcomm0'
        BAUD_RATE = 9600
        s = serial.Serial(DEVICE, BAUD_RATE)
        print('Connect to', DEVICE)

        s.write(b's')
        soil_moisture=str(s.readline()).replace("\\r\\n'", "")
        soil_moisture=soil_moisture.replace("b'", "")

        s.write(b'd')
        ldr=str(s.readline()).replace("\\r\\n'", "")
        ldr=ldr.replace("b'", "")

        s.write(b't')
        temperature=str(s.readline()).replace("\\r\\n'", "")
        temperature=temperature.replace("b'", "")

        s.write(b'h')
        humidity=str(s.readline()).replace("\\r\\n'", "")
        humidity=humidity.replace("b'", "")

        s.write(b'l')
        is_day=str(s.readline()).replace("\\r\\n'", "")
        is_day=is_day.replace("b'", "")

        data={
            "temperature": temperature,
            "soil_moisture": soil_moisture,
            "ldr": ldr,
            "humidity": humidity,
            "is_day": is_day
        }
        return Response(data, status.HTTP_200_OK)
