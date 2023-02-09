# CoDeck

## Concept

CoDeck is an IoT project developed by José Manuel Aguado Gala, Cristian De Gracia Nuero and José Justo Tena Agudo. 

It consists of a keyboard to whose keys can be assigned different scripts developed by the user, this allows us to associate keyboard shortcuts, interaction with the browser, operating system commands or execution of software installed on CoDeck among many other options.

You can see a picture of the product in final-product.jpeg and a video of the project running in video-demo.mp4.

## Hardware

On the hardware side we have a keyboard created on Arduino components that allows us to send a certain signal depending on the key pressed to a program developed in Arduino.

## Software

On the software side, the Arduino program communicates the signals it receives to a code developed in Python which offers an interface developed using TKinder that allows the user to associate their scripts to each of the keys and persistence of these associations and scripts through a SQLite database.
