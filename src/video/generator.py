import pyttsx3
import moviepy
import gTTS
from moviepy.video.tools.drawing import color_gradient
from moviepy.video.VideoClip import TextClip

engine = pyttsx3.init()

class Generator:

    def __init__(self, text):
        self.text = text

    def generate_video(self, clip, video):
        video = moviepy.video.VideoFileClip('speech.mp3', audio=True).set_duration(clip.duration)
        final_clip = moviepy.video.CompositeVideoClip([clip, video])
        final_clip.write_videofile("video.mp4", codec='libx264')

    def generate_speech(self, text):
        # Set the voice and language of the text-to-speech engine
        engine.setProperty('voice', 'english')
        engine.setProperty('language', 'en')

        # Have the text-to-speech engine speak the input text
        engine.say(text)
        engine.runAndWait()

        # Generate an audio file from the spoken text using the gTTS library
        audio = gTTS(text=text, lang='en')
        audio.save('speech.mp3')


    def generate_clip(self):
        # Generate an image of the text
        text = "Hello, my name is John. I am a software engineer."
        clip = TextClip(text, font='Arial', color='white', fontsize=24)
        return clip

