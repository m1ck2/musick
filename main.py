import os
import webapp2
import jinja2

jinja_current_directory = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
  def get(self):
    welcome_template = jinja_current_directory.get_template(
      "templates/welcome.html")
    self.response.write(welcome_template.render())

class ArtistsHandler(webapp2.RequestHandler):
  def get(self):
    welcome_template = jinja_current_directory.get_template(
      "templates/artists.html")
    self.response.write(welcome_template.render())

class ArtistHandler(webapp2.RequestHandler):
    def get(self):
        artist_info = {
          'Taylor Swift': {
              'image': 'taylor.png',
              'spotify_link': '06HL4z0CvFAxyc27GXpf02',
          },
          'Christina Aguilera': {
              'image': 'christina.jpg',
              'spotify_link': '1l7ZsJRRS8wlW3WfJfPfNS',
          },
          'Abba': {
            'image': 'abba.png',
            'spotify_link': '0LcJLqbBmaGUft1e9Mm8HV'
          },
        }
        name = self.request.get("name")
        artist_template = jinja_current_directory.get_template("templates/artist.html")
        self.response.write(artist_template.render({
            "name": name,
            "image": artist_info[name]['image'],
            "spotify_link": artist_info[name]['spotify_link']}))

app = webapp2.WSGIApplication([
  ('/', WelcomeHandler),
  ('/artists', ArtistsHandler),
  ('/artist', ArtistHandler),
], debug=True)
