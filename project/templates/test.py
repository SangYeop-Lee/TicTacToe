from moviepy.editor import *

clip = (VideoFileClip('motion.mp4')).subclip((0), (0,5))
clip.write_mp4('motion.mp4')

#http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/