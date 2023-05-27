import camera
from time import sleep
import machine, os, time
import network
import urequests
import ufirebase as firebase
from machine import Pin
import ustruct
from simple import MQTTClient

#Pin del led de flash
flash = machine.Pin(4, machine.Pin.OUT)



#--------------------------------------------------------------------WIFI-------------------------------------------------------------------------



print("Conectando al WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('ALANBRITO 9843', 'zam5sfw5aqj5k7m')
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Connected!")



#------------------------------------------------------------------Discord-----------------------------------------------------------------------



# Configuración del webhook de Discord
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1109212131032830093/SRH70rea08-80gurfzuR5vm8roMpJQwozw05X-PYN-Pyg59zZBRDSY_EfxOJZREzZdSC'

# Capturar foto y enviarla a Discord (Pir)
def capture_and_send_photo_discord():
    # Tomando la foto
    print('Capturando foto...')
    camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
    time.sleep(2)  # Esperar 2 segundos para que la cámara esté lista
    img = camera.capture()    
    camera.deinit()

    print('Enviando foto a Discord...')
    
    # Establece el limite que se utiliza para separar las partes del formulario en el payload
    boundary = 'boundary123'
    # Crea el encabezado de la solicitud HTTP, tipo de contenido muchas partes, data en formulario
    headers = {
        'Content-Type': 'multipart/form-data; boundary=' + boundary
    }
    # Inicia la construccion del cuerpo de la solicitud, agrega una parte del formulario
    payload = b'--' + boundary.encode() + b'\r\n' \
              b'Content-Disposition: form-data; name="content"\r\n\r\n' \
              b'Se ha detectado movimiento desde el pin: Pin 14. Movimiento en: \r\n' \
              b'--' + boundary.encode() + b'\r\n' \
              b'Content-Disposition: form-data; name="file"; filename="photo.jpg"\r\n' \
              b'Content-Type: image/jpeg\r\n\r\n'
    # Agrega los bits de la imagen capturada al payload
    payload += img
    # (--) Final del formulario
    payload += b'\r\n--' + boundary.encode() + b'--\r\n'
    # Envia la solicitud POST a la URL de webhook de discord. Encabezado, datos
    response = urequests.post(DISCORD_WEBHOOK_URL, headers=headers, data=payload)
    # Imprime la respuesta
    print('Respuesta:', response.text)
    
    # Convertir la imagen en formato JPEG a una cadena de bytes
    photo_data = img.compress(quality=10).to_bytes()

    # Subir la foto a Firebase Storage
    upload_photo_to_firebase(photo_data)
    
    
# Capturar foto y enviarla a Discord (Tomar foto)
def capture_and_send_photo_discord_test():
    # Tomando la foto
    print('Capturando foto...')
    camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
    time.sleep(2)  # Esperar 2 segundos para que la cámara esté lista
    img = camera.capture()    
    camera.deinit()

    print('Enviando foto a Discord...')
    
    # Establece el limite que se utiliza para separar las partes del formulario en el payload
    boundary = 'boundary123'
    # Crea el encabezado de la solicitud HTTP, tipo de contenido muchas partes, data en formulario
    headers = {
        'Content-Type': 'multipart/form-data; boundary=' + boundary
    }
    # Inicia la construccion del cuerpo de la solicitud, agrega una parte del formulario
    payload = b'--' + boundary.encode() + b'\r\n' \
              b'Content-Disposition: form-data; name="content"\r\n\r\n' \
              b'Foto de prueba:  \r\n' \
              b'--' + boundary.encode() + b'\r\n' \
              b'Content-Disposition: form-data; name="file"; filename="photo.jpg"\r\n' \
              b'Content-Type: image/jpeg\r\n\r\n'
    # Agrega los bits de la imagen capturada al payload
    payload += img
    # (--) Final del formulario
    payload += b'\r\n--' + boundary.encode() + b'--\r\n'
    # Envia la solicitud POST a la URL de webhook de discord. Encabezado, datos
    response = urequests.post(DISCORD_WEBHOOK_URL, headers=headers, data=payload)
    # Imprime la respuesta
    print('Respuesta:', response.text)
        
        
        
#------------------------------------------------------------------PIR-----------------------------------------------------------------------



movimiento = False

def handle_interrupt(pin):
  global movimiento
  movimiento = True
  global interrupt_pin
  interrupt_pin = pin
  
pir = Pin(14, Pin.IN)
pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
print("Set up done!")
foto=1



#------------------------------------------------------------------FIREBASE-----------------------------------------------------------------------



firebase.setURL("https://proyecto-arquitectura-7085b-default-rtdb.firebaseio.com/")

# Configuración de Firebase Storage
FIREBASE_STORAGE_BUCKET = "proyecto-arquitectura-7085b.appspot.com"
FIREBASE_STORAGE_URL = "https://firebasestorage.googleapis.com/v0/b/" + FIREBASE_STORAGE_BUCKET

# Capturar foto con la ESP32-CAM
def capture_photo_firebase():
    # Tomando la foto
    print('Capturando foto...')
    camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
    time.sleep(2)  # Esperar a que la cámara se inicialice
    img = camera.capture()
    camera.deinit()
    return img

# Subir foto a Firebase
def upload_photo_firebase(img):
    response = urequests.post(FIREBASE_STORAGE_URL + "/o?uploadType=media&name=photo.jpg",
                             data=img,
                             headers={"Content-Type": "image/jpeg"})
    print("Foto subida a Firebase Storage. Código de respuesta:", response.status_code)

   
   
#------------------------------------------------------------------WHILE-----------------------------------------------------------------------
    
    
    
while True:
    
    print("Obteniendo datos del firebase....")
    
    firebase.get("Proyecto/ESP32/activar", "camara_activa", bg = 0)
    firebase.get("Proyecto/ESP32/tomarFoto", "camara_foto", bg = 0)
    firebase.get("Proyecto/ESP32/flash", "camara_flash", bg = 0)
    
    print("Se obtuvieton los datos del firebase correctamente")
    
    # Camara activa
    if firebase.camara_activa == "true":
        firebase.put("Proyecto/ESP32/mensaje1", "\"La camara esta activa\"", bg = 0)
        if movimiento:
            print('Movimiento detectado por el pin:', interrupt_pin)
            capture_and_send_photo_discord()
            img = capture_photo_firebase()
            upload_photo_firebase(img)
            movimiento = False
            print("Se han enviado los datos correctamente")
        else:
            print("No se detecta movimiento...")
        
    # Camara desactivada 
    if firebase.camara_activa == "false":
        movimiento = False
        firebase.put("Proyecto/ESP32/mensaje1", "\"La camara esta desactivada\"", bg = 0)
        
    # Tomar foto de prueba
    if int(firebase.camara_foto) == 1:
        firebase.put("Proyecto/ESP32/activar", "false", bg = 0) # Pone camara activa como 0 para solo tomar una foto y poder identificar cual es
        firebase.put("Proyecto/ESP32/mensaje1", "\"La camara esta desactivada\"", bg = 0)
        capture_and_send_photo_discord_test()
        img = capture_photo_firebase()
        upload_photo_firebase(img)
        firebase.put("Proyecto/ESP32/tomarFoto", "0", bg = 0) # Pone tomar foto como 0 para solo tomar una foto

    # Flash encendido
    if firebase.camara_flash == "true":
        flash.value(1)
        firebase.put("Proyecto/ESP32/mensaje2", "\"El flash esta activado\"", bg = 0)
        
    # Flash apagado
    if firebase.camara_flash == "false":
        flash.value(0)
        firebase.put("Proyecto/ESP32/mensaje2", "\"El flash esta desactivado\"", bg = 0)
        
    