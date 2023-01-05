import pyttsx3
import moviepy
import gtts
from moviepy.video.tools.drawing import color_gradient
from moviepy.video.VideoClip import TextClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

engine = pyttsx3.init()

# Step 1:  Generate speech from text

class Generator:

    def __init__(self, text):
        self.text = text
        self.audio_file_name = 'speech.mp3'
        self.video_file_name = 'video.mp4'
        self.generate_speech(text, self.audio_file_name)
        self.clip = self.generate_clip(text)
        # self.generate_video(self.clip, self.audio_file_name, self.video_file_name)

    def generate_video(self, clip, audio_file_name, video_file_name):
        self.audio = AudioFileClip('speech.mp3').set_duration(clip.duration)
        final_clip = CompositeVideoClip([self.audio.set_duration(clip.duration), clip])
        final_clip.write_videofile(video_file_name, codec='libx264')

    def generate_speech(self, text, audio_file_name):
        # Set the voice and language of the text-to-speech engine
        engine.setProperty('voice', 'english')
        engine.setProperty('language', 'en')

        # Have the text-to-speech engine speak the input text
        engine.say(text)
        engine.runAndWait()

        # Generate an audio file from the spoken text using the gTTS library
        audio = gtts.gTTS(text=text, lang='en')
        audio.save(audio_file_name)


    def generate_clip(self, text):
        # Generate an image of the text
        clip = TextClip(text, font='Arial', color='white', fontsize=24).set_duration(self.audio.duration).set_audio(self.audio)
        clip.write_videofile("movie.mp4", codec='libx264')
        return clip

res = Generator("Google's YouTube has agreed to a deal with the NFL that will make it the new home for the NFL's Sunday Ticket package beginning next season, the two announced Thursday morning. Sunday Ticket will be available as an add-on for YouTube TV as well as a standalone purchase on YouTube Primetime Channels. Additionally, as part of the agreement, YouTube and the NFL will facilitate exclusive access to official content and attendance opportunities for select YouTube Creators at key NFL tentpole events. Amazon bought the rights to NFL's Thursday Night Football franchise for $1 billion a year through 2023.")