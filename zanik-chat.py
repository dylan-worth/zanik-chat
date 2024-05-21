import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import nltk
from nltk.chat.util import Chat, reflections
import pygame
from random import choice

# Initialize Pygame mixer
pygame.mixer.init()

# Load the audio file
pygame.mixer.music.load("./Zanik's_Theme.ogx")
pygame.mixer.music.play(-1)  # Loop the music indefinitely

# Expanded conversation data with new questions
pairs = [
    [r"hi|hello|hey", ["Hello, adventurer! I'm Zanik. How can I assist you today in your RuneScape journey?", ]],
    [r"what is your name\??", ["My name is Zanik, the brave Dorgeshuun warrior.", ]],
    [r"how are you\??", ["I'm always ready for an adventure! How about you?", ]],
    [r"tell me about the Dorgeshuun", ["The Dorgeshuun are a tribe of cave goblins who have lived underground for generations. We're a peaceful folk, but ready to defend ourselves if needed!", ]],
    [r"what is RuneScape\??", ["RuneScape is a vast, magical world full of quests, adventures, and intriguing characters. It's where I come from!", ]],
    [r"bye|goodbye", ["Goodbye, adventurer! May your journeys be safe and prosperous!", ]],
    [r"thanks|thank you|ty", ["You're welcome! How else can I help?", ]],
    [r"where can I (fish|catch) shrimp\??", ["You can fish/catch shrimp at various locations like Lumbridge Swamp, Draynor Village, and Catherby.", ]],
    [r"where can I (fish|catch) trout\??", ["You can fish/catch trout in the River Lum, located at the Barbarian Village, and in the River to the east of Varrock.", ]],
    [r"where can I (fish|catch) salmon\??", ["You can fish/catch salmon in the same places as trout: Barbarian Village and the River to the east of Varrock.", ]],
    [r"where can I (fish|catch) lobster\??", ["You can fish/catch lobster at the Fishing Guild, Catherby, and Karamja.", ]],
    [r"where can I (fish|catch) swordfish\??", ["You can fish/catch swordfish at the Fishing Guild, Catherby, and Karamja.", ]],
    [r"where can I (fish|catch) shark\??", ["You can fish/catch shark at the Fishing Guild, Catherby, and Karamja.", ]],
    [r"(.*)grand exchange(.*)", ["Have you ever been to the Grand Exchange? It's quite the bustling marketplace!", ]],
    [r"(.*)lumbridge(.*)", ["The Lumbridge Castle is one of my favorite places. It's so full of history.", ]],
    [r"(.*)wise old man(.*)", ["Did you know the Wise Old Man once tried to rob a bank? Quite the character!", ]],
    [r"(.*)taverley(.*)", ["I love the peacefulness of Taverley. The druids are always so welcoming.", ]],
    [r"(.*)catherby(.*)", ["If you ever need a break, the Catherby beach is perfect for fishing and relaxing.", ]],
    [r"(.*)fremennik(.*)", ["The Fremennik people are fascinating, aren't they? Such rich traditions and stories.", ]],
    [r"(.*)wilderness(.*)", ["I once had an epic battle in the Wilderness. Dangerous, but thrilling!", ]],
    [r"(.*)herblore(.*)", ["Have you tried making potions with Herblore? It can be very rewarding.", ]],
    [r"(.*)varrock museum(.*)", ["The Varrock Museum is a must-visit if you want to learn about Gielinor's history.", ]],
    [r"(.*)farming(.*)", ["Did you know you can grow your own food in RuneScape? Farming is a useful skill!", ]],
    [r"(.*)monastery(.*)", ["I always find peace when I visit the Monastery just west of Edgeville.", ]],
    [r"(.*)smithing(.*)", ["Smithing your own weapons and armor is a fantastic way to be self-sufficient.", ]],
    [r"(.*)music(.*)", ["The music in RuneScape is so diverse! Each area has its own unique theme.", ]],
    [r"(.*)treasure hunt(.*)", ["Have you ever been on a treasure hunt? Clue scrolls can lead to great adventures.", ]],
    [r"(.*)agility(.*)", ["The agility courses are not only fun but also a great way to stay fit!", ]],
    [r"(.*)dye(.*)", ["Did you know you can dye your gear different colors? FashionScape is real!", ]],
    [r"(.*)firemaking(.*)", ["The Firemaking skill is more useful than people think, especially in the Wintertodt.", ]],
    [r"(.*)gnome stronghold(.*)", ["Have you visited the Gnome Stronghold? Those gnomes are quite innovative.", ]],
    [r"(.*)legends' guild(.*)", ["The Legends' Guild is a place of honor. Only the most experienced adventurers can enter.", ]],
    [r"(.*)seasonal events(.*)", ["RuneScape's seasonal events are always a blast. Have you participated in any?", ]],
    [r"(.*)abyssal(.*)", ["The Abyssal creatures in the Abyss are some of the most dangerous foes you'll face.", ]],
    [r"(.*)lodestones(.*)", ["I love using the lodestones for quick travel. They save so much time!", ]],
    [r"(.*)great orb project(.*)", ["Have you ever played the Great Orb Project? It's a fun and challenging minigame.", ]],
    [r"(.*)morytania(.*)", ["The dungeons beneath Morytania are filled with dark secrets and powerful monsters.", ]],
    [r"(.*)god wars dungeon(.*)", ["If you ever need a challenge, try taking on the bosses in the God Wars Dungeon.", ]],
    [r"how do I start a quest\??", ["You can start a quest by talking to NPCs with a blue star icon on the minimap. They'll give you the details and tasks you need to complete.", ]],
    [r"where can I train my combat skills\??", ["You can train combat skills in various places. For low-level training, try fighting cows and goblins near Lumbridge.", ]],
    [r"how do I join a clan\??", ["To join a clan, you can talk to the Clan Vexillum NPC in any major city, or ask a player who is part of a clan to invite you.", ]],
    [r"where do I get a pickaxe\??", ["You can buy a pickaxe from the general store in Lumbridge or the Dwarven Mine.", ]],
    [r"how do I cook food\??", ["To cook food, you need to use a raw ingredient like fish or meat on a fire or range. There's a range in Lumbridge Castle's kitchen.", ]],
    [r"what are daily challenges\??", ["Daily challenges are tasks given to you each day that offer experience and rewards for completing them. You can find them in your Challenges tab.", ]],
    [r"how do I get to the Grand Exchange\??", ["The Grand Exchange is located in Varrock. You can walk there or use a teleport spell if you have the required magic level.", ]],
    [r"what is the best way to make money\??", ["There are many ways to make money, such as skilling, completing quests, and participating in minigames like the Grand Exchange flipping.", ]],
    [r"where can I mine ores\??", ["You can mine ores in various locations. For low-level ores, try the mining sites near Lumbridge and Varrock.", ]],
    [r"how do I get better armor\??", ["You can get better armor by crafting it through smithing, buying it from shops or other players, or receiving it as drops from monsters.", ]],
    [r"how do I teleport\??", ["You can teleport using teleport spells, which require runes, or by using teleport items like teleport tabs and amulets.", ]],
    [r"what are Slayer tasks\??", ["Slayer tasks are assignments given by Slayer Masters to kill specific types of monsters. Completing these tasks gives Slayer experience and rewards.", ]],
    [r"where can I chop wood\??", ["You can chop wood in various locations. For beginners, try the trees near Lumbridge and Draynor Village.", ]],
    [r"how do I craft items\??", ["Crafting involves using raw materials like leather, gems, or clay at crafting stations. You can start crafting leather items in Al Kharid.", ]],
    [r"what are clans\??", ["Clans are groups of players who team up for activities, events, and socializing. Joining a clan can enhance your RuneScape experience.", ]],
    [r"where can I find fishing spots\??", ["Fishing spots are located near bodies of water. For beginners, try the fishing spots in Lumbridge Swamp or Draynor Village.", ]],
    [r"how do I level up my skills\??", ["You level up your skills by performing activities related to that skill. For example, mine ores to level up Mining or cook food to level up Cooking.", ]],
    [r"what is the Wilderness\??", ["The Wilderness is a dangerous area where players can engage in PvP combat. It's located in the northern part of the map.", ]],
    [r"how do I use the bank\??", ["You can use the bank by finding a bank booth or chest in major cities like Varrock, Falador, and Lumbridge.", ]],
    [r"what are treasure trails\??", ["Treasure trails are clue scrolls that lead you on a treasure hunt. Completing them can reward you with valuable items.", ]],
    [r"how do I make potions\??", ["You can make potions using the Herblore skill. Gather herbs and secondary ingredients, then use them on a vial of water at a bank or herblore shop.", ]],
    [r"where can I buy runes\??", ["You can buy runes from magic shops in Varrock, Port Sarim, and other cities, or craft them using the Runecrafting skill.", ]],
    [r"what are minigames\??", ["Minigames are special activities that offer unique gameplay experiences and rewards. Examples include Pest Control and the TzHaar Fight Pit.", ]],
    [r"how do I train agility\??", ["You can train agility by completing agility courses. The Gnome Stronghold Agility Course is a good starting point for beginners.", ]],
    [r"what are daily spins\??", ["Daily spins are part of the Squeal of Fortune or Treasure Hunter. You can spin the wheel daily for a chance to win prizes.", ]],
    [r"how do I make armor\??", ["You can make armor using the Smithing skill. Mine ores, smelt them into bars, and then use an anvil to smith the bars into armor pieces.", ]],
    [r"what is the best food for healing\??", ["The best food for healing depends on your cooking level. Higher-level foods like sharks and rocktails provide more health restoration.", ]],
    [r"how do I use lodestones\??", ["Lodestones are part of the Home Teleport network. Activate lodestones by visiting them, and then you can teleport to them for free.", ]],
    [r"where can I catch dragonfish\??", ["Dragonfish can be caught in special fishing spots found in higher-level areas like the Fishing Guild and Menaphos.", ]],
    [r"how do I access the RuneScape Wiki\??", ["You can access the RuneScape Wiki by visiting the website runescape.wiki. It's a great resource for all things RuneScape.", ]],
    [r"goblify", ["Let me generate a goblin name for you!", ]],
    [r"what is your combat level\??", ["My Combat level is 41.", ]],
    [r"What is this song|music\??", ["It is called Zanik's Theme, it was released November 12, 2007.", ]],
    [r"how do I unlock this theme\??", ["Zanik's Theme is a music track unlocked during the cutscene of Grubfoot's dream of Yu'biusk during the Land of the Goblins quest. ", ]],
    [r"what is Open881\??", ["Rumors in Dorgeshuun, Open881 is the project that is currently being worked on by Dylan", ]]
]

# Create Chat object
chatbot = Chat(pairs, reflections)

class ZanikChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zanik Chat - RuneScape")
        self.root.configure(bg='#2E2E2E')  # Dark grey background to resemble Dorgeshuun tunnels

        # Load RuneScape font
        self.font = ("runescape_uf", 12)

        # Frame for Zanik's image and chat log
        top_frame = ttk.Frame(root, style='TFrame')
        top_frame.pack(pady=10)

        # Load Zanik's image
        self.zanik_img = Image.open("zanik_face.png")
        self.zanik_img = self.zanik_img.resize((100, 100), Image.LANCZOS)
        self.zanik_photo = ImageTk.PhotoImage(self.zanik_img)

        self.image_label = ttk.Label(top_frame, image=self.zanik_photo, background='#2E2E2E')
        self.image_label.pack(side='left', padx=10)

        self.chat_log = tk.Text(top_frame, state='disabled', width=60, height=20, wrap='word', bg='#3E3E3E', fg='#FFFFFF', font=self.font)
        self.chat_log.pack(side='left', pady=10)

        self.entry_frame = ttk.Frame(root, style='TFrame')
        self.entry_frame.pack(pady=10)

        self.entry_field = ttk.Entry(self.entry_frame, width=70, font=self.font)
        self.entry_field.pack(side='left', padx=10)
        self.entry_field.bind("<Return>", self.send_message)

        self.send_button = ttk.Button(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.pack(side='left')

        self.mute_button = ttk.Button(self.entry_frame, text="Mute", command=self.toggle_mute)
        self.mute_button.pack(side='left')

        self.is_muted = False

        # Goblin name generation
        self.prefixes = ['Beetle', 'Bent', 'Blob', 'Bone', 'Dirt', 'Drip', 'Earth', 'Fat', 'Foul', 'Frog', 'Grass', 'Grub', 'Lump', 'Maggot', 'Moss', 'Mud', 'Roach', 'Slime', 'Slug', 'Small', 'Smelly', 'Snail', 'Snow', 'Snot', 'Stupid', 'Thick', 'Thin', 'Toad', 'Ugly', 'Wart', 'Wood', 'Worm']
        self.body_parts = ['arms', 'beard', 'blood', 'bones', 'bottom', 'brain', 'brains', 'chin', 'ears', 'eye', 'eyes', 'face', 'feet', 'finger', 'fingers', 'fists', 'foot', 'hair', 'hands', 'head', 'knees', 'knuckles', 'legs', 'nails', 'neck', 'nose', 'teeth', 'thighs', 'thumb', 'toes', 'tongue']

    def send_message(self, event=None):
        user_input = self.entry_field.get()
        self.display_message(f"You: {user_input}")

        if user_input.lower() in ["bye", "goodbye", "exit"]:
            self.display_message("Zanik: Goodbye, adventurer! May your journeys be safe and prosperous!")
            self.clear_chat()
            return

        if user_input.lower() == "goblify":
            goblin_name = self.generate_goblin_name()
            self.display_message(f"Zanik: Your goblin name is {goblin_name}")
        else:
            response = chatbot.respond(user_input.lower())
            self.display_message(f"Zanik: {response}")

        self.entry_field.delete(0, tk.END)

    def display_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.config(state='disabled')
        self.chat_log.yview(tk.END)

    def clear_chat(self):
        self.chat_log.config(state='normal')
        self.chat_log.delete("1.0", tk.END)
        self.chat_log.config(state='disabled')

    def toggle_mute(self):
        if self.is_muted:
            pygame.mixer.music.unpause()
            self.mute_button.config(text="Mute")
        else:
            pygame.mixer.music.pause()
            self.mute_button.config(text="Unmute")
        self.is_muted = not self.is_muted

    def generate_goblin_name(self):
        prefix = choice(self.prefixes)
        body_part = choice(self.body_parts)
        return f'{prefix} {body_part}'

if __name__ == "__main__":
    root = tk.Tk()

    # Apply custom styles for a dark, cave-like theme
    style = ttk.Style()
    style.configure('TFrame', background='#2E2E2E')
    style.configure('TLabel', background='#2E2E2E', foreground='#FFFFFF')
    style.configure('TButton', background='#4A4A4A', foreground='#FFFFFF')

    app = ZanikChatApp(root)
    root.mainloop()
 
