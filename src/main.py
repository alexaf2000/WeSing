
# importing pyglet module
import pyglet


pyglet.options['search_local_libs'] = True

# Return an error if not FFMPEG was found

print("FFmpeg DDLs found: ", pyglet.media.have_ffmpeg())
 
# width of window
width = 500
   
# height of window
height = 500
   
# caption i.e title of the window
title = "Geeksforgeeks"
   
# creating a window
window = pyglet.window.Window(width, height, title)
 
 
# video path
vidPath ="C:\\Users\\alex_\\Videos\\Captures\\gu.mp4"
 
# creating a media player object
player = pyglet.media.Player()
 
# creating a source object
source = pyglet.media.StreamingSource()
 
# load the media from the source
MediaLoad = pyglet.media.load(vidPath)
 
# add this media in the queue
player.queue(MediaLoad)
 
# play the video
player.play()
print(pyglet.media.get_decoders())
 
# on draw event
@window.event
def on_draw():
     
    # clea the window
    window.clear()
     
    # if player source exist
    # and video format exist
    if player.source and player.source.video_format:
         
        # get the texture of video and
        # make surface to display on the screen
        player.get_texture().blit(0, 0)
         
         
# key press event    
@window.event
def on_key_press(symbol, modifier):
   
    # key "p" get press
    if symbol == pyglet.window.key.P:
         
        # printing the message
        print("Key : P is pressed")
         
        # pause the video
        player.pause()
         
        # printing message
        print("Video is paused")
         
         
    # key "r" get press
    if symbol == pyglet.window.key.R:
         
        # printing the message
        print("Key : R is pressed")
         
        # resume the video
        player.play()
         
        # printing message
        print("Video is resumed")
 
# run the pyglet application

pyglet.app.run()
