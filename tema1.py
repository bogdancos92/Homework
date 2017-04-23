class Song(object):
	
	def __init__(self,lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
		
lyrics_var=["Roses are red", "Violets are blue", "No mutual friends", "Who the hell are you"]
		
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

facebook_song = Song(lyrics_var)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

facebook_song.sing_me_a_song()