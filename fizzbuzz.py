import unittest
class FizzBuzz():
    def fizzbuzz(self,number):
        if number > 0:
            if number % 3 == 0 and number % 5 == 0:
                return "Fizz Buzz"
            if number % 3 == 0:
                return "Fizz"
            if number % 5 == 0:
                return "Buzz"
        return str(number)

    def player_fizz(self,range_number):
        my_list = []
        for number in range(range_number):
            my_list.append(self.fizzbuzz(number))
        return my_list

class TestFizzBuzzMethods(unittest.TestCase):

    def test_get_fizzbuzz(self):
        game = FizzBuzz()
        self.assertEqual(game.fizzbuzz(1), '1')
        self.assertEqual(game.fizzbuzz(3), "Fizz")
        self.assertEqual(game.fizzbuzz(4), '4')
        self.assertEqual(game.fizzbuzz(5), "Buzz")
        self.assertEqual(game.fizzbuzz(15), "Fizz Buzz")

    def test_get_player(self):
        game = FizzBuzz()
        self.assertEqual(game.player_fizz(16), ['0','1','2','Fizz','4','Buzz','Fizz','7','8','Fizz','Buzz','11','Fizz','13','14','Fizz Buzz'])

if __name__ == '__main__':
    unittest.main()