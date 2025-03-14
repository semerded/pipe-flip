import sys
import pygame
from src import data
from src.enums import colorBlindType
from src.color import Color
from src.widgets.button import Button

pygame.display.set_caption("Pause Menu")

font = pygame.font.Font(None, 36)

options = ["Change Keybinds", "Colorblind Mode"]
submenu_active = {1: None, 2: None}
awaiting_keybind = {1: None, 2: None}

keybinds = {
    1: {"Left": pygame.K_a, "Right": pygame.K_d, "Jump": pygame.K_SPACE},
    2: {"Left": pygame.K_LEFT, "Right": pygame.K_RIGHT, "Jump": pygame.K_UP},
}

# Main menu buttons for Player 1 and Player 2
player1_button1 = Button(x=data.window_width // 2 - 100, y=100, width=200, height=40, color=Color.GRAY, border_radius=-1)
player1_button1.set_text(options[0], font, Color.BLACK)

player1_button2 = Button(x=data.window_width // 2 - 100, y=150, width=200, height=40, color=Color.GRAY, border_radius=-1)
player1_button2.set_text(options[1], font, Color.BLACK)

player2_button1 = Button(x=data.window_width // 2 - 100, y=data.window_height - 250, width=200, height=40, color=Color.GRAY, border_radius=-1)
player2_button1.set_text(options[0], font, Color.BLACK)

player2_button2 = Button(x=data.window_width // 2 - 100, y=data.window_height - 200, width=200, height=40, color=Color.GRAY, border_radius=-1)
player2_button2.set_text(options[1], font, Color.BLACK)

# Keybind buttons for Player 1
keybind_button1_p1 = Button(x=data.window_width // 2 - 100, y=data.window_height // 2 - 50, width=200, height=40, color=Color.GRAY, border_radius=-1)
keybind_button1_p1.set_text(f"Left: {pygame.key.name(keybinds[1]['Left'])}", font, Color.BLACK)

keybind_button2_p1 = Button(x=data.window_width // 2 - 100, y=data.window_height // 2, width=200, height=40, color=Color.GRAY, border_radius=-1)
keybind_button2_p1.set_text(f"Right: {pygame.key.name(keybinds[1]['Right'])}", font, Color.BLACK)

keybind_button3_p1 = Button(x=data.window_width // 2 - 100, y=data.window_height // 2 + 50, width=200, height=40, color=Color.GRAY, border_radius=-1)
keybind_button3_p1.set_text(f"Jump: {pygame.key.name(keybinds[1]['Jump'])}", font, Color.BLACK)

# Keybind buttons for Player 2
keybind_button1_p2 = Button(x=data.window_width // 2 - 100, y=data.window_height // 2 - 50, width=200, height=40, color=Color.GRAY, border_radius=-1)
keybind_button1_p2.set_text(f"Left: {pygame.key.name(keybinds[2]['Left'])}", font, Color.BLACK)

keybind_button2_p2 = Button(x=data.window_width // 2 - 100, y=data.window_height // 2, width=200, height=40, color=Color.GRAY, border_radius=-1)
keybind_button2_p2.set_text(f"Right: {pygame.key.name(keybinds[2]['Right'])}", font, Color.BLACK)

keybind_button3_p2 = Button(x=data.window_width // 2 - 100, y=data.window_height // 2 + 50, width=200, height=40, color=Color.GRAY, border_radius=-1)
keybind_button3_p2.set_text(f"Jump: {pygame.key.name(keybinds[2]['Jump'])}", font, Color.BLACK)

# Back buttons for Player 1 and Player 2
back_button_p1 = Button(x=data.window_width - 150, y=data.window_height // 4 + 100, width=100, height=40, color=Color.GRAY, border_radius=-1)
back_button_p1.set_text("Back", font, Color.BLACK)

back_button_p2 = Button(x=data.window_width - 150, y=(3 * data.window_height) // 4 + 100, width=100, height=40, color=Color.GRAY, border_radius=-1)
back_button_p2.set_text("Back", font, Color.BLACK)

# Back to game button
back_to_game_button = Button(x=data.window_width // 2 - 100, y=data.window_height // 2 - 50, width=200, height=40, color=Color.GRAY, border_radius=-1)
back_to_game_button.set_text("Back to Game", font, Color.BLACK)

# Exit game button
exit_game_button = Button(x=data.window_width // 2 - 100, y=data.window_height // 2 + 50, width=200, height=40, color=Color.GRAY, border_radius=-1)
exit_game_button.set_text("Exit Game", font, Color.BLACK)


def execute_option(player, option):
    """Handles button interactions and opens submenus"""
    global submenu_active
    if option == "Change Keybinds":
        submenu_active[player] = "keybinds"
        print(f"Player {player} selected 'Change Keybinds'")
    elif option == "Colorblind Mode":
        submenu_active[player] = "colorblind"
        print(f"Player {player} selected 'Colorblind Mode'")


def draw_submenu(player):
    """Draws the submenu for the selected player"""
    data.window.fill(Color.BLACK)

    y_offset = data.window_height // 4 if player == 1 else (3 * data.window_height) // 4

    title_text = "Keybind Settings" if submenu_active[player] == "keybinds" else "Colorblind Mode" if submenu_active[player] == "colorblind" else "Settings"
    text = font.render(f"Player {player} - {title_text}", True, Color.WHITE)
    text_rect = text.get_rect(center=(data.window_width // 2, y_offset - 100))
    data.window.blit(text, text_rect)

    if submenu_active[player] == "keybinds":
        # Draw Keybind buttons for the respective player
        keybind_buttons = [keybind_button1_p1, keybind_button2_p1, keybind_button3_p1] if player == 1 else [keybind_button1_p2, keybind_button2_p2, keybind_button3_p2]
        for button in keybind_buttons:
            button.draw()

        if awaiting_keybind[player]:
            waiting_text = f"Press a new key for '{awaiting_keybind[player]}'"
            waiting_surface = font.render(waiting_text, True, Color.WHITE)
            waiting_rect = waiting_surface.get_rect(center=(data.window_width // 2, y_offset + 150))
            data.window.blit(waiting_surface, waiting_rect)

        y_offset += len(keybind_buttons) * 50
        back_button_p1.rect.x = data.window_width - 150
        back_button_p1.rect.y = y_offset + 10
        back_button_p1.draw()

    if submenu_active[player] == "colorblind":
        selected_mode = getattr(colorBlindType, f"player{player}_mode", colorBlindType.none)
        selected_mode_text = f"Current Mode: {selected_mode.name.capitalize()}"
        mode_text = font.render(selected_mode_text, True, Color.WHITE)
        mode_rect = mode_text.get_rect(center=(data.window_width // 2, y_offset - 50))
        data.window.blit(mode_text, mode_rect)

        back_button_p1.rect.x = data.window_width // 2 + 150
        back_button_p1.rect.y = y_offset - 50
        back_button_p1.draw()

        for i, mode in enumerate(colorBlindType):
            mode_name = mode.name.capitalize()
            mode_button = Button(x=data.window_width // 2 - 100, y=y_offset + i * 50, width=200, height=40, color=Color.GRAY, border_radius=-1)
            mode_button.set_text(mode_name, font, Color.BLACK)
            mode_button.draw()

        y_offset += len(colorBlindType) * 50

    if submenu_active[player] not in ["keybinds", "colorblind"]:
        back_button_p1.rect.x = data.window_width - 150
        back_button_p1.rect.y = y_offset + 10
        back_button_p1.draw()


def menu():
    """Main menu function"""
    running = True
    handle_menu_events()
    data.window.fill(Color.BLACK)

    for player in submenu_active:
        if submenu_active[player]:
            draw_submenu(player)
            continue

    if submenu_active[1] is None:
        # Draw Player 1 buttons
        player1_button1.draw()
        player1_button2.draw()
        back_to_game_button.draw()
        exit_game_button.draw()

    pygame.draw.line(
        data.window, Color.WHITE,
        (0, data.window_height // 2),
        (data.window_width, data.window_height // 2), 2
    )

    if submenu_active[2] is None:
        # Draw Player 2 buttons
        player2_button1.draw()
        player2_button2.draw()

    pygame.display.flip()


def handle_menu_events():
    """Handles button clicks"""
    global awaiting_keybind
    if submenu_active[1] is None:  # Only allow Player 1 buttons when no submenu is active
        if player1_button1.is_clicked():
            execute_option(1, options[0])
        elif player1_button2.is_clicked():
            execute_option(1, options[1])

    if submenu_active[2] is None:  # Only allow Player 2 buttons when no submenu is active
        if player2_button1.is_clicked():
            execute_option(2, options[0])
        elif player2_button2.is_clicked():
            execute_option(2, options[1])

    if back_button_p1.is_clicked():
        submenu_active[1] = None
        awaiting_keybind[1] = None
        print("Returning to main menu for Player 1!")

    if back_button_p2.is_clicked():
        submenu_active[2] = None
        awaiting_keybind[2] = None
        print("Returning to main menu for Player 2!")

    if back_to_game_button.is_clicked():
        print("Returning to the game!")
        return

    if exit_game_button.is_clicked():
        print("Exiting the game!")
        pygame.quit()
        sys.exit()
