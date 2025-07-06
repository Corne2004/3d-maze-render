import functions

# STEPS:
# Get maze size                 DONE
# Get maze layout               DONE
# Get position and orientation  DONE
# Start rendering the tiles

size = functions.size_input()
maze = functions.layout_input(size)
camera_location = functions.location_input(size)
