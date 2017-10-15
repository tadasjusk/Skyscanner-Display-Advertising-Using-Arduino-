
import requests,serial, time
payload={'apikey':'ha788682524436452673036521217390'}
r = requests.get("http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/ES/eur/en-US/bcn/anywhere/2017-10-20/2017-10-22",params=payload)
j=r.json()

quotes = j['Quotes']

cheapest_quote = quotes[0]
cheapest_price = quotes[0]['MinPrice']
for quote in quotes:
  if quote['MinPrice'] < cheapest_price:
      cheapest_price = quote['MinPrice']
      cheapest_quote = quote

DestinationId=(cheapest_quote['OutboundLeg']['DestinationId'])

places =j['Places']

for place in places:
  if place['PlaceId']==DestinationId:
      cheapest_place=place['CityName']
      

arduino = serial.Serial('COM13', 115200, timeout=.1)
time.sleep(1) #give the connection a second to settle
arduino.write("Flights to ")
arduino.write(cheapest_place.encode('ascii'))
arduino.write(" from ")
arduino.write(str(int(cheapest_price)))
arduino.write(" Eur")

while True:
    data = arduino.readline()
    if data:
        print data.rstrip('\n') #strip out the new lines for now
        # (better to do .read() in the long run for this reason
