# ProyectoArquitectura

## Descripción del Proyecto

El objetivo de este proyecto es desarrollar un sistema utilizando la placa ESP32-CAM con el fin de capturar imágenes, enviarlas a Discord y almacenarlas en Firebase Storage. Además, se implementará una aplicación móvil utilizando App Inventor para mostrar las imágenes capturadas y controlar la cámara, incluyendo la activación y desactivación del flash.

## Componentes Necesarios

- ESP32-CAM: Módulo con cámara integrada y capacidades de conexión Wi-Fi.
- Sensor PIR.
- Cables de conexión.
- Smartphone con la aplicación App Inventor instalada.
- Cuenta en Discord.
- Cuenta en Firebase.

## Pasos para Configurar el Proyecto

#### 1. Conexión de la ESP32-CAM:

- Conecte la ESP32-CAM a la computadora utilizando cables de conexión.
- Abra el editor Thonny y asegúrese de tener las bibliotecas necesarias instaladas para la ESP32-CAM.
- Configure el editor para programar la ESP32-CAM con micropython.
- Cargue el programa de ejemplo de captura de imágenes en la ESP32-CAM y verifique su correcto funcionamiento.

![Imagen de WhatsApp 2023-06-02 a las 12 47 58](https://github.com/AlanVasquezAriza/ProyectoArquitectura/assets/124604196/c867c65b-befa-400b-b0d1-de84997ab25d)

#### 2. Configuración de Discord:

- Cree una cuenta en Discord si aun no la tiene.
- Crea un nuevo servidor o selecciona uno existente donde desee enviar las imágenes capturadas por la ESP32-CAM.
- Configure un canal específico dentro del servidor para recibir las imágenes.
- Genere una conexion con Webhooks en Discord para permitir que el programa se conecte y envíe imágenes al servidor seleccinado.

![Imagen de WhatsApp 2023-06-02 a las 12 47 40](https://github.com/AlanVasquezAriza/ProyectoArquitectura/assets/124604196/70197c34-0022-42cf-9893-db2eb837bb34)

#### 3. Configuración de Firebase:

- Cree una cuenta en Firebase si aun no la tiene.
- Crea un nuevo proyecto en Firebase y habilita Firebase Storage y realtime database.
- Obtenga el archivo JSON de configuración de Firebase para su proyecto.

![Imagen de WhatsApp 2023-06-02 a las 12 52 34](https://github.com/AlanVasquezAriza/ProyectoArquitectura/assets/124604196/394b558d-a47a-4e97-9982-3867d2da74d5)

#### 4. Programación de la ESP32-CAM:

- Desarrolle una funcion para capturar imagenes utilizando la camara y almacenarlas en un formato JSON que contenga la informacion de la imagen codificada.
- Utilice la biblioteca network para establecer una conexion con su red Wi-Fi.
- Utilice la biblioteca ufirebase para poderse conectar con firabase.
- Implemente una función para enviar la imagen capturada al canal de Discord.
- Implemente una funcion para cargar la imagen capturada a firebase store.
- Implemente una funcion que verifique los datos en el realtime database.

#### 5. Configuración de App Inventor:

- Abra el entorno de desarrollo de App Inventor y cree una nueva aplicación.
- Agregue los componentes necesarios, como un visor de imágenes, un switch para controlar el flash de la cámara y un swith para controlar el sensor PIR.
- Configure la conexion con firebase storage utilizando los bloques disponibles en App Inventor.
- Cree eventos y funciones que permitan mostrar la imagen capturada y controlar el flash con realtime database.

![Imagen de WhatsApp 2023-06-02 a las 12 53 43](https://github.com/AlanVasquezAriza/ProyectoArquitectura/assets/124604196/5c178449-51a6-4dff-b8b2-e3b7064af12c)

#### 6. Prueba y Depuración:

- Verifique que la ESP32-CAM sea capaz de capturar imágenes y enviarlas correctamente a Discord y firabase storage.

![image](https://github.com/AlanVasquezAriza/ProyectoArquitectura/assets/124604196/187346af-625b-4c3c-a3e4-1e63665d211d)

- Realice pruebas exhaustivas de la aplicación en App Inventor para asegurarse de que pueda controlar el flash y mostrar las imágenes capturadas de manera adecuada.

![Imagen de WhatsApp 2023-06-02 a las 13 07 47](https://github.com/AlanVasquezAriza/ProyectoArquitectura/assets/124604196/997850ed-4a97-4475-a3f7-0691ccfa4ee9)

#### 7. Mejoras y Personalizaciones:

- Realice mejoras adicionales en el proyecto, como la implementación de funciones adicionales de control de la cámara o la optimización del rendimiento del sistema.
