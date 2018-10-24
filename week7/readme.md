### SVA IxD Week 7 - OpenCV Project
Team - Luigi, Ravi, Ching

# DESIGN CONCEPT
For this project, we are using the camera to identify street crossing signs for users that are unable to see it. Since the city use the same image for signs, we want to use openCV to detect the shape and color, then show output for indications according to the result.

For example:

[https://imgur.com/FWezK4E]

[https://imgur.com/rs6Qq7x]

**INPUT**
The image capture by the camera is processed through the Color Detection code so that colors can be identfied. 

**OUTPUT**
As soon as the color is identified, an audio with an instruction is played for the user. For example: "Go!" for green and "Stop!" for red.


# Challenges

**1. Identifying the edges of the images**
The Threshold function is important to identify the edges on the image that are being read by the camera. This function substitutes each pixel by a black or white pixel, depending on the aumount of the intensity applied. We used a slider to be able to control this intensity.

**2. Getting the pixel added**
We use the code on the color detection example, but we failed to load the value for pixel.length.
