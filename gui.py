import pygame, time, sys
import backend

# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted

# from pygame.locals import *
# https://www.youtube.com/watch?v=Rvcyf4HsWiw code to take in text input comes from this youtube video


pygame.init()
width, height = 800, 800
backgroundColor = 41, 78, 128

stateData = backend.Data()  # making a data object

screen = pygame.display.set_mode((width, height))

gameDisplay = pygame.display.set_mode((width, height))
# displays the window??
pygame.display.set_caption('COVID STATS')

# covid stats header
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 0)  # this is the color BLACK
# assigning values to X and Y variable
X = 800
Y = 600
display_surface = pygame.display.set_mode((X, Y))
# set the pygame window name
pygame.display.set_caption('COVID STATS')
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 50)
# create a text surface object,
# on which text is drawn on it.
text = font.render('COVID-19 STATS', True, white)
textRect = text.get_rect()
# set the center of the rectangular object.
textRect.center = (X // 2, Y // 10)

# getting text input
base_font = pygame.font.Font(None, 32);
user_text = ' '
input_rect = pygame.Rect(150, 100, 140, 32)
color_active = pygame.Color('lightskyblue3');
color_passive = pygame.Color('grey15');
color = color_passive;
input_rect.center = (input_rect.x + input_rect.width * 2, input_rect.y + input_rect.height * 2)
active = False;

font2 = pygame.font.Font('freesansbold.ttf', 12)
# all state data text
allStateText = font2.render('List All States', True, blue)
allStateRect = allStateText.get_rect()
allStateBoxRect = pygame.Rect(width / 4, 375, 400, 20)  # create a rect just for All state box
allStateRect.center = (allStateBoxRect.x + allStateBoxRect.width / 2, allStateBoxRect.y + allStateBoxRect.height / 2)

# Alphabetical order textbox
alphabeticalText = font2.render('Sort Alphabetically', True, blue)
alphabeticalTextRect = alphabeticalText.get_rect()
alphabeticalBoxRect = pygame.Rect(width / 4, 400, 400, 20)  # create a rect just for alphabetical state box
alphabeticalTextRect.center = (alphabeticalBoxRect.x + alphabeticalBoxRect.width / 2, alphabeticalBoxRect.y + alphabeticalBoxRect.height / 2)

# Highest cases textbox
# we're going to use the same font
highestCasesText = font2.render('Sort High to Low', True, blue)
highestCasesRect = highestCasesText.get_rect()
highestCasesBoxRect = pygame.Rect(width / 4, 425, 400, 20)  # rectangle for lowest cases
highestCasesRect.center = (highestCasesBoxRect.x + highestCasesBoxRect.width / 2, highestCasesBoxRect.y + highestCasesBoxRect.height / 2)

# lowest cases textbox
lowestCasesText = font2.render('Sort Low to High', True, blue)
lowestCasesRect = lowestCasesText.get_rect()
lowestCasesBoxRect = pygame.Rect(width / 4, 450, 400, 20)
lowestCasesRect.center = (lowestCasesBoxRect.x + lowestCasesBoxRect.width / 2, lowestCasesBoxRect.y + lowestCasesBoxRect.height / 2)

# searchbar text
black = 0, 0, 0
searchText = font2.render('Search', True, backgroundColor)
searchRect = searchText.get_rect()
searchBarRect = pygame.Rect(input_rect.x, input_rect.y + input_rect.height, input_rect.width - 40, input_rect.height)
searchRect.center = (searchBarRect.x + searchBarRect.width / 2, searchBarRect.y + searchBarRect.height / 2)

allStateDataRect = pygame.Rect(10, searchBarRect.y + searchBarRect.height, width * 2, searchBarRect.height * 3)
allStateDataRect.center = (10, height / 2)

while True:
    allStateClicked = False
    alphabetClicked = False
    highestClicked = False
    lowestClicked = False
    searchClicked = False

    # getting text input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  # mouseclick
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
            # if one of the four lower buttons are clicked
            if allStateRect.collidepoint(event.pos):
                allStateClicked = True
            if searchRect.collidepoint(event.pos):
                searchClicked = True
            if alphabeticalBoxRect.collidepoint(event.pos):
                alphabetClicked = True
            if highestCasesRect.collidepoint(event.pos):
                highestClicked = True
            if lowestCasesRect.collidepoint(event.pos):
                lowestClicked = True

        if event.type == pygame.KEYDOWN:  # checks if any button was pressed
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]  # very first character one b4 last
                else:
                    user_text += event.unicode  # takes in characters

    screen.fill(backgroundColor)

    display_surface.blit(text, textRect)

    # drawing text input
    if active:
        color = color_active
    else:
        color = color_passive
    pygame.draw.rect(screen, color, input_rect, 2)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)

    # states should be in user_text
    if searchClicked == True:
        print(stateData.getCases(user_text.strip()))

    # draw search bar
    pygame.draw.rect(display_surface, white, searchBarRect)
    display_surface.blit(searchText, searchRect)
    # draw home bar

    if allStateClicked == True:
        # Retrieve dictionary to print
        states = stateData.data
        for key, val in states.items():
            print (key, val)

    elif alphabetClicked == True:
        # Retrieve sorted dictionary to print
        states = stateData.sortAlphabetical()
        for key, val in states.items():
            print(key, val)


    elif highestClicked == True:
        # Retrieve sorted dictionary to print
        states = stateData.sortHighToLow()
        for key, val in states.items():
            print(key, val)

    elif lowestClicked == True:
        # Retrieve sorted dictionary to print
        states = stateData.sortLowToHigh()
        for key, val in states.items():
            print(key, val)

    else:
        # below draws 4 rectangles at the bottom & text inside
        pygame.draw.rect(display_surface, white, allStateBoxRect)
        pygame.draw.rect(display_surface, white, alphabeticalBoxRect)
        pygame.draw.rect(display_surface, white, highestCasesBoxRect)
        pygame.draw.rect(display_surface, white, lowestCasesBoxRect)

        # draws text for boxes
        display_surface.blit(allStateText, allStateRect)
        display_surface.blit(alphabeticalText, alphabeticalTextRect)
        display_surface.blit(highestCasesText, highestCasesRect)
        display_surface.blit(lowestCasesText, lowestCasesRect)

    pygame.display.flip()
    pygame.display.update()
    time.sleep(10 / 1000)
    # copying the text surface object to the display
    # surface object at the center coordinate.

