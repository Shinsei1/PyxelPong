# Créé par Waîl Yeager, le 15/01/2024 en Python 3.7
import pyxel

class Jeu:
    def __init__(self):
        pyxel.init(128, 128, title="Tennis")
        self.raquette_y = 1
        self.raquette2y = 82
        self.balle_x = 60
        self.balle_y = 60
        self.balle_speed_x = 2
        self.balle_speed_y = 1
        self.passe = 0
        self.lose = False

        pyxel.run(self.update, self.draw)

    def deplacement(self):
        if pyxel.btn(pyxel.KEY_DOWN) and self.raquette_y < 108:
            self.raquette_y += 6
        if pyxel.btn(pyxel.KEY_UP) and self.raquette_y > 2:
            self.raquette_y -= 6

        if pyxel.btn(pyxel.KEY_S) and self.raquette2y < 108:
            self.raquette2y += 6
        if pyxel.btn(pyxel.KEY_Z) and self.raquette2y > 2:
            self.raquette2y -= 6

    def pos_actu(self):
        return [self.balle_y] , [self.raquette_y,self.raquette2y]


    def update(self):
        self.deplacement()
        self.balle_x += self.balle_speed_x
        self.balle_y += self.balle_speed_y

        if self.balle_x < -10 or self.balle_x > 128:
                self.lose = True

        if self.balle_x < 0:
            if self.raquette_y < self.balle_y < self.raquette_y + 32:
                self.balle_speed_x = abs(self.balle_speed_x)
        elif self.balle_x > 120:
            if self.raquette2y < self.balle_y < self.raquette2y + 32:
                self.balle_speed_x = -abs(self.balle_speed_x)

        if self.balle_y < 0 or self.balle_y > 120:
            self.balle_speed_y = -self.balle_speed_y

        if self.pos_actu()[0][0] == self.pos_actu()[1][0] or self.pos_actu()[0][0] == self.pos_actu()[1][1]:
            self.passe += 1


    def draw(self):
        if self.lose == False:
            pyxel.cls(0)
            pyxel.rect(1, self.raquette_y, 8, 45, 1)
            pyxel.rect(119, self.raquette2y, 8, 45, 1)
            pyxel.circb(self.balle_x, self.balle_y, 5, 14)
            #pyxel.rect(self.balle_x, self.balle_y, 8, 8, 8)
            pyxel.text(35, 120, "Nombre de passes:" + str(self.passe), 11)
        else:
             pyxel.text(50, 64, "GAME OVER", 7)
Jeu()
