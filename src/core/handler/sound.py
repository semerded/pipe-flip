import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.active_channels = {}
        self.load_sounds()

    def load_sounds(self):
        sound_dir = os.path.join("assets", "sounds")
        sound_files = {
            "background": "background_sound.wav",
            "button_press": "btn_press_impatient.wav",
            "button_tick": "btn_tick.wav",
            "footsteps": "footstep.wav",
            "game_over": "game_over.wav",
            "jump": "jump_cropped.wav",
            "level_complete": "level_complete.wav",
            "menu_selection": "menu_selection.wav"
        }

        for sound_name, filename in sound_files.items():
            path = os.path.join(sound_dir, filename)
            if os.path.exists(path):
                self.sounds[sound_name] = pygame.mixer.Sound(path)
            else:
                print(f"Warning: Sound file '{filename}' not found at {path}.")

    def play_sound(self, sound_name):
        channel: pygame.mixer.Channel
        if sound_name in self.active_channels:
            channel = self.active_channels[sound_name]
            if not channel.get_busy():
                sound: pygame.mixer.Sound = self.sounds.get(sound_name)
            else:
                return
        else:
            sound: pygame.mixer.Sound = self.sounds.get(sound_name)
        
        if sound:
            self.active_channels[sound_name] = sound.play()
        else:
            print(f"Warning: Sound '{sound_name}' not loaded.")

    def stop_sound(self, sound_name):
        sound = self.sounds.get(sound_name)
        if sound:
            sound.stop()

    def play_background_music(self, loops=-1):
        bg_sound = self.sounds.get("background")
        if bg_sound:
            bg_sound.play(loops=loops)

    def stop_all_sounds(self):
        # pygame.mixer.stop()
        # Stop all sounds except background music
        for sound_name, sound in self.sounds.items():
            if sound_name != "background":  # Don't stop background music
                sound.stop()
        pygame.mixer.music.stop()
