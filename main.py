import pygame
import random

# Pygame 초기화
pygame.init()

# 게임 창 설정
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("슈팅 게임")
player1_img = pygame.image.load("C:\\Users\\박선균\\Desktop\\알게콘 프로젝트\\airplane.png")
player1_img = pygame.transform.scale(player1_img, (70, 70))
player2_img = pygame.image.load("C:\\Users\\박선균\\Desktop\\알게콘 프로젝트\\airplane.png")
player2_img = pygame.transform.scale(player2_img, (70, 70))
player2_img = pygame.transform.rotate(player2_img,180)

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 플레이어 설정
player_width, player_height = 50, 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 7
player2_x = screen_width // 2 - player_width // 2
player2_y = player_height - 10

player1_is_reloading = False #장전 확인
player2_is_reloading = False


# 총알 설정
bullet_width, bullet_height = 5, 10
bullet_speed = 10
bullet_volume = 45
bullets = []
bullets_volume = 30

# 총알2 설정
bullet2_width, bullet_height = 5, 10
bullet2_speed = 10
bullet2_volume = 45
bullets_2 = []
bullets_2_volume = 30

# 게임 루프
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 플레이어 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
        print(player_x)
        print(player_y)
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
        print(player_x)
        print(player_y)

    # 플레이어2 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player2_x > 0:
        player2_x -= player_speed
        print(player2_x)
        print(player2_y)
    if keys[pygame.K_d] and player2_x < screen_width - player_width:
        player2_x += player_speed
        print(player2_x)
        print(player2_y)



    # 총알 발사
    
    keys = pygame.key.get_pressed()

    # SPACE 키가 눌렸고 총알이 남아 있을 때
    if keys[pygame.K_SPACE] and bullets_volume > 0:
        # 총알 감소
        bullets_volume -= 1
        # 총알의 위치 계산
        bullet_x = player_x + player_width // 2 - bullet_width // 2
        bullet_y = player_y
        print(bullets_volume)
        # 총알을 총알 리스트에 추가
        bullets.append([bullet_x, bullet_y])
        now_clock = pygame.time.get_ticks()  # 현재 시간을 밀리초로 가져오기

    # SPACE 키가 눌렸고 총알이 더 이상 남아 있지 않을 때
    elif keys[pygame.K_SPACE] and bullets_volume == 0:
        print("장전 중 입니다..")

        # 루프 진입
        while True:
            later_clock = pygame.time.get_ticks()  # 현재 시간을 밀리초로 가져오기
            print(later_clock, now_clock)

            # 현재 시간과의 차이가 3초 이상인지 확인
            if later_clock - now_clock >= 3000:  # 밀리초 단위로 변환
                # 총알 수를 45로 재설정하고 루프 종료
                bullets_volume = 45
                break
            

    # 총알2 발사
    keys = pygame.key.get_pressed()
    if keys[pygame.K_c] and bullets_2_volume > 0:
        bullets_2_volume -= 1
        bullet_x = player2_x +40
        bullet_y = player2_y+70
        print(bullets_2_volume)
        bullets_2.append([bullet_x, bullet_y])


    # 총알 이동
    for bullet in bullets:
        bullet[1] -= bullet_speed
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # 총알2 이동
    for bullet in bullets_2:
        bullet[1] += bullet_speed
    bullets_2 = [bullet for bullet in bullets_2 if bullet[1] > 0]

    # 충돌 체크
    for bullet in bullets:
        if bullet[0] < player2_x + 70 and bullet[0] + bullet_width > player2_x and \
               bullet[1] < player2_y + 70 and bullet[1] + bullet_height > player2_y:
                bullets.remove(bullet)
                print("player1 win")  # player1 win logic
    # 충돌2 체크
    for bullet in bullets_2:
        if bullet[0] < player_x + 70 and bullet[0] + bullet_width > player_x and \
                bullet[1] < player_y + 70 and bullet[1] + bullet_height > player_y:
            bullets_2.remove(bullet)
            print("player2 win") #player 2 win logic



    # 화면 그리기
    screen.fill(WHITE)
    screen.blit(player1_img, (player_x, player_y))
    screen.blit(player2_img,(player2_x,player2_y))

    for bullet in bullets:
        pygame.draw.rect(
            screen, RED, [bullet[0], bullet[1], bullet_width, bullet_height])
    for bullet in bullets_2:
        pygame.draw.rect(
            screen, RED, [bullet[0], bullet[1], bullet_width, bullet_height])


    pygame.display.flip()

    # 초당 프레임 설정
    clock.tick(60)

# Pygame 종료
pygame.quit()
