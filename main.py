from tinydb import TinyDB, Query

class Book:
    def __init__(self, title, author, resume,image):
        self.title = title
        self.author = author
        self.resume = resume
        self.image = image

class UserBookRegistry:
    def __init__(self,ranking,tipo,favorito,desejado,troco,tenho,emprestei,paginas,dt_resenha,paginas_lidas,dt_leitura,book):
        self.ranking = ranking
        self.tipo = tipo
        self.favorito = favorito
        self.desejado = desejado
        self.troco = troco
        self.tenho = tenho
        self.emprestei = emprestei
        self.paginas = paginas
        self.dt_resenha = dt_resenha
        self.paginas_lidas = paginas_lidas
        self.dt_leitura = dt_leitura
        self.edicao = book
        
class BookShelf:
    def __init__(self, db_file):
        self.db = TinyDB(db_file)
        self.books_table = self.db.table("books")

    def add_book(self, userBookRegistry):
        self.books_table.insert({ "ranking": userBookRegistry.ranking, "tipo": userBookRegistry.tipo,"favorito": userBookRegistry.favorito, "desejado": userBookRegistry.desejado, "troco": userBookRegistry.troco, "tenho": userBookRegistry.tenho,"emprestei": userBookRegistry.emprestei, "paginas": userBookRegistry.paginas, "dt_resenha": 0, "paginas_lidas": userBookRegistry.paginas_lidas,  "dt_leitura": userBookRegistry.dt_leitura, "edicao" : {"titulo": userBookRegistry.edicao.title, "autor": userBookRegistry.edicao.author, "sinopse": userBookRegistry.edicao.resume, "capa_media": userBookRegistry.edicao.image}} )

    def get_books(self):
        return self.books_table.all()

    def search_books(self, keyword):
        BookQuery = Query()
        return self.books_table.search((BookQuery.title.contains(keyword)) |
                                       (BookQuery.author.contains(keyword)) |
                                       (BookQuery.resume.contains(keyword)))

def main():
    db_file = "bookshelf_db.json"
    book_shelf = BookShelf(db_file)

    while True:
        print("\nBook Shelf Application")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            resume = input("Enter book Resume: ")
            image = input("Enter book Image: ")
            new_book = Book(title, author, resume, image)            
            ranking = input("Enter book ranking: ")
            tipo = input("Enter book tipo: ")
            favorito = input("Enter book is favorito: ")
            desejado = input("Enter book is desejado: ")
            troco = input("Enter book is troco: ")
            tenho = input("Enter book is tenho: ")
            emprestei = input("Enter book  is emprestei: ")
            paginas = input("Enter book paginas: ")
            dt_resenha = input("Enter book dt_resenha: ")
            paginas_lidas = input("Enter book paginas_lidas: ")
            dt_leitura = input("Enter book dt_leitura: ")
            edicao = new_book
            new_book_registry = UserBookRegistry(ranking, tipo, favorito, desejado,troco,tenho,emprestei,paginas,dt_resenha,paginas_lidas,dt_leitura,edicao)
            book_shelf.add_book(new_book_registry)
            print("Book added successfully!")

        elif choice == "2":
            books = book_shelf.get_books()
            if books:
                print("\nBooks in the Shelf:")
                for idx, book in enumerate(books, start=1):
                    print(f"{idx}.Title: {book['edicao']['titulo']},\n Author: {book['edicao']['autor']},\n Resume: {book['edicao']['sinopse']}\n\n")
            else:
                print("No books in the shelf.")

        elif choice == "3":
            print("Exiting Book Shelf Application.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()