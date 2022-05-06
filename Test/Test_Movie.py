from unittest import TestCase
import requests

class Test_Movie(TestCase):

    def test_post(self):
        movie = requests.post('http://127.0.0.1:5000/', json = {"title": "The Mask","description":"Stanley Ipkiss, modeste employé de banque, passionné par l'univers de Tex Avery, trouve un masque ancien aux pouvoirs surnaturels. Il est néanmoins partagé entre devenir cette créature verte sûre d'elle ou rester le timide Stanley Ipkiss, incapable d'aborder la magnifique chanteuse de cabaret Tina Carlyle.","duration":"1h40"})
        self.assertEqual(movie.status_code, 200)

    def test_get(self):
        movie = requests.get('http://127.0.0.1:5000/62752b923a6e0cc328af79fe').json()
        self.assertEqual(movie['movie']['title'], "The Batman")


    def test_put(self):
        movie = requests.put('http://127.0.0.1:5000/627561a8dae258aecd09ff1b', json = {"title": "Justice League","description":"Trop nul ce film","duration":"2h40"})
        self.assertEqual(movie.status_code, 200)


    def test_delete(self):
        movie = requests.delete('http://127.0.0.1:5000/62756283075df1c172a7b6b1')
        self.assertEqual(movie.status_code, 200)


    