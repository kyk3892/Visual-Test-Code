"""justwindows.py"""
import sys
import pygame
from pygame.locals import QUIT

pygame.init() #pygame 모듈을 초기화
SURFACE = pygame.display.set_mode((400,300))
pygame.display.set_caption("JUST WINDOWS") #윈도의 타이틀


def main():
    """main routine"""
    while True:
        SURFACE.fill((255,255,0))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

        
if __name__=='__main__':
    main()