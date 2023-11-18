import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Se conectó con MQTT: " + str(rc))
    client.subscribe("ALSW/#")

def on_message(client, userdata, msg):
    print(f"Suscriptor {userdata} - {msg.topic} {str(msg.payload)}")

# Suscriptor 1
client1 = mqtt.Client(userdata="Subscriber1")
client1.on_connect = on_connect
client1.on_message = on_message
client1.connect("test.mosquitto.org", 1883, 60)

# Suscriptor 2
client2 = mqtt.Client(userdata="Subscriber2")
client2.on_connect = on_connect
client2.on_message = on_message
client2.connect("test.mosquitto.org", 1883, 60)

# Suscriptor 3
client3 = mqtt.Client(userdata="Subscriber3")
client3.on_connect = on_connect
client3.on_message = on_message
client3.connect("test.mosquitto.org", 1883, 60)

# Mantener la conexión y escuchar mensajes
client1.loop_forever()
client2.loop_forever()
client3.loop_forever()
