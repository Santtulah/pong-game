import sys
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = pygame.color.Color('red')
FPS = 60
screen_width = 1000
screen_height = 600
bg_color = pygame.Color('black')


class Button:
    def __init__(self, parent_screen,  color, x, y, width, height, text=''):
        self.parent_screen = parent_screen
        self.color = color
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.text = text

    def draw(self, parent_screen, outline=None):
        if outline:
            pygame.draw.rect(self.parent_screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 3, border_radius=10)

            pygame.draw.rect(self.parent_screen, self.color, (self.x, self.y, self.width, self.height), 0, border_radius=10)

        pygame.draw.rect(self.parent_screen, self.color, (self.x, self.y, self.width, self.height), 3, border_radius=10)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 35)
            text = font.render(self.text, False, WHITE)
            self.parent_screen.blit(text, (self.x + self.width/2 - text.get_width()/2, self.y + self.height/2 - text.get_height()/2))

        pygame.display.update()

    def mouse_over(self, pos):

        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


class Players:

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.paddle_width, self.paddle_height = 30, 140
        self.player = pygame.Rect(screen_width - 40, screen_height / 2 - 70, self.paddle_width, self.paddle_height)
        self.opponent = pygame.Rect(10, screen_height / 2 - 70, self.paddle_width, self.paddle_height)
        self.player_color = pygame.Color('red')
        self.player_speed = 0

    def draw_players(self):
        pygame.draw.rect(self.parent_screen, self.player_color, self.player)
        pygame.draw.rect(self.parent_screen, self.player_color, self.opponent)

    def move_player(self):
        self.player.y += self.player_speed

        if self.player.y <= 0 or self.player.bottom >= screen_height:
            self.player.y -= self.player_speed


class Ball:

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.ball_color = pygame.Color('white')
        self.ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
        self.ball_speed_x, self.ball_speed_y = 15, 0

    def move_ball(self):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

    def draw_ball(self):
        pygame.draw.ellipse(self.parent_screen, self.ball_color, self.ball)


class Menu:

    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.opponent_speed = 0
        self.play_button = Button(self.parent_screen, WHITE, screen_width / 2 - 150, screen_height / 2 - 80, 300, 60,
                                  'PLAY PONG')
        self.quit_button = Button(self.parent_screen, WHITE, screen_width / 2 - 150, screen_height / 2, 300, 60, 'QUIT')

        self.easy_button = Button(self.parent_screen, WHITE, screen_width / 2 - 150, screen_height / 2 - 80, 300, 60,
                                  'Easy')
        self.medium_button = Button(self.parent_screen, WHITE, screen_width / 2 - 150, screen_height / 2, 300, 60, 'Medium')

        self.hard_button = Button(self.parent_screen, WHITE, screen_width / 2 - 150, screen_height / 2 + 80, 300, 60, 'Hard')

        # self.ball_animation = pygame.Rect(15, 15, 30, 30)

    def draw_main_menu(self):
        self.play_button.draw(self.parent_screen, WHITE)
        self.quit_button.draw(self.parent_screen, WHITE)

    def draw_level_menu(self):
        self.easy_button.draw(self.parent_screen, WHITE)
        self.medium_button.draw(self.parent_screen, WHITE)
        self.hard_button.draw(self.parent_screen, WHITE)

    def main_menu(self):
        self.parent_screen.fill(bg_color)
        self.play_button.color = BLACK
        self.quit_button.color = BLACK
        self.draw_main_menu()

        menu = True

        while menu:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()

                    if self.play_button.mouse_over(pos):
                        self.play_button.color = RED

                    elif self.quit_button.mouse_over(pos):
                        self.quit_button.color = RED

                    else:
                        self.play_button.color = BLACK
                        self.quit_button.color = BLACK

                    self.draw_main_menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.mouse_over(pygame.mouse.get_pos()):
                        menu = False

                    if self.quit_button.mouse_over(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()

    def level_menu(self):
        self.parent_screen.fill(bg_color)
        self.easy_button.color = BLACK
        self.medium_button.color = BLACK
        self.hard_button.color = BLACK
        self.draw_level_menu()

        menu = True

        while menu:

            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:

                    if self.easy_button.mouse_over(pos):
                        self.easy_button.color = RED

                    elif self.medium_button.mouse_over(pos):
                        self.medium_button.color = RED

                    elif self.hard_button.mouse_over(pos):
                        self.hard_button.color = RED

                    else:
                        self.easy_button.color = BLACK
                        self.medium_button.color = BLACK
                        self.hard_button.color = BLACK

                    self.draw_level_menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.easy_button.mouse_over(pygame.mouse.get_pos()):
                        self.opponent_speed = 5
                        menu = False
                    if self.medium_button.mouse_over(pygame.mouse.get_pos()):
                        self.opponent_speed = 6
                        menu = False
                    if self.hard_button.mouse_over(pygame.mouse.get_pos()):
                        self.opponent_speed = 7
                        menu = False


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pong')
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.players = Players(self.screen)
        self.ball = Ball(self.screen)
        self.opponent_score = 0
        self.player_score = 0
        self.score_time = None
        self.max_goals = 5
        self.font = pygame.font.SysFont('comicsans', 40)
        self.play_again_button = Button(self.screen, WHITE, screen_width / 2 + 125, screen_height / 2 - 200, 250, 50,
                                   'PLAY AGAIN')
        self.main_menu_button = Button(self.screen, WHITE, screen_width / 2 + 125, screen_height / 2 - 125, 250, 50,
                                  'MAIN MENU')
        self.menu = Menu(self.screen)
        self.pong_sound = pygame.mixer.Sound('media/pong.ogg')
        self.score_sound = pygame.mixer.Sound('media/score.ogg')

    def mouse_movement_logic(self):

        pos = pygame.mouse.get_pos()

        if self.play_again_button.mouse_over(pos):
            self.play_again_button.color = RED
            self.play_again_button.draw(self.screen, WHITE)

        else:
            self.play_again_button.color = BLACK
            self.play_again_button.draw(self.screen, WHITE)

        if self.main_menu_button.mouse_over(pos):
            self.main_menu_button.color = RED
            self.main_menu_button.draw(self.screen, WHITE)

        else:
            self.main_menu_button.color = BLACK
            self.main_menu_button.draw(self.screen, WHITE)

    def reset(self):
        self.players = Players(self.screen)
        self.player_score, self.opponent_score = 0, 0
        self.ball.ball_speed_y = 0
        self.ball.ball_speed_x = 15

    def game_over(self):

        self.display_score()

        if self.player_score == self.max_goals:

            self.screen.blit(self.font.render('WINNER!', False, 'white'), (700, screen_height / 2))
            self.play_again_button.x = screen_width / 2 + 125
            self.main_menu_button.x = screen_width / 2 + 125
            self.mouse_movement_logic()

        if self.opponent_score == self.max_goals:

            self.screen.blit(self.font.render('WINNER!', False, 'white'), (100, screen_height / 2))
            self.play_again_button.x = screen_width / 2 - 375
            self.main_menu_button.x = screen_width / 2 - 375
            self.mouse_movement_logic()

        pygame.display.flip()

    def start_ball(self):

        opponent_countdown_pos = screen_width / 2 - screen_width / 4, screen_height / 2 - self.ball.ball.height
        player_countdown_pos = screen_width / 2 + screen_height / 4 + self.ball.ball.width, screen_height / 2 - self.ball.ball.height
        current_time = pygame.time.get_ticks()

        if (self.opponent_score + self.player_score) % 2 == 0:

            if current_time - self.score_time < 700:
                three = self.font.render('3', False, 'white')
                self.screen.blit(three, player_countdown_pos)

            if 700 < current_time - self.score_time < 1400:
                two = self.font.render('2', False, 'white')
                self.screen.blit(two, player_countdown_pos)

            if 1400 < current_time - self.score_time < 2100:
                one = self.font.render('1', False, 'white')
                self.screen.blit(one, player_countdown_pos)

            if current_time - self.score_time < 2400:
                self.ball.ball_speed_x, self.ball.ball_speed_y = 0, 0

            else:
                self.ball.ball_speed_y = 0
                self.ball.ball_speed_x = 15
                self.score_time = None

        else:

            if current_time - self.score_time < 700:
                three = self.font.render('3', False, 'white')
                self.screen.blit(three, opponent_countdown_pos)

            if 700 < current_time - self.score_time < 1400:
                two = self.font.render('2', False, 'white')
                self.screen.blit(two, opponent_countdown_pos)

            if 1400 < current_time - self.score_time < 2100:
                one = self.font.render('1', False, 'white')
                self.screen.blit(one, opponent_countdown_pos)

            if current_time - self.score_time < 2400:
                self.ball.ball_speed_x, self.ball.ball_speed_y = 0, 0

            else:
                self.ball.ball_speed_y = 0
                self.ball.ball_speed_x = -15
                self.score_time = None

    def display_score(self):

        display_opponent_score = self.font.render(f'{self.opponent_score}', True, (pygame.color.Color('white')))
        display_player_score = self.font.render(f'{self.player_score}', True, (pygame.color.Color('white')))
        self.screen.blit(display_player_score, (screen_width / 2 + 35, 40))
        self.screen.blit(display_opponent_score, (screen_width / 2 - 50, 40))

    def draw_middle_line(self):
        pygame.draw.aaline(self.screen, pygame.Color('white'), (screen_width / 2, 0), (screen_width / 2, screen_height))

    def collision_with_paddle(self):
        max_y_speed = 9

        if self.ball.ball.colliderect(self.players.player) and self.ball.ball_speed_x > 0:
            # Difference between balls and paddles center y-position
            difference_between_y = self.players.player.centery - self.ball.ball.centery

            # Calculates how far from the center of the paddle the ball collides
            reduction_factor = (self.players.paddle_height / 2) / max_y_speed

            # speed of the ball considering the position it collides from middle of the paddle
            y_velocity = difference_between_y / reduction_factor

            if abs(self.ball.ball.right - self.players.player.left) < 10 and self.ball.ball_speed_x > 0:
                self.ball.ball_speed_x *= -1
                self.ball.ball_speed_y = -1 * y_velocity

            if abs(self.ball.ball.top - self.players.player.bottom) < 10 and self.ball.ball_speed_y < 0:
                self.ball.ball_speed_y *= -1
            if abs(self.ball.ball.bottom - self.players.player.top) < 10 and self.ball.ball_speed_y > 0:
                self.ball.ball_speed_y *= -1

            else:
                self.ball.ball_speed_x *= -1
            pygame.mixer.Sound.play(self.pong_sound)

        if self.ball.ball.colliderect(self.players.opponent) and self.ball.ball_speed_x < 0:
            # Difference between balls and paddles center y-position
            difference_between_y = self.players.opponent.centery - self.ball.ball.centery

            # Calculates how far from the center of the paddle the ball collides
            reduction_factor = (self.players.paddle_height / 2) / max_y_speed

            # speed of the ball considering the position it collides from middle of the paddle
            y_velocity = difference_between_y / reduction_factor

            if abs(self.players.opponent.right - self.ball.ball.left) < 10 and self.ball.ball_speed_x < 0:
                self.ball.ball_speed_x *= -1
                self.ball.ball_speed_y = y_velocity
            if abs(self.ball.ball.top - self.players.opponent.bottom) < 10 and self.ball.ball_speed_y < 0:
                self.ball.ball_speed_y *= -1
            if abs(self.ball.ball.bottom - self.players.opponent.top) < 10 and self.ball.ball_speed_y > 0:
                self.ball.ball_speed_y *= -1
            else:
                self.ball.ball_speed_x *= -1
            pygame.mixer.Sound.play(self.pong_sound)

    def ball_hits_borders(self):

        if self.ball.ball.top <= 0 or self.ball.ball.bottom >= screen_height:
            self.ball.ball_speed_y *= -1

        if self.ball.ball.left <= 0:
            self.player_score += 1
            self.score_time = pygame.time.get_ticks()
            self.ball.ball.center = screen_width / 2 + 15, screen_height / 2 - 15
            pygame.mixer.Sound.play(self.score_sound)

        if self.ball.ball.right >= screen_width:
            self.opponent_score += 1
            self.score_time = pygame.time.get_ticks()
            self.ball.ball.center = screen_width / 2 - 15, screen_height / 2 - 15
            pygame.mixer.Sound.play(self.score_sound)

        if self.player_score == 5 or self.opponent_score == 5:
            self.score_time = False
            raise 'Game over'

    def move_opponent(self):

        if self.players.opponent.centery < self.ball.ball.y:
            self.players.opponent.centery += self.menu.opponent_speed
        if self.players.opponent.centery > self.ball.ball.y:
            self.players.opponent.centery -= self.menu.opponent_speed
        if self.players.opponent.top <= 0:
            self.players.opponent.top = 0
        if self.players.opponent.bottom >= screen_height:
            self.players.opponent.bottom = screen_height

    def play(self):

        self.screen.fill(bg_color)
        self.players.draw_players()
        self.ball.draw_ball()
        self.draw_middle_line()
        self.ball_hits_borders()
        self.collision_with_paddle()
        self.move_opponent()
        self.players.move_player()
        self.display_score()
        self.ball.move_ball()
        if self.score_time:
            self.start_ball()

        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        pause = False

        self.menu.main_menu()
        self.menu.level_menu()

        while running:

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if event.key == pygame.K_RETURN:
                        pause = False

                    if not pause:

                        if event.key == pygame.K_UP:
                            self.players.player_speed -= 7

                        if event.key == pygame.K_DOWN:
                            self.players.player_speed += 7

                if event.type == pygame.KEYUP:

                    if not pause:

                        if event.key == pygame.K_UP:
                            self.players.player_speed += 7
                        if event.key == pygame.K_DOWN:
                            self.players.player_speed -= 7

                if event.type == pygame.MOUSEMOTION:
                    if pause:
                        self.mouse_movement_logic()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_again_button.mouse_over(pygame.mouse.get_pos()):
                        pause = False

                    if self.main_menu_button.mouse_over(pygame.mouse.get_pos()):
                        self.menu.main_menu()
                        self.menu.level_menu()
                        pause = False

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            try:
                if not pause:
                    self.play()

            except Exception as e:

                pause = True
                self.game_over()
                self.reset()


if __name__ == '__main__':
    game = Game()
    game.run()
