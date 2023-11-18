import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Se conectó con MQTT: " + str(rc))
    client.subscribe("ALSW/#")

def on_message(client, userdata, msg):
    print(f"Publicador {userdata} - {msg.topic} {str(msg.payload)}")

# Publicador 1
client1 = mqtt.Client(userdata="Publisher1")
client1.on_connect = on_connect
client1.on_message = on_message
client1.connect("test.mosquitto.org", 1883, 60)

# Publicador 2
client2 = mqtt.Client(userdata="Publisher2")
client2.on_connect = on_connect
client2.on_message = on_message
client2.connect("test.mosquitto.org", 1883, 60)

# Publicador 3
client3 = mqtt.Client(userdata="Publisher3")
client3.on_connect = on_connect
client3.on_message = on_message
client3.connect("test.mosquitto.org", 1883, 60)

# Loop infinito para mantener la conexión y permitir la publicación
while True:
    client1.publish("ALSW/test_topic", "Mensaje del publicador 1")
    client2.publish("ALSW/test_topic", "Mensaje del publicador 2")
    client3.publish("ALSW/test_topic", "Mensaje del publicador 3")
    time.sleep(5)  