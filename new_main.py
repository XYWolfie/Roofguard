import pygame as pg
from new_sprites import *
from pygame import mixer




class Game():
    def __init__(self): # kjører når vi starter spillet

        pg.init()
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.DARKRED = (126,0,0)
        self.DARKGREEN = (0,126,0)
        self.BLUE = (150,222,209)
        self.COOLGREEN = (175,225,175)
        self.RANDOM = (153,223,67)

        self.WIDTH = 1000
        self.HEIGHT = 1000  

        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.comic_sans50 = pg.font.SysFont("Comic Sans MS", 50)   
        self.times75 = pg.font.SysFont("Times New Roman", 75)  
        
        self.FPS = 120
        self.clock = pg.time.Clock()

        self.bg = pg.image.load("bg_image.png").convert_alpha()
        self.bg = pg.transform.scale(self.bg, (1000,1000)) 

        self.hurt_sound = pg.mixer.Sound("hurt_sound.wav")
        self.hurt_sound.set_volume(0.4)

        self.start_screen_ambient = pg.mixer.Sound("windy-forest-ambience-01.wav")
        self.start_screen_ambient.set_volume(0.3)
        self.start_screen_ambient.fadeout(100)

        pg.mixer.set_num_channels(10)

        self.start_screen()


    def start_screen(self):
        pg.mixer.music.stop()
        pg.mixer.music.load("start_screen_music.mp3")
        pg.mixer.music.play(-1)
        self.start_screen_ambient.play(-1)
        #pg.mixer.Channel(0).play(pg.mixer.music("start_screen_music.mp3"))
        #pg.mixer.music.load("windy-forest-ambience-01.wav")
        #pg.mixer.Channel(1).play(pg.mixer.music("windy-forest-ambience-01.wav"))
        self.game_start = True
        while self.game_start:
            self.clock.tick(self.FPS)
            self.start_game_text = self.times75.render("Click SPACE to start", False, (self.BLACK))
            for event in pg.event.get():
                 if event.type == pg.QUIT:
                    self.game_over = False
                    pg.quit()

                 if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.game_start = False
                        pg.mixer.Sound.stop(self.start_screen_ambient)

            self.screen.blit(birth_screen, (-400,-260))
            self.screen.blit(self.start_game_text,(195,675))  # tegner tekst på skjerm. 
            
        
            pg.display.update()

        self.new()

      


    def new(self): # ny runde, kjører feks når vi dør

        pg.mixer.music.stop()
        pg.mixer.music.load('bg_music.mp3') 
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.5)

        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.enemy_group_spawn_ghost = pg.sprite.Group()
        self.enemy_group_spawn_skeleton = pg.sprite.Group()
        self.enemy_group_spawn_slime = pg.sprite.Group()
        self.projectiles_group = pg.sprite.Group()
        self.health_potion_group = pg.sprite.Group()
        self.run_potion_group = pg.sprite.Group()

        self.digger = Player(self)
        self.skeleton = Enemy()
        self.ghost = Enemy2()
        self.slime = Enemy3()

        self.stop = False

        self.text_player_hp = self.comic_sans50.render("HP: " + str(self.digger.liv), False, (self.DARKRED))  
        
        self.liv = 100

        self.can_run_potion_spawn = True
        self.can_heal_potion_spawn = True

        self.run()




    def run(self): # mens vi spiller, gameloop er her
            self.playing = True
            while self.playing: #gameloop
                self.clock.tick(self.FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.playing = False
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_v:
                            self.new()
                        if event.key == pg.K_b:
                            self.playing = False

                self.screen.fill(self.COOLGREEN)
                self.screen.blit(self.bg, (0, 0))

                # kollisjoner
                self.all_sprites.update() # kjør update funskjon til alle sprites i all_sprites
                self.hits = pg.sprite.spritecollide(self.digger, self.enemy_group, False)
                if self.hits:
                    self.digger.liv -= 1
                    print("LIV: ", self.digger.liv)
                    self.text_player_hp = self.comic_sans50.render("HP: " + str(self.digger.liv), False, (self.DARKRED))
                    if self.digger.liv <= 0:
                        self.stop = True
                        self.playing = False
                    
                    self.hits[0].liv -= 10
                    pg.mixer.Sound.play(self.hurt_sound)
                
                self.projectile_hit_ghost = pg.sprite.groupcollide(self.enemy_group_spawn_ghost, self.projectiles_group, False, True)
                if self.projectile_hit_ghost:
                    for enemy in self.projectile_hit_ghost:
                        enemy.liv -= 1
                        if self.ghost.liv <= 0:
                            self.digger.score += 30
                            
                self.projectile_hit_skeleton = pg.sprite.groupcollide(self.enemy_group_spawn_skeleton, self.projectiles_group, False, True)
                if self.projectile_hit_skeleton:
                    for enemy in self.projectile_hit_skeleton:
                        enemy.liv -= 1     
                        if enemy.liv <= 0:
                            self.digger.score += 25
                            
                    
                self.projectile_hit_slime = pg.sprite.groupcollide(self.enemy_group_spawn_slime, self.projectiles_group, False, True)
                if self.projectile_hit_slime:
                    for enemy in self.projectile_hit_slime:
                        enemy.liv -= 1
                        print(enemy.liv)
                        if enemy.liv <= 0:
                            self.digger.score += 20
                            enemy.kill()

                

                self.text_player_score = self.comic_sans50.render("SCORE: " + str(self.digger.score), False, (self.BLUE))
                
                
        
                #lag nye fiender + waves
                if len(self.enemy_group_spawn_skeleton) < 4:
                    self.skeleton = Enemy()
                    self.all_sprites.add(self.skeleton)
                    self.enemy_group.add(self.skeleton)
                    self.enemy_group_spawn_skeleton.add(self.skeleton)

                if len(self.enemy_group_spawn_ghost) < 3 and self.digger.score > 499:
                    self.ghost = Enemy2()
                    self.all_sprites.add(self.ghost)
                    self.enemy_group.add(self.ghost)
                    self.enemy_group_spawn_ghost.add(self.ghost)

                if len(self.enemy_group_spawn_slime) <3 and self.digger.score > 1499:
                    self.slime = Enemy3()
                    self.all_sprites.add(self.slime)
                    self.enemy_group.add(self.slime)
                    self.enemy_group_spawn_slime.add(self.slime)

                if self.digger.score > 999 and  self.can_run_potion_spawn is True:
                    self.run_potion = Running_potion(self)
                    self.all_sprites.add(self.run_potion)
                    self.run_potion_group.add(self.run_potion)
                    self.can_run_potion_spawn = False

                if self.digger.score > 1999:
                    self.skeleton.speed = randint(2,4)
                    self.ghost.speed = 1
                    self.slime.speed = 3

                if self.digger.score > 2499 and self.can_heal_potion_spawn is True:
                    self.health_potion = Healing_potion(self)
                    self.all_sprites.add(self.health_potion)
                    self.health_potion_group.add(self.health_potion)
                    self.can_heal_potion_spawn = False
                
                if self.digger.score > 2999:
                    self.skeleton.speed = randint(3,5)
                    self.ghost.speed = 2
                    self.slime.speed = 4
                
                if self.digger.score > 3499:
                    self.skeleton.speed = randint(4,6)
                    self.ghost.speed = 3
                    self.slime.speed = 5

                if self.digger.score > 3499:
                    self.skeleton.speed = randint(5,7)
                    self.ghost.speed = 4
                    self.slime.speed = 6

                if self.digger.score > 3999:
                    self.skeleton.speed = randint(6,8)
                    self.ghost.speed = 5
                    self.slime.speed = 7
            
                self.all_sprites.draw(self.screen) # tegner alle sprites i gruppen all_sprites til screen
        
                self.screen.blit(self.text_player_hp, (190, 5))

                self.screen.blit(self.text_player_score, (650, 5))

                hpotion_hit = pg.sprite.spritecollide(self.digger, self.health_potion_group, True)
                if hpotion_hit:
                    hpotion_hit[0].give_liv()
                    self.text_player_hp = self.comic_sans50.render("HP: " + str(self.digger.liv), False, self.DARKRED)
                
                rpotion_hit = pg.sprite.spritecollide(self.digger, self.run_potion_group, True)
                if rpotion_hit:
                    rpotion_hit[0].give_run()


                print("Amount of sprites: ",len(self.all_sprites))
                pg.display.update()

            # etter game loop  
            if self.stop:
                self.game_stop()

        
    def game_stop(self): # game over screen
        pg.mixer.music.stop()
        pg.mixer.music.load("Fluffing-a-Duck.mp3")
        pg.mixer.music.play(-1)
        self.game_over = True
        while self.game_over:
            self.clock.tick(self.FPS)
            self.game_over_text = self.comic_sans50.render("Game over, click R to restart", False, (self.DARKRED))
            self.back_to_menu_text = self.comic_sans50.render("Click B to reach the menu", False, (self.DARKRED))
            self.score_text = self.comic_sans50.render("SCORE:" + str(self.digger.score), False, (self.DARKRED))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False
                    pg.quit()
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_b:
                        self.game_over = False
                        self.start_screen()


                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:  # om vi clicker på R, avslutter vi game over loop, og går derett til self.new() som ligger etter game_over loop
                        self.game_over = False 
            
            self.screen.fill(self.BLACK)
            self.screen.blit(self.game_over_text,(165,750))  # tegner tekst på skjerm. 
            self.screen.blit(self.back_to_menu_text, (200, 800))
            self.screen.blit(dead_screen, (250,175))
            self.screen.blit(self.score_text, (325,90))
 
            pg.display.update()
 
        self.new()  # starter ny runde
        







g = Game() # game klassen blir laget (spillet starter)