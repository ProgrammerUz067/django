from django.test import TestCase,Client
from django.urls import reverse
from .models import Book
from .forms import AddBookForm
from .views import DeleteBookView



class BookModelTestCase(TestCase):
    def setUp(self):
        self.book=Book.objects.create(
            title="Shum Bola",
            body="Juda zo'r kitob",
            price="20000",
            author="G'afur G'ulom"
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title,"Shum Bola")
        self.assertEqual(self.book.body,"Juda zo'r kitob")
        self.assertEqual(self.book.price,"20000")
        self.assertEqual(self.book.author,"G'afur G'ulom")


    def test_book_str(self):
        self.assertEqual(str(self.book),"Shum Bola")


class Test_forms(TestCase):
    def test_book_create(self):
        urls=reverse("book_add")
        response=self.client.get(urls)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed("add_book.html")

    def test_book_creation(self):
        from_data={
            'title':"Test book",
            'body':"book decription",
            'price':"20000",
            'author':"test user",
        }
        form=AddBookForm(data=from_data)
        self.assertTrue(form.is_valid())
        new_book=form.save()
        seved_book=Book.objects.get(id=new_book.id)
        self.assertEqual(seved_book.title,"Test book")
        self.assertEqual(seved_book.body,"book decription")
        self.assertEqual(seved_book.price,"20000")
        self.assertEqual(seved_book.price,"test user")





class Test_delet_book(TestCase):
    def test_delet(self):
        urls = reverse("delbook")
        response = self.client.delete(urls)
        self.assertEqual(response.status_code,404)
        self.assertTemplateUsed("delet.html")















