''' tocar uma muisica em py'''
import pygame 
pygame.init() # inicia o pygame(módulo)
pygame.mix.music.load(musica.mp3) #uso do mix  em pygame
pygame.mixer.music.play() # da  play
pygame.event.wait()
#depois que tocar a musica ele vai ter que espera, ate a música terminar pra ele poder encerra o progrma 

#  o programa não rodou por causa de um erro na modolo pygame 
# no caso seria nescessario outro modúlo ou biblioteca para executar a musica 
