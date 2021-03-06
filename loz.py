import arcade
import os
import math

sprite_scale = 0.5
native_sprite = 128
sprite_size = int(sprite_scale * native_sprite)

screen_width = sprite_size * 18
screen_height = sprite_size * 10
screen_title = "Temporary Title"

move_speed = 10

tex_right = 1
tex_left = 0

health = 6

bullet_speed = 5

boomboom = 60

class Room:

    def __init__(self):
        self.wall_list = None

        self.background_list = None





def startroom_setup():

    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, screen_height - sprite_size):
            # Loop for each box going across
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 3 and x != sprite_size * 4 and x != sprite_size * 10 and x != sprite_size * 11) or y == 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in (0, screen_width - sprite_size):
        # Loop for each box going across
        for y in range(sprite_size, screen_height - sprite_size, sprite_size):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != sprite_size * 4 and y != sprite_size * 5) or x == 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
    wall.left = 7 * sprite_size
    wall.bottom = 5 * sprite_size
    room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background_2.jpg")

    return room

def outside1_setup():

    room = Room()

    room.wall_list = arcade.SpriteList()

    for y in (0, screen_height - sprite_size):
            # Loop for each box going across
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 7 and x != sprite_size * 8) or y == 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for x in (0, screen_width - sprite_size):
        # Loop for each box going across
        for y in range(sprite_size, screen_height - sprite_size, sprite_size):
            # Skip making a block 4 and 5 blocks up
            if (y != sprite_size * 4 and y != sprite_size * 5) or x != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

            

    wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
    wall.left = 7 * sprite_size
    wall.bottom = 5 * sprite_size
    room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background_2.jpg")

    return room

def startcave_setup():

    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 3 and x != sprite_size * 4) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
    wall.left = 7 * sprite_size
    wall.bottom = 5 * sprite_size
    room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background.jpg")

    return room

def outside2_setup():

    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5) or x != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 7 and x != sprite_size * 8) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background_2.jpg")

    return room

def outside3_setup():

    room = Room()

    room.wall_list = arcade.SpriteList()

    for x in (0, screen_width - sprite_size):
        for y in range(0, screen_height, sprite_size):
            if (y != sprite_size * 4 and y != sprite_size * 5):
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    for y in (0, screen_height - sprite_size):
        for x in range(0, screen_width, sprite_size):
            if (x != sprite_size * 10 and x != sprite_size * 11) or y != 0:
                wall = arcade.Sprite("images/boxCrate_double.png", sprite_scale)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    room.background = arcade.load_texture("images/background_2.jpg")

    return room

class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        # Load a left facing texture and a right facing texture.
        # mirrored=True will mirror the image we load.
        texture = arcade.load_texture("images/character.png", mirrored=True, scale=sprite_scale)
        self.textures.append(texture)
        texture = arcade.load_texture("images/character.png", scale=sprite_scale)
        self.textures.append(texture)

        # By default, face right.
        self.set_texture(tex_right)



    def update(self):


        # Figure out if we should face left or right
        if self.change_x < 0:
            self.set_texture(tex_left)
        if self.change_x > 0:
            self.set_texture(tex_right)





class Explosion(arcade.Sprite):
    """ This class creates an explosion animation """

    # Static variable that holds all the explosion textures
    explosion_textures = []

    def __init__(self, texture_list):
        super().__init__("images/explosion/explosion0000.png")

        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list

    def update(self):

        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.kill()


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.frame_count = 0

        # Sprite lists
        self.current_room = 0

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None
        self.enemy_list = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Pre-load the animation frames. We don't do this in the __init__
        # of the explosion sprite because it
        # takes too long and would cause the game to pause.
        self.explosion_texture_list = []

        for i in range(boomboom):
            # Files from http://www.explosiongenerator.com are numbered sequentially.
            # This code loads all of the explosion0000.png to explosion0270.png files
            # that are part of this explosion.
            texture_name = f"images/explosion/explosion{i:04d}.png"

            self.explosion_texture_list.append(arcade.load_texture(texture_name))

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = Player()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()

        enemy = arcade.Sprite("images/enemy.png", sprite_scale)
        enemy.center_x = 120
        enemy.center_y = screen_height - 120
        enemy.angle = 180
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite("images/enemy.png", sprite_scale)
        enemy.center_x = screen_width - 120
        enemy.center_y = screen_height - 120
        enemy.angle = 180
        self.enemy_list.append(enemy)


        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = startroom_setup()
        self.rooms.append(room)

        room = outside1_setup()
        self.rooms.append(room)

        room = startcave_setup()
        self.rooms.append(room)

        room = outside2_setup()
        self.rooms.append(room)

        room = outside3_setup()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)


    def on_draw(self):
        health_x = 20
        health_y = screen_height - 50
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_texture_rectangle(screen_width // 2, screen_height // 2,
                                      screen_width, screen_height, self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.
        if self.current_room != 0 and self.current_room == 1:
            self.enemy_list.draw()
            self.bullet_list.draw()

        self.player_list.draw()
        self.explosions_list.draw()

        for i in range(health):
            arcade.draw_xywh_rectangle_filled(health_x, health_y, 20, 20, arcade.color.BLUE)
            health_x += 50


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def update(self, delta_time):
        global health
        """ Movement and game logic """

        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = move_speed
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -move_speed
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -move_speed
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = move_speed

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.player_list.update()

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > screen_width and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = screen_width
        elif self.player_sprite.center_x in range(670,740) and self.player_sprite.center_y > screen_height and self.current_room == 0:
            self.current_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y > screen_height and self.current_room == 0:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y < 0 and self.current_room == 2:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = screen_height
        elif self.player_sprite.center_y > screen_height and self.current_room == 1:
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0
        elif self.player_sprite.center_y < 0 and self.current_room == 3:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = screen_height
        elif self.player_sprite.center_y < 0 and self.current_room == 4:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = screen_height
        elif self.player_sprite.center_x < 0 and self.current_room == 3:
            self.current_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = screen_width
        elif self.player_sprite.center_x > screen_width and self.current_room == 4:
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0

        self.frame_count += 1




        for enemy in self.enemy_list:
            if self.current_room != 0 and self.current_room == 1:
                # Get the destination location for the bullet
                dest_x = self.player_sprite.center_x
                dest_y = self.player_sprite.center_y

                # Do math to calculate how to get the bullet to the destination.
                # Calculation the angle in radians between the start points
                # and end points. This is the angle the bullet will travel.
                x_diff = dest_x - enemy.center_x
                y_diff = dest_y - enemy.center_y
                angle = math.atan2(y_diff, x_diff)

                # Set the enemy to face the player.
                enemy.angle = math.degrees(angle) - 90

                if self.frame_count % 180 == 0:
                    bullet = arcade.Sprite("images/laserBlue01.png", sprite_scale)
                    bullet.center_x = enemy.center_x
                    bullet.center_y = enemy.center_y

                    # Angle the bullet sprite
                    bullet.angle = math.degrees(angle)

                    # Taking into account the angle, calculate our change_x
                    # and change_y. Velocity is how fast the bullet travels.
                    bullet.change_x = math.cos(angle) * bullet_speed
                    bullet.change_y = math.sin(angle) * bullet_speed

                    self.bullet_list.append(bullet)

            # Get rid of the bullet when it flies off-screen
            for bullet in self.bullet_list:
                hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bullet_list)
                hit_list2 = arcade.check_for_collision_with_list(bullet, self.rooms[self.current_room].wall_list)
                if bullet.top < 0:
                    bullet.kill()
                elif len(hit_list2) > 0:
                    bullet.kill()
                elif len(hit_list) > 0:
                    health -= 1
                    explosion = Explosion(self.explosion_texture_list)
                    explosion.center_x = hit_list[0].center_x
                    explosion.center_y = hit_list[0].center_y
                    self.explosions_list.append(explosion)
                    bullet.kill()


            self.bullet_list.update()
            self.explosions_list.update()




        if health == 0:
            self.player_sprite.kill()
            print("You died")

        print(self.player_sprite.center_x)




def main():
    """ Main method """
    window = MyGame(screen_width, screen_height, screen_title)
    window.setup()
    arcade.run()



if __name__ == "__main__":
    main()

