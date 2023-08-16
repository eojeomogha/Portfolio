# Mickey With The Blicky

Incomplete top down shooter

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Controls](#controls)
- [License](#license)

## Features

List the main features and functionalities of your game here.

- Player Movement and Shooting
  - The player can move using the WASD keys.
  - The player can aim their weapon with the mouse.
  - Left Mouse Button or Space Bar allows the player to shoot bullets.

- Aiming Line
  - The aiming line is displayed from the player's position to the mouse cursor.
  - The aiming line helps the player see where their weapon is aimed.

- Collision Handling
  - The player's movement is restricted to prevent them from moving out of bounds.
  - The player's hitbox is used for collision detection with other sprites.

- Bullet Spawning and Movement
  - The player's bullets spawn in front of the player's gun.
  - Bullets move in the direction the player's gun is aimed.
  - Bullets disappear after a specified duration.

- Enemy AI
  - Enemies are controlled by simple AI that tries to move towards the player.
  - Enemies move up and down within a specified range.
  - Enemy movement alternates between up and down to create a dynamic behavior.

- Graphics and Visuals
  - Player and enemy sprites are displayed on the screen.
  - Bullets and aiming lines are drawn to indicate player actions.
  - The game window features a background image for the environment.

- Game Loop and Controls
  - The game loop ensures smooth gameplay and rendering.
  - Controls are explained in the README, including player movement and shooting.

- Camera and Sprite Groups
  - A camera class manages sprite rendering within the game world.
  - Sprites are organized into sprite groups for efficient rendering and collision detection.

- Documentation and Comments
  - The code includes explanatory comments to describe key functionalities.
  - Important code segments are documented for ease of understanding and modification.

- Resizable Display
  - The game window is initialized with customizable dimensions.
  - The game can be played in different display sizes.

## Demo

<img width="812" alt="game" src="https://github.com/eojeomogha/MWTB/assets/134320691/302c257e-9503-46cc-b04c-43d164ad8bf8">

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/eojeomogha/MWTB.git
2. Install required dependencies using pip install -r requirements.txt.
3. Run the game using python main.py.

## Controls

- Movement: WASD keys
- Aim: Mouse cursor
- Shoot: Left Mouse Button or Space Bar

## License
This project is licensed under the [MIT License](https://chat.openai.com/c/LICENSE)
