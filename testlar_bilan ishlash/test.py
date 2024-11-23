import unittest
from main import add_son,min_num,toq_juft,yosh,orta,karra,ism,sonlar_ortaarifmetigi,Kattakkichikharflar,absyxs,otaarifmetigi,yil


class TestAddNumber(unittest.TestCase):
    def test_add_number(self):
        self.assertEqual(add_son(4,1),5)


    def test_negative_number(self):
        self.assertEqual(add_son(-11,-2),-13)





class TestAyirSon(unittest.TestCase):
    def test_ayirma(self):
        self.assertEqual(min_num(5,1),4)





class Test_yosh(unittest.TestCase):
    def test_bola(self):
        self.assertEqual(yosh(8),"bola")

    def test_osmir(self):
        self.assertEqual(yosh(15),"O'smir")

    def test_katta(self):
        self.assertEqual(yosh(45),"Katta yoshli")






class Test_sozlar(unittest.TestCase):
    def test_sozlarni_ol(self):
        self.assertEqual(orta("Ramiz"),"Rmz")





class Test_kopaytir(unittest.TestCase):
    def test_kopaytirish(self):
        self.assertEqual(karra(14,2),28)









# class Test_ajratish(unittest.TestCase):
#     def test_belgini_ajratish(self):
#         self.assertEqual(belgi_sonni_ajratish("@slo23"),"slo23@")




# class Test_islower_upper(unittest.TestCase):
#     def test_islower_upper(self):
#         self.assertEqual(Kattakkichikharflar("PyNaTive"),'yaivePNT')




class Test_abs(unittest.TestCase):
    def test_add(self):
        self.assertEqual(absyxs("Abs","Xcd"),"AXbcsd")







class Test_arif(unittest.TestCase):
    def test_arif(self):
        self.assertEqual(otaarifmetigi('agiv@iijbfuab234'),3)








    if __name__ == '__main__':
        unittest.main(verbosity=2)
