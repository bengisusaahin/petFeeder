# petFeeder
Rasperrypi0 project 

Firstly I want to remind you of our project. In this project, we developed a pet feeder machine controllable by the cell phones of pet owners. We developed a 3D prototype and as you can see in the pictures in the slide it has different sections and you can change the feed bowl using your mobile phone. When you want to change the section of the bowl it will be rotating and your pet will be able to eat the food in another section when the feed in one section is done.
We developed our mobile application on Android Studio with Java. For Raspberry Pi, we used Python to program it.
In the development process, we faced some problems and I want to talk about them. while developing the prototype, we realized that it was not useful and could not be improved. This was our first problem. We searched for different resources on the internet for a more useful and aesthetic design. We took a look at various 3d designs in thingiverse.com. As a result of these stages, we decided on the final version of our prototype. We printed our prototype from a 3d printer.
Another problem was that the servo and prototype worked together correctly.  We handled it more easily using gpiozero's angularservo method. Otherwise, we would have to write long and complex code.
Another problem we had was the connection problem. We had a hard time connecting our computer and Raspberry Pi to the same network. At the end of our internet searches, we were able to connect to the same network by setting the name and password of the hotspot wifi as the same as the Raspberry Pi 0.

Sending commands from our mobile app to our Raspberry Pi was another issue. At the end of the searches we made on the network on the Internet, we were able to successfully send the commands.

The libraries used in this project are: AngularServo
RPi.GPIO
gpiozero
Servomotor from socket 
AngularServo

LEARNED TECHNOLOGIES:
We learned how to print from a 3d printer as another technology.
 
<img hspace="10"  src = "https://github.com/bengisusaahin/petFeeder/assets/74653216/37ff04fc-4af7-4042-9fb2-abe3f61e5024"  width = "250" height = "300" />
<img  hspace="10" src = "https://github.com/bengisusaahin/petFeeder/assets/74653216/b540cc86-5c97-4075-b63e-e582b56527c1"  width = "250" height = "300" />

<img hspace="10"  src = "https://github.com/bengisusaahin/petFeeder/assets/74653216/c9ef3df9-1741-401c-9fad-9d5db8c46c16"  width = "200" height = "400" />




