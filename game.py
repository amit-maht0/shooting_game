import random
import sys

class ShootingGame:
    def __init__(self):
        self.guns=[
            {"name":'AK47',"magazine_size":10,"damage_per":60, "total_bullet": 20},
            {"name":'Pistol',"magazine_size":6, "damage_per":50,"total_bullet":30},
            {"name":'Short Gun',"magazine_size":1,"damage_per":90,"total_bullet":10},
            {"name":'Sniper',"magazine_size":5,"damage_per":100, "total_bullet":5}
            ]
        
        self.animals=[
            {"name":"Deer","resistance_per":40,"animal_count":50,"min_point":10},
            {"name":"Lion","resistance_per":70,"animal_count":10,"min_point":20},
            {"name":"Elephant","resistance_per":80,"animal_count":30,"min_point":30},
            {"name":"Dinosaur","resistance_per":100,"animal_count":5,"min_point":50}
        ]
        self.total_point = 0
        self.animal_killed = 0
        print("---------- Let's start shooting game! ----------")

    def select_gun(self):
        print("Choose your gun from inventory")
        for index, value in enumerate(self.guns):
            print(f"{index} : {value['name']}")

        gun_option = int(input('Select your preferred gun option :'))
        return self.guns[gun_option]
        

    def select_animal(self):
        random_animal = random.choice(self.animals)
        return random_animal
       

    def kill_info(self):
        kill_cmd = '''Press 'S' to shoot animal. On each press of 'S', damage will be made to the target animal as per gun damage capacity.\nKeep pressing 'S' untill the animal is dead.\n'''
        print(kill_cmd)


    def start_game(self):

        def kill_animal(user_cmd, tmp_magz, cmd_type, damage_delt):
            if selec_gun['total_bullet'] > 0 :
                if user_cmd == None:
                    if cmd_type.lower() == 's':
                        user_cmd = input('Enter S to shoot again: ') 
                    elif cmd_type.lower() == 'r':
                        user_cmd = input('Enter R to reload: ') 
                    else:
                        print('Invalid input!\n')
                        print('Game over!\n')
                        print(f"Total Points Earned : {self.total_point}")
                        return
                    
                    if user_cmd.lower() == 'r':
                        cmd_type = 's'
                        tmp_magz = selec_gun['magazine_size']
                        kill_animal(None, tmp_magz, cmd_type, damage_delt)

                    elif user_cmd.lower() == 's' :
                        pass

                if tmp_magz > 0 :
                    damage_delt = damage_delt - selec_gun['damage_per']
            
                    if damage_delt > 0:
                        selec_gun['total_bullet'] = selec_gun['total_bullet'] - 1
                        tmp_magz = tmp_magz-1
                        cmd_type = 's' if tmp_magz >0 else 'r'
                        bullet_left = 0 if selec_gun['total_bullet'] <= 0 else selec_gun['total_bullet']
                        print('Ahh! this animal is tough! \n')
                        print(f"Animal damage : {damage_delt}\nBullet left : {bullet_left}\n")
                        kill_animal(None, tmp_magz, cmd_type , damage_delt)

                    elif damage_delt == 0 or damage_delt <0:
                        selec_gun['total_bullet'] = selec_gun['total_bullet'] - 1
                        tmp_magz = tmp_magz-1
                        self.total_point = self.total_point + targ_animal['min_point']
                        targ_animal['animal_count'] = targ_animal['animal_count'] -1
                        self.animal_killed=self.animal_killed+1

                        bullet_left = 0 if selec_gun['total_bullet'] <= 0 else selec_gun['total_bullet']
                        print('Woow! You killed one animal \n')
                        print(f"Animal killed :{self.animal_killed}\nBullet left : {bullet_left}\nPoints Earned : {self.total_point}\n")

                        if targ_animal['animal_count'] <= 0:
                            print('You killed all animals!\n')
                            print(f"Total Points Earned : {self.total_point}\n")
                            print('You win!!')
                            return
                        
                        is_exit = input('Enter P to play again, x to exit : ')
                        
                        if is_exit.lower() == 'p':
                            cmd_type = 's'
                            damage_delt = targ_animal['resistance_per']
                            kill_animal(None, tmp_magz, cmd_type, damage_delt)
                        elif is_exit.lower() == 'x':
                            print('exixt',is_exit)
                            print(f"Total Points Earned : {self.total_point}")
                            sys.exit()
                        else:
                            print('Invalid input\n')
                            print('Game over!\n')
                            print(f"Total Points Earned : {self.total_point}")
                            return
                        
                elif tmp_magz <= 0:
                    cmd_type='r'
                    print(f"Opps! Reload magazine!")
                    kill_animal(None, tmp_magz, cmd_type, damage_delt)

            elif selec_gun['total_bullet'] <= 0 :
                print('Opps! You are out of bullet! \n')
                print('Run for your life!\n')
                print(f"Total Points Earned : {self.total_point}")
                return

        def input_func():
            user_input = input('Enter S to shoot :')
            temp_magazine = selec_gun['magazine_size']
            aniaml_resist = targ_animal['resistance_per']
            kill_animal(user_input, temp_magazine, 's', aniaml_resist)


        selec_gun = self.select_gun()
        print('--------------------------------------------- \n')
        print('Selected Gun info: \n')
        print(f"Gun : {selec_gun['name']} \nMagazine Size: {selec_gun['magazine_size']} \nDamage Percentage : {selec_gun['damage_per']} \nTotal Bullet : {selec_gun['total_bullet']} \n")
       
        targ_animal = self.select_animal()
        print('---------------------------------------------- \n')
        print('Your target animal is : \n')
        print(f"Animal : {targ_animal['name']}\nDamage Capacity : {targ_animal['resistance_per']}\nAnimal Count : {targ_animal['animal_count']}\nMinimum Point Per Kill : {targ_animal['min_point']}\n")

        print('--------------------------------------------- \n')
        self.kill_info()
        input_func()


start = ShootingGame()
start.start_game()