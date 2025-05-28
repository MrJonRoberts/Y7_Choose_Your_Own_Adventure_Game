# Choose your own adventure game
# Mr Jon Roberts

# ######################################################################################
# SETUP - Functions

def print_room(room):
    print("\n" + room['room_name'])
    if not room['visited']:
        print(room['full_description'])
        room['visited'] = True
    else:
        print(room['brief_desc'])

def print_actions(room):
    print("\nDo you want to:")
    for key, desc in room['actions'].items():
        print(f"  {key}: {desc}")

def get_action(room):
    choice = None
    valid = set(room['actions'].keys())
    while choice not in valid:
        choice = input("> ").strip()
        if choice not in valid:
            print(f"Please enter one of: {', '.join(valid)}")
    return choice

def look(room):
    print("\nYou look around:")
    print(room['full_description'])

# ######################################################################################
# SETUP - Rooms

forest_entrance = {
    "room_name": "Forest Entrance",
    "room_number": 1,
    "full_description": (
        "You stand at the edge of a dense, ancient forest. The canopy above filters "
        "sunlight into shifting patterns across the leaf-strewn ground. A narrow path "
        "leads north into the trees, while a faint trail veers east."
    ),
    "brief_desc": "Forest entrance with paths north and east.",
    "visited": False,
    "actions": {
      "1": "Go north to the Mossy Clearing",
      "2": "Go east to the Twisting Path",
      "l": "Look around"
    }
}

mossy_clearing = {
    "room_name": "Mossy Clearing",
    "room_number": 2,
    "full_description": (
        "A quiet clearing carpeted with soft moss and framed by towering pines. "
        "Sunbeams dance on the damp earth. To the south is the forest entrance. "
        "A dark hollow lies to the west, and a sparkling stream glints to the east."
    ),
    "brief_desc": "Mossy clearing with hollow west and stream east.",
    "visited": False,
    "actions": {
      "1": "Return south to the Forest Entrance",
      "2": "Go west to the Old Oak Tree",
      "3": "Go east to the Shallow Stream",
      "l": "Look around"
    }
}

twisting_path = {
    "room_name": "Twisting Path",
    "room_number": 3,
    "full_description": (
        "The narrow path twists between gnarled roots and fallen logs. The air is cool "
        "and still. To the left, the undergrowth thickens. To the right, the path rises "
        "toward a rocky skyline."
    ),
    "brief_desc": "Twisting forest path with left and right forks.",
    "visited": False,
    "actions": {
      "1": "Take the left fork into the Dead End Thicket",
      "2": "Take the right fork toward the Rocky Cliff",
      "3": "Return to the Forest Entrance",
      "l": "Look around"
    }
}

oak_tree = {
    "room_name": "Old Oak Tree",
    "room_number": 4,
    "full_description": (
        "An enormous oak stands here, its ancient trunk hollowed at the base. Its massive "
        "roots create natural steps into darkness. Sunlight filters through leaves overhead. "
        "The clearing lies east."
    ),
    "brief_desc": "Hollow oak tree with roots descending.",
    "visited": False,
    "actions": {
      "1": "Climb down into the hollow to the Hidden Cave Entrance",
      "2": "Return east to the Mossy Clearing",
      "l": "Look around"
    }
}

shallow_stream = {
    "room_name": "Shallow Stream",
    "room_number": 5,
    "full_description": (
        "A clear stream flows gently here, stones visible beneath the water. Upstream, it "
        "curves into the trees; downstream, it disappears over smooth rocks. The mossy "
        "clearing is to the west."
    ),
    "brief_desc": "Shallow stream with upstream and downstream paths.",
    "visited": False,
    "actions": {
      "1": "Follow the stream upstream to the Abandoned Campsite",
      "2": "Follow the stream downstream to the Rocky Cliff",
      "3": "Return west to the Mossy Clearing",
      "l": "Look around"
    }
}

dead_end = {
    "room_name": "Dead End Thicket",
    "room_number": 6,
    "full_description": (
        "Thick brambles and fallen branches block the path in every direction. "
        "The thicket seems endless, with no way forward."
    ),
    "brief_desc": "Thick brambles block the path.",
    "visited": False,
    "actions": {
      "1": "Turn back to the Twisting Path",
      "l": "Look around"
    }
}

hidden_cave = {
    "room_name": "Hidden Cave Entrance",
    "room_number": 7,
    "full_description": (
        "Behind the oak's roots, a dark opening leads into the earth. A faint echo drips "
        "from within. The light of the clearing is visible behind you."
    ),
    "brief_desc": "Shadowy cave entrance under the roots.",
    "visited": False,
    "actions": {
      "1": "Enter the cave into the Dank Cavern",
      "2": "Climb up to the Old Oak Tree",
      "l": "Look around"
    }
}

rocky_cliff = {
    "room_name": "Rocky Cliff",
    "room_number": 8,
    "full_description": (
        "A sheer rock face rises sharply here. A narrow ledge clings to the cliff; below, "
        "you hear the distant rush of water. The Twisting Path winds back into the forest."
    ),
    "brief_desc": "Sheer cliff with a narrow ledge below.",
    "visited": False,
    "actions": {
      "1": "Go back to the Twisting Path",
      "2": "Attempt to scale down the cliff",
      "l": "Look around"
    }
}

dank_cavern = {
    "room_name": "Dank Cavern",
    "room_number": 9,
    "full_description": (
        "The air is damp and cold. Stalactites drip water into small puddles. A faint glow "
        "hints at a large cavern beyond. The cave entrance is behind you."
    ),
    "brief_desc": "Damp cavern with dripping stalactites.",
    "visited": False,
    "actions": {
      "1": "Venture deeper to the Underground Lake",
      "2": "Exit back to the Hidden Cave Entrance",
      "l": "Look around"
    }
}

falling_bridge = {
    "room_name": "Falling Bridge",
    "room_number": 10,
    "full_description": (
        "A rotting rope bridge spans a deep chasm. The planks sway with each step. On the other "
        "side, mist obscures the path. The rocky ledge is to the north."
    ),
    "brief_desc": "Rope bridge over a misty chasm.",
    "visited": False,
    "actions": {
      "1": "Cross the bridge carefully to the Abandoned Campsite",
      "2": "Rush across the bridge",
      "3": "Return north to the Rocky Cliff",
      "l": "Look around"
    }
}

underground_lake = {
    "room_name": "Underground Lake",
    "room_number": 11,
    "full_description": (
        "A still, mirror-like lake glows with bioluminescent algae. The air smells of damp stone. "
        "A dark tunnel lies beyond the water; the cavern mouth is behind you."
    ),
    "brief_desc": "Glowing lake with a tunnel beyond.",
    "visited": False,
    "actions": {
      "1": "Wade through the water to the Subterranean Tunnel",
      "2": "Return to the Dank Cavern",
      "l": "Look around"
    }
}

subterranean_tunnel = {
    "room_name": "Subterranean Tunnel",
    "room_number": 12,
    "full_description": (
        "A narrow tunnel winds deep into the rock, faint inscriptions etched in the walls. "
        "The lake's glow fades behind you."
    ),
    "brief_desc": "Narrow tunnel with etched walls.",
    "visited": False,
    "actions": {
      "1": "Follow the tunnel northeast to the Treasure Chamber",
      "2": "Follow the tunnel southwest and risk a trap",
      "3": "Return to the Underground Lake",
      "l": "Look around"
    }
}

abandoned_camp = {
    "room_name": "Abandoned Campsite",
    "room_number": 13,
    "full_description": (
        "Tattered tents and broken supplies lie scattered. A charred firepit suggests someone "
        "left in haste. A torn map flap points toward a cave."
    ),
    "brief_desc": "Deserted campsite with a torn map.",
    "visited": False,
    "actions": {
      "1": "Inspect the torn map to find the Subterranean Tunnel",
      "2": "Return to the Shallow Stream",
      "l": "Look around"
    }
}

treasure_chamber = {
    "room_name": "Treasure Chamber",
    "room_number": 14,
    "full_description": (
        "A small chamber glittering with gold and jewels. In its center sits an ornate treasure "
        "chest, locked but inviting. The tunnel entrance lies behind you."
    ),
    "brief_desc": "Chamber glittering with treasure.",
    "visited": False,
    "actions": {
      "1": "Open the treasure chest",
      "2": "Return to the Subterranean Tunnel",
      "l": "Look around"
    }
}

trap_pit = {
    "room_name": "Trap Pit",
    "room_number": 15,
    "full_description": (
        "The ground gives way and you plummet into a spike-lined pit. Darkness consumes you as the "
        "trap seals above. Your quest ends here."
    ),
    "brief_desc": "You fell into a trap pit—Game Over.",
    "visited": False,
    "actions": {
      "1": "Restart the game at the Forest Entrance",
      "2": "Quit",
      "l": "Look around"
    }
}

# map room_number → room object for easy reset
rooms = {
    1: forest_entrance,
    2: mossy_clearing,
    3: twisting_path,
    4: oak_tree,
    5: shallow_stream,
    6: dead_end,
    7: hidden_cave,
    8: rocky_cliff,
    9: dank_cavern,
    10: falling_bridge,
    11: underground_lake,
    12: subterranean_tunnel,
    13: abandoned_camp,
    14: treasure_chamber,
    15: trap_pit
}

# ######################################################################################
# GAME - Intro

game_name = "Forest Treasure Hunt"
game_over = False

player_name = input(f"What name do you want to be known as in the realm of {game_name}? ")
print(f"\nWelcome, {player_name}! Your quest is to explore the forest and find the hidden treasure.\n")

# start in room 1
current_room = forest_entrance

# ######################################################################################
# GAME LOOP

while not game_over:
    print_room(current_room)
    print_actions(current_room)
    choice = get_action(current_room)

    # handle look
    if choice == "l":
        look(current_room)
        continue

    rn = current_room["room_number"]

    # navigation logic
    if rn == 1:  # Forest Entrance
        if choice == "1":
            current_room = mossy_clearing
        elif choice == "2":
            current_room = twisting_path

    elif rn == 2:  # Mossy Clearing
        if choice == "1":
            current_room = forest_entrance
        elif choice == "2":
            current_room = oak_tree
        elif choice == "3":
            current_room = shallow_stream

    elif rn == 3:  # Twisting Path
        if choice == "1":
            current_room = dead_end
        elif choice == "2":
            current_room = rocky_cliff
        elif choice == "3":
            current_room = forest_entrance

    elif rn == 4:  # Old Oak Tree
        if choice == "1":
            current_room = hidden_cave
        elif choice == "2":
            current_room = mossy_clearing

    elif rn == 5:  # Shallow Stream
        if choice == "1":
            current_room = abandoned_camp
        elif choice == "2":
            current_room = rocky_cliff
        elif choice == "3":
            current_room = mossy_clearing

    elif rn == 6:  # Dead End Thicket
        if choice == "1":
            current_room = twisting_path

    elif rn == 7:  # Hidden Cave Entrance
        if choice == "1":
            current_room = dank_cavern
        elif choice == "2":
            current_room = oak_tree

    elif rn == 8:  # Rocky Cliff
        if choice == "1":
            current_room = twisting_path
        elif choice == "2":
            current_room = falling_bridge

    elif rn == 9:  # Dank Cavern
        if choice == "1":
            current_room = underground_lake
        elif choice == "2":
            current_room = hidden_cave

    elif rn == 10:  # Falling Bridge
        if choice == "1":
            current_room = abandoned_camp
        elif choice == "2":
            current_room = trap_pit
        elif choice == "3":
            current_room = rocky_cliff

    elif rn == 11:  # Underground Lake
        if choice == "1":
            current_room = subterranean_tunnel
        elif choice == "2":
            current_room = dank_cavern

    elif rn == 12:  # Subterranean Tunnel
        if choice == "1":
            current_room = treasure_chamber
        elif choice == "2":
            current_room = trap_pit
        elif choice == "3":
            current_room = underground_lake

    elif rn == 13:  # Abandoned Campsite
        if choice == "1":
            current_room = subterranean_tunnel
        elif choice == "2":
            current_room = shallow_stream

    elif rn == 14:  # Treasure Chamber
        if choice == "1":
            print("\nYou open the treasure chest and find the ancient gold and jewels! Congratulations—you win!\n")
            game_over = True
        elif choice == "2":
            current_room = subterranean_tunnel

    elif rn == 15:  # Trap Pit
        if choice == "1":
            # restart: reset visited flags
            for r in rooms.values():
                r['visited'] = False
            print("\nYou manage to climb out, shaken but alive. You find yourself back at the Forest Entrance.\n")
            current_room = forest_entrance
        elif choice == "2":
            print("\nYou resign yourself to your fate. Game over.\n")
            game_over = True

# ######################################################################################
# GAME END

print(f"Thank you for playing {game_name}, {player_name}!")

