#Ashvin Fernandes
import canonical

class CanonicalTest(unittest.TestCase):


	def test_convertBrackets(self):
		self.assertEqual(canonical.convertBrackets("1 + x"), "1 + x")
		self.assertEqual(canonical.convertBrackets("1 + x + (y + z)"), "1 + x + y + z")
		self.assertEqual(canonical.convertBrackets("1 + x - (y + z)"), "1 + x - y - z")
		self.assertEqual(canonical.convertBrackets("1 + x - (y + z - (a))"), "1 + x - y - z + a")

	def test_sortCanon(self):
		self.assertEqual(canonical.sortCanon(["a", "b^2", "x^22y^22", ""]), ["x^22y^22", "b^2", "a", ""])

	def test_convert(self):
		self.assertEqual(canonical.convertToCanon("x^2 + 3.5xy + y = y^2 - xy + y"), "x^2 - y^2 + 4.5xy = 0")
		self.assertEqual(canonical.convertToCanon("3.2y^2 + 2.8x - 1.0 = 1.2y^2 + 2.0"), "2.0y^2 + 2.8x - 3.0 = 0")
		self.assertEqual(canonical.convertToCanon("2.0x^2 - 2.0x^2 + 2.2y = 3.0"), "2.2y - 3.0 = 0")
		self.assertEqual(canonical.convertToCanon("2.5xy^2 + y^2 - x + 3 = 7.2xy^2 - 2.4y^2 + 3.0y"), " - 4.7xy^2 + 3.4y^2 - x - 3.0y + 3.0 = 0")
		self.assertEqual(canonical.convertToCanon("2.5xy^2 + (y^2 - (x + 3)) = 7.2xy^2 - (2.4y^2 + 3.0y)"), " - 4.7xy^2 + 3.4y^2 - x + 3.0y - 3.0 = 0")
		self.assertEqual(canonical.convertToCanon("(2.0x - 1) + (3.0y + 1) = 2"), "2.0x + 3.0y - 2.0 = 0")
		self.assertEqual(canonical.convertToCanon("2.0x = 2.0x"), "0 = 0")
		

if __name__ == "__main__":
	unittest.main(exit=False)
	input('Press ENTER to exit')
