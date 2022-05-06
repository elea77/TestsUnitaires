from unittest import TestCase
import requests

class Test_Movie(TestCase):

    def test_post(self):
        requests.post('http://127.0.0.1:5000/', json = {"title": "The Mask","description":"Stanley Ipkiss, modeste employé de banque, passionné par l'univers de Tex Avery, trouve un masque ancien aux pouvoirs surnaturels. Il est néanmoins partagé entre devenir cette créature verte sûre d'elle ou rester le timide Stanley Ipkiss, incapable d'aborder la magnifique chanteuse de cabaret Tina Carlyle.","duration":"1h40"})

    def test_get(self):
        requests.get('http://127.0.0.1:5000/62752b923a6e0cc328af79fe').json()

    def test_put(self):
        requests.put('http://127.0.0.1:5000/62752c2f8023ce9a3237fd25', json = {"title": "Justice League","description":"Trop nul ce film","duration":"2h40"}).json()

    def test_delete(self):
        requests.delete('http://127.0.0.1:5000/6275435a0f594406bdb86ebe')

    
