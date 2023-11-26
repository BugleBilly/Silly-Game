import pygame
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
BG_COLOR = (0, 0, 0)  # Black color
BUTTON_COLOR = (150, 150, 150)  # Button color
TEXT_COLOR = (255, 255, 255)  # White color for text
FONT_SIZE = 36

# Texts
question_text = "Is Billy cool?"
yes_text = "Yes"
no_text = "No"

# Load images
yes_image = pygame.image.load("happybilly.jpg")  # Replace with the actual file path of your image
yes_image_rect = yes_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

no_image = pygame.image.load("sadbilly.jpg")  # Replace with the actual file path of your image
no_image_rect = no_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("True or False Game")

font = pygame.font.SysFont(None, FONT_SIZE)  # Default system font with specified size

# Calculate text sizes and positions
question_text_render = font.render(question_text, True, TEXT_COLOR)
question_text_rect = question_text_render.get_rect(center=(WIDTH // 2, HEIGHT // 4))

yes_text_render = font.render(yes_text, True, TEXT_COLOR)
yes_text_rect = yes_text_render.get_rect(center=(WIDTH // 4, HEIGHT // 2))

no_text_render = font.render(no_text, True, TEXT_COLOR)
no_text_rect = no_text_render.get_rect(center=(3 * WIDTH // 4, HEIGHT // 2))

clock = pygame.time.Clock()

# Flags
show_yes_image = False
show_no_image = False

running = True
while running:
    window.fill(BG_COLOR)  # Fill the window with the background color

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Check if the mouse click is on the buttons
            if yes_text_rect.collidepoint(mouse_pos):
                show_yes_image = True
            elif no_text_rect.collidepoint(mouse_pos):
                show_no_image = True

    # Display the question
    window.blit(question_text_render, question_text_rect)

    # Create clickable buttons for Yes and No
    yes_button = pygame.draw.rect(window, BUTTON_COLOR, yes_text_rect)
    no_button = pygame.draw.rect(window, BUTTON_COLOR, no_text_rect)

    # Display Yes and No texts on buttons
    window.blit(yes_text_render, yes_text_rect)
    window.blit(no_text_render, no_text_rect)

    # Display images based on the button clicked
    if show_yes_image:
        window.blit(yes_image, yes_image_rect)
    elif show_no_image:
        window.blit(no_image, no_image_rect)

    pygame.display.update()
    clock.tick(60)

# After exiting the loop, quit Pygame
pygame.quit()
