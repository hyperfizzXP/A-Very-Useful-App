#A Very Useful App
#Created by hyperfizz XP

from tkinter import *
from tkinter import colorchooser
import os
import random
from datetime import datetime
from datetime import date

Colour = "#3639CC"
Font = "Fixedsys"
FontBig = "Fixedsys 20"
Card1 = 0
Card2 = 0

def RollDice():
    global DiceWindow
    
    DiceWindow = Toplevel(MainWindow)
    DiceWindow.title("Roll a Dice")
    DiceWindow.iconbitmap("Dice.ico")
    DiceWindow.geometry("350x200")
    DiceWindow.configure(bg = Colour)
    DiceWindow.resizable(False, False)

    DiceImageLabel = Label(DiceWindow, image = DiceImage, bg = Colour).pack(pady = 2)
    RollDiceLabel = Label(DiceWindow, text = "Roll a dice", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)

    RollButton = Button(DiceWindow, text = "Roll Dice", font = Font, bg = Colour, fg = "White", command = lambda: [RollingDice()]).pack(pady = 2)

def RollingDice():
    DiceWindow.destroy()

    DiceResult = random.randint(1, 6)

    RollDiceWindow = Toplevel(MainWindow)
    RollDiceWindow.title("Roll a Dice")
    RollDiceWindow.iconbitmap("Dice.ico")
    RollDiceWindow.geometry("350x200")
    RollDiceWindow.configure(bg = Colour)
    RollDiceWindow.resizable(False, False)

    if DiceResult == 1:
        ResultLabel = Label(RollDiceWindow, text = "Dice Says: 1", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)
        DiceLabel = Label(RollDiceWindow, image = Dice1Image, bg = Colour).pack(pady = 2)

    elif DiceResult == 2:
        ResultLabel = Label(RollDiceWindow, text = "Dice Says: 2", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)
        DiceLabel = Label(RollDiceWindow, image = Dice2Image, bg = Colour).pack(pady = 2)

    elif DiceResult == 3:
        ResultLabel = Label(RollDiceWindow, text = "Dice Says: 3", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)
        DiceLabel = Label(RollDiceWindow, image = Dice3Image, bg = Colour).pack(pady = 2)

    elif DiceResult == 4:
        ResultLabel = Label(RollDiceWindow, text = "Dice Says: 4", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)
        DiceLabel = Label(RollDiceWindow, image = Dice4Image, bg = Colour).pack(pady = 2)

    elif DiceResult == 5:
        ResultLabel = Label(RollDiceWindow, text = "Dice Says: 5", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)
        DiceLabel = Label(RollDiceWindow, image = Dice5Image, bg = Colour).pack(pady = 2)

    elif DiceResult == 6:
        ResultLabel = Label(RollDiceWindow, text = "Dice Says: 6", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)
        DiceLabel = Label(RollDiceWindow, image = Dice6Image, bg = Colour).pack(pady = 2)
        
    CloseButton = Button(RollDiceWindow, image = CloseImage, bg = Colour, command = lambda: [RollDiceWindow.destroy()]).pack(pady = 2)

def FlipCoin():
    global CoinWindow

    CoinWindow = Toplevel(MainWindow)
    CoinWindow.title("Flip a Coin")
    CoinWindow.iconbitmap("Coin.ico")
    CoinWindow.geometry("350x200")
    CoinWindow.configure(bg = Colour)
    CoinWindow.resizable(False, False)

    CoinImageLabel = Label(CoinWindow, image = CoinImage, bg = Colour).pack(pady = 2)
    FlipCoinLabel = Label(CoinWindow, text = "Flip a Coin", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)

    FlipButton = Button(CoinWindow, text = "Flip Coin", font = Font, bg = Colour, fg = "White", command = lambda: [FlippingCoin()]).pack(pady = 2)

def FlippingCoin():
    CoinWindow.destroy()

    CoinResult = random.randint(1, 2)

    FlipCoinWindow = Toplevel(MainWindow)
    FlipCoinWindow.title("Flip a Coin")
    FlipCoinWindow.iconbitmap("Coin.ico")
    FlipCoinWindow.geometry("350x200")
    FlipCoinWindow.configure(bg = Colour)
    FlipCoinWindow.resizable(False, False)

    if CoinResult == 1:
        ResultLabel = Label(FlipCoinWindow, text = "Coin Says: Heads", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)
        CoinLabel = Label(FlipCoinWindow, image = CoinHeadsImage, bg = Colour).pack(pady = 2)

    elif CoinResult == 2:
        ResultLabel = Label(FlipCoinWindow, text = "Coin Says: Tails", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)
        CoinLabel = Label(FlipCoinWindow, image = CoinTailsImage, bg = Colour).pack(pady = 2)

    CloseButton = Button(FlipCoinWindow, image = CloseImage, bg = Colour, command = lambda: [FlipCoinWindow.destroy()]).pack(pady = 2)

def ColourPicker():
    global ColourWindow
    
    ColourWindow = Toplevel(MainWindow)
    ColourWindow.title("Colour Picker")
    ColourWindow.iconbitmap("ColourPicker.ico")
    ColourWindow.geometry("350x200")
    ColourWindow.configure(bg = Colour)
    ColourWindow.resizable(False, False)

    ColourImageLabel = Label(ColourWindow, image = ColourImage, bg = Colour).pack(pady = 2)
    ColourLabel = Label(ColourWindow, text = "Colour Picker", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)

    ColourPickButton = Button(ColourWindow, text = "Pick a Colour", font = Font, bg = Colour, fg = "White", command = lambda: [ChooseColour()]).pack(pady = 2)

def ChooseColour():
    ColourWindow.destroy()

    global ColourCode
    
    ColourCode = colorchooser.askcolor(title = "Choose a Colour")

    ShowColour()

def ShowColour():
    ShowColourWindow = Toplevel(MainWindow)
    ShowColourWindow.title("Colour Picker")
    ShowColourWindow.iconbitmap("ColourPicker.ico")
    ShowColourWindow.geometry("350x200")
    ShowColourWindow.configure(bg = Colour)
    ShowColourWindow.resizable(False, False)

    ColourImageLabel = Label(ShowColourWindow, image = ColourImage, bg = Colour).pack(pady = 2)
    ShowColourLabel = Label(ShowColourWindow, text = ColourCode, font = FontBig, bg = Colour, fg = "White").pack(pady = 2)

    CloseButton = Button(ShowColourWindow, image = CloseImage, bg = Colour, command = lambda: [ShowColourWindow.destroy()]).pack(pady = 2)

def TellTime():
    TimeWindow = Toplevel(MainWindow)
    TimeWindow.title("Tell the Time")
    TimeWindow.iconbitmap("Clock.ico")
    TimeWindow.geometry("350x200")
    TimeWindow.configure(bg = Colour)
    TimeWindow.resizable(False, False)

    now = datetime.now()
    CurrentTime = now.strftime("%H:%M:%S")

    TimeImageLabel = Label(TimeWindow, image = TimeImage, bg = Colour).pack(pady = 2)
    TellTimeLabel = Label(TimeWindow, text = "The Current Time\nis " + CurrentTime, font = FontBig, bg = Colour, fg = "White").pack(pady = 2)

    CloseButton = Button(TimeWindow, image = CloseImage, bg = Colour, command = lambda: [TimeWindow.destroy()]).pack(pady = 2)

def Calendar():
    CalendarWindow = Toplevel(MainWindow)
    CalendarWindow.title("Calendar")
    CalendarWindow.iconbitmap("Calendar.ico")
    CalendarWindow.geometry("350x200")
    CalendarWindow.configure(bg = Colour)
    CalendarWindow.resizable(False, False)

    
    CurrentDate = date.today()

    CalendarImageLabel = Label(CalendarWindow, image = CalendarImage, bg = Colour).pack(pady = 2)
    DateLabel = Label(CalendarWindow, text = "The Current Date\nis " + str(CurrentDate), font = FontBig, bg = Colour, fg = "White").pack(pady = 2)

    CloseButton = Button(CalendarWindow, image = CloseImage, bg = Colour, command = lambda: [CalendarWindow.destroy()]).pack(pady = 2)

def HigherOrLower():
    global CardsWindow
    global Card1
    global Card2

    Card1 = random.randint(1, 10)
    Card2 = random.randint(1, 10)
    
    CardsWindow = Toplevel(MainWindow)
    CardsWindow.title("Higher or Lower")
    CardsWindow.iconbitmap("Card.ico")
    CardsWindow.geometry("378x220")
    CardsWindow.configure(bg = Colour)
    CardsWindow.resizable(False, False)

    CardImageLabel = Label(CardsWindow, image = CardImage, bg = Colour).grid(column = 1, row = 0)
    HigherLowerLabel = Label(CardsWindow, text = "Higher or Lower?", font = FontBig, bg = Colour, fg = "White").grid(column = 1, row = 1)

    if Card1 == 1:
        Card1Label = Label(CardsWindow, image = Card1Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(CardsWindow, text = "Ace", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 2:
        Card1Label = Label(CardsWindow, image = Card2Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(CardsWindow, text = "2", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 3:
        Card1Label = Label(CardsWindow, image = Card3Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(CardsWindow, text = "3", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 4:
        Card1Label = Label(CardsWindow, image = Card4Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(CardsWindow, text = "4", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 5:
        Card1Label = Label(CardsWindow, image = Card5Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(CardsWindow, text = "5", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 6:
        Card1Label = Label(CardsWindow, image = Card6Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(CardsWindow, text = "6", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 7:
        Card1Label = Label(CardsWindow, image = Card7Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(CardsWindow, text = "7", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 8:
        Card1Label = Label(CardsWindow, image = Card8Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(CardsWindow, text = "8", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 9:
        Card1Label = Label(CardsWindow, image = Card9Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(CardsWindow, text = "9", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 10:
        Card1Label = Label(CardsWindow, image = Card10Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(CardsWindow, text = "10", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)

    UnknownCardLabel = Label(CardsWindow, image = CardBackImage, bg = Colour).grid(column = 2, row = 2)
    UnknownLabel = Label(CardsWindow, text = "?", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)

    HigherButton = Button(CardsWindow, text = "Higher", font = Font, bg = Colour, fg = "White", width = 6, command = lambda: [ChooseHigher()]).grid(column = 0, row = 4)
    LowerButton = Button(CardsWindow, text = "Lower", font = Font, bg = Colour, fg = "White", width = 6, command = lambda: [ChooseLower()]).grid(column = 2, row = 4)

    HigherOrLowerLabel = Label(CardsWindow, text = "Is the card on the left\nhigher or lower than\nthe card on the right?", font = Font, bg = Colour, fg = "White").grid(column = 1, row = 5)

def ChooseHigher():
    CardsWindow.destroy()
    HigherWinLose()

def ChooseLower():
    CardsWindow.destroy()
    LowerWinLose()

def HigherWinLose():
    global HigherWindow
    
    HigherWindow = Toplevel(MainWindow)
    HigherWindow.title("Higher or Lower")
    HigherWindow.iconbitmap("Card.ico")
    HigherWindow.geometry("350x220")
    HigherWindow.configure(bg = Colour)
    HigherWindow.resizable(False, False)

    CardImageLabel = Label(HigherWindow, image = CardImage, bg = Colour).grid(column = 1, row = 0)
    if Card1 == 1:
        Card1Label = Label(HigherWindow, image = Card1Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(HigherWindow, text = "Ace", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 2:
        Card1Label = Label(HigherWindow, image = Card2Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(HigherWindow, text = "2", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 3:
        Card1Label = Label(HigherWindow, image = Card3Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(HigherWindow, text = "3", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 4:
        Card1Label = Label(HigherWindow, image = Card4Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(HigherWindow, text = "4", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 5:
        Card1Label = Label(HigherWindow, image = Card5Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(HigherWindow, text = "5", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 6:
        Card1Label = Label(HigherWindow, image = Card6Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(HigherWindow, text = "6", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 7:
        Card1Label = Label(HigherWindow, image = Card7Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(HigherWindow, text = "7", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 8:
        Card1Label = Label(HigherWindow, image = Card8Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(HigherWindow, text = "8", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 9:
        Card1Label = Label(HigherWindow, image = Card9Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(HigherWindow, text = "9", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 10:
        Card1Label = Label(HigherWindow, image = Card10Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(HigherWindow, text = "10", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)

    if Card2 == 1:
        Card1Label = Label(HigherWindow, image = Card1Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(HigherWindow, text = "Ace", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 2:
        Card1Label = Label(HigherWindow, image = Card2Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(HigherWindow, text = "2", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 3:
        Card1Label = Label(HigherWindow, image = Card3Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(HigherWindow, text = "3", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 4:
        Card1Label = Label(HigherWindow, image = Card4Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(HigherWindow, text = "4", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 5:
        Card1Label = Label(HigherWindow, image = Card5Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(HigherWindow, text = "5", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 6:
        Card1Label = Label(HigherWindow, image = Card6Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(HigherWindow, text = "6", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 7:
        Card1Label = Label(HigherWindow, image = Card7Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(HigherWindow, text = "7", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 8:
        Card1Label = Label(HigherWindow, image = Card8Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(HigherWindow, text = "8", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 9:
        Card1Label = Label(HigherWindow, image = Card9Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(HigherWindow, text = "9", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 10:
        Card1Label = Label(HigherWindow, image = Card10Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(HigherWindow, text = "10", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)

    if Card1 >= Card2:
        WinLabel = Label(HigherWindow, text = "Correct, Higher!", font = FontBig, bg = Colour, fg = "White").grid(column = 1, row = 1)

    else:
        WinLabel = Label(HigherWindow, text = "Wrong, Lower!", font = FontBig, bg = Colour, fg = "White").grid(column = 1, row = 1)

    PlayAgainButton = Button(HigherWindow, text = "Play Again", font = Font, bg = Colour, fg = "White", command = lambda: [PlayAgainHigher(Card1, Card2)]).grid(column = 1, row = 4)
    CloseButton = Button(HigherWindow, image = CloseImage, bg = Colour, fg = "White", command = lambda: [HigherWindow.destroy()]).grid(column = 1, row = 5)
        
def LowerWinLose():
    global LowerWindow
    
    LowerWindow = Toplevel(MainWindow)
    LowerWindow.title("Higher or Lower")
    LowerWindow.iconbitmap("Card.ico")
    LowerWindow.geometry("350x220")
    LowerWindow.configure(bg = Colour)
    LowerWindow.resizable(False, False)
    
    CardImageLabel = Label(LowerWindow, image = CardImage, bg = Colour).grid(column = 1, row = 0)
    if Card1 == 1:
        Card1Label = Label(LowerWindow, image = Card1Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(LowerWindow, text = "Ace", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 2:
        Card1Label = Label(LowerWindow, image = Card2Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(LowerWindow, text = "2", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 3:
        Card1Label = Label(LowerWindow, image = Card3Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(LowerWindow, text = "3", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 4:
        Card1Label = Label(LowerWindow, image = Card4Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(LowerWindow, text = "4", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 5:
        Card1Label = Label(LowerWindow, image = Card5Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(LowerWindow, text = "5", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 6:
        Card1Label = Label(LowerWindow, image = Card6Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(LowerWindow, text = "6", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 7:
        Card1Label = Label(LowerWindow, image = Card7Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(LowerWindow, text = "7", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 8:
        Card1Label = Label(LowerWindow, image = Card8Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(LowerWindow, text = "8", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 9:
        Card1Label = Label(LowerWindow, image = Card9Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(LowerWindow, text = "9", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)
    elif Card1 == 10:
        Card1Label = Label(LowerWindow, image = Card10Image, bg = Colour).grid(column = 0, row = 2)
        NumberLabel = Label(LowerWindow, text = "10", font = FontBig, bg = Colour, fg = "White").grid(column = 0, row = 3)

    if Card2 == 1:
        Card1Label = Label(LowerWindow, image = Card1Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(LowerWindow, text = "Ace", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 2:
        Card1Label = Label(LowerWindow, image = Card2Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(LowerWindow, text = "2", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 3:
        Card1Label = Label(LowerWindow, image = Card3Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(LowerWindow, text = "3", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 4:
        Card1Label = Label(LowerWindow, image = Card4Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(LowerWindow, text = "4", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 5:
        Card1Label = Label(LowerWindow, image = Card5Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(LowerWindow, text = "5", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 6:
        Card1Label = Label(LowerWindow, image = Card6Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(LowerWindow, text = "6", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 7:
        Card1Label = Label(LowerWindow, image = Card7Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(LowerWindow, text = "7", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 8:
        Card1Label = Label(LowerWindow, image = Card8Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(LowerWindow, text = "8", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 9:
        Card1Label = Label(LowerWindow, image = Card9Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(LowerWindow, text = "9", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)
    elif Card2 == 10:
        Card1Label = Label(LowerWindow, image = Card10Image, bg = Colour).grid(column = 2, row = 2)
        NumberLabel = Label(LowerWindow, text = "10", font = FontBig, bg = Colour, fg = "White").grid(column = 2, row = 3)

    if Card1 <= Card2:
        WinLabel = Label(LowerWindow, text = "Correct, Lower!", font = FontBig, bg = Colour, fg = "White").grid(column = 1, row = 1)

    else:
        WinLabel = Label(LowerWindow, text = "Wrong, Higher!", font = FontBig, bg = Colour, fg = "White").grid(column = 1, row = 1)

    PlayAgainButton = Button(LowerWindow, text = "Play Again", font = Font, bg = Colour, fg = "White", command = lambda: [PlayAgainLower(Card1, Card2)]).grid(column = 1, row = 4)
    CloseButton = Button(LowerWindow, image = CloseImage, bg = Colour, fg = "White", command = lambda: [LowerWindow.destroy()]).grid(column = 1, row = 5)

def PlayAgainHigher(Card1, Card2):
    HigherWindow.destroy()
    ReassignInt()

def PlayAgainLower(Card1, Card2):
    LowerWindow.destroy()
    ReassignInt()

def ReassignInt():
    Card1 = random.randint(1, 10)
    Card2 = random.randint(1, 10)

    HigherOrLower()

expression = ""
 
def press(num):
    global expression
 
    expression = expression + str(num)
 
    equation.set(expression)
 
 
def equalpress():
    try:
 
        global expression
 
        total = str(eval(expression))
 
        equation.set(total)
 
        expression = ""
 
    except:
 
        equation.set(" error ")
        expression = ""
 
 
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
def Calculator():
    global equation
    
    CalculatorWindow = Toplevel(MainWindow)
    CalculatorWindow.title("Calculator")
    CalculatorWindow.iconbitmap("Calculator.ico")
    CalculatorWindow.geometry("270x185")
    CalculatorWindow.configure(bg = Colour)
    CalculatorWindow.resizable(False, False)
 
    equation = StringVar()
 
    expression_field = Entry(CalculatorWindow, textvariable=equation)
 
    expression_field.grid(columnspan=4, ipadx=70)
 
    button1 = Button(CalculatorWindow, text=' 1 ', bg = Colour, fg = "White",
                    command=lambda: press(1), height=2, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(CalculatorWindow, text=' 2 ', bg = Colour, fg = "White",
                    command=lambda: press(2), height=2, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(CalculatorWindow, text=' 3 ', bg = Colour, fg = "White",
                    command=lambda: press(3), height=2, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(CalculatorWindow, text=' 4 ', bg = Colour, fg = "White",
                    command=lambda: press(4), height=2, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(CalculatorWindow, text=' 5 ', bg = Colour, fg = "White",
                    command=lambda: press(5), height=2, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(CalculatorWindow, text=' 6 ', bg = Colour, fg = "White",
                    command=lambda: press(6), height=2, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(CalculatorWindow, text=' 7 ', bg = Colour, fg = "White",
                    command=lambda: press(7), height=2, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(CalculatorWindow, text=' 8 ', bg = Colour, fg = "White",
                    command=lambda: press(8), height=2, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(CalculatorWindow, text=' 9 ', bg = Colour, fg = "White",
                    command=lambda: press(9), height=2, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(CalculatorWindow, text=' 0 ', bg = Colour, fg = "White",
                    command=lambda: press(0), height=2, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(CalculatorWindow, text=' + ', bg = Colour, fg = "White",
                command=lambda: press("+"), height=2, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(CalculatorWindow, text=' - ', bg = Colour, fg = "White",
                command=lambda: press("-"), height=2, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(CalculatorWindow, text=' × ', bg = Colour, fg = "White",
                    command=lambda: press("*"), height=2, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(CalculatorWindow, text=' ÷ ', bg = Colour, fg = "White",
                    command=lambda: press("/"), height=2, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(CalculatorWindow, text=' = ', bg = Colour, fg = "White",
                command=equalpress, height=2, width=7)
    equal.grid(row=5, column=2)
 
    Decimal= Button(CalculatorWindow, text='.', bg = Colour, fg = "White",
                    command=lambda: press('.'), height=2, width=7)
    Decimal.grid(row=5, column=1)
    
    CalculatorWindow.mainloop()

    
MainWindow = Tk()
MainWindow.title("A Very Useful App")
MainWindow.iconbitmap("Icon.ico")
MainWindow.geometry("350x525")
MainWindow.configure(bg = Colour)

LogoImage = PhotoImage(file = "Logo.png")
DiceImage = PhotoImage(file = "Dice.png")
CoinImage = PhotoImage(file = "Coin.png")
ColourImage = PhotoImage(file = "ColourPicker.png")
CloseImage = PhotoImage(file = "Close.png")
CoinHeadsImage = PhotoImage(file = "CoinHeads.png")
CoinTailsImage = PhotoImage(file = "CoinTails.png")
Dice1Image = PhotoImage(file = "Dice1.png")
Dice2Image = PhotoImage(file = "Dice2.png")
Dice3Image = PhotoImage(file = "Dice3.png")
Dice4Image = PhotoImage(file = "Dice4.png")
Dice5Image = PhotoImage(file = "Dice5.png")
Dice6Image = PhotoImage(file = "Dice6.png")
TimeImage = PhotoImage(file = "Clock.png")
CalendarImage = PhotoImage(file = "Calendar.png")
CardImage = PhotoImage(file = "Card.png")
Card1Image = PhotoImage(file = "CardAce.png")
Card2Image = PhotoImage(file = "Card2.png")
Card3Image = PhotoImage(file = "Card3.png")
Card4Image = PhotoImage(file = "Card4.png")
Card5Image = PhotoImage(file = "Card5.png")
Card6Image = PhotoImage(file = "Card6.png")
Card7Image = PhotoImage(file = "Card7.png")
Card8Image = PhotoImage(file = "Card8.png")
Card9Image = PhotoImage(file = "Card9.png")
Card10Image = PhotoImage(file = "Card10.png")
CardBackImage = PhotoImage(file = "CardBack.png")
CalculatorImage = PhotoImage(file = "Calculator.png")

LogoLabel = Label(MainWindow, image = LogoImage, bg = Colour).pack(pady = 2)
HelloLabel = Label(MainWindow, text = "Hello!!!", font = FontBig, bg = Colour, fg = "White").pack(pady = 2)
MainLabel = Label(MainWindow, text = "What we doin' today, sir?", font = Font, bg = Colour, fg = "White").pack(pady = 2)

RollDiceButton = Button(MainWindow, image = DiceImage, bg = Colour, width = 50, height = 50, command = lambda: [RollDice()]).pack(pady = 2)
FlipCoinButton = Button(MainWindow, image = CoinImage, bg = Colour, width = 50, height = 50, command = lambda: [FlipCoin()]).pack(pady = 2)
ColourPickerButton = Button(MainWindow, image = ColourImage, bg = Colour, width = 50, height = 50, command = lambda: [ColourPicker()]).pack(pady = 2)
TellTimeButton = Button(MainWindow, image = TimeImage, bg = Colour, width = 50, height = 50, command = lambda: [TellTime()]).pack(pady = 2)
CalendarButton = Button(MainWindow, image = CalendarImage, bg = Colour, width = 50, height = 50, command = lambda: [Calendar()]).pack(pady = 2)
CardsButton = Button(MainWindow, image = CardImage, bg = Colour, width = 50, height = 50, command = lambda: [HigherOrLower()]).pack(pady = 2)
CalculatorButton = Button(MainWindow, image = CalculatorImage, bg = Colour, width = 50, height = 50, command = lambda: [Calculator()]).pack(pady = 2)

print("Hello World!")

MainWindow.mainloop()
