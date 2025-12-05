from http.server import HTTPServer, BaseHTTPRequestHandler
from models import author
main_author = author.author("Lisa", "P3120")
from controllers import CurrencyRatesCRUD

env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)

template = env.get_template("index.html")

result = template.render(myapp="Приложение",
                         author_name=main_author.name,
                         group=main_author.group,
                         navigation=[{'caption': 'Основная страница',
                                      'href': "/lisa_3120"},
                                     {"user": "пользователь",
                                      'href': "/lisa_3120_user"},
                                     {"autorization": "Авторизация",
                                      'href': "/lisa_3120_auto"},
                                     {"user_currencies": "подписчики на группу валют",
                                      'href': "/lisa_3120_usercur"},
                                     {"logout": "Выход",
                                      'href': "/lisa_3120_log"},
                                     {"courses": "Курсы валют",
                                      'href': "/lisa_3120_course"}]
                         )


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global result
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        # result = ""
        print(self.path)
        self.wfile.write(bytes(result, "utf-8"))


class CurrencyRatesMock():
    def __init__(self):
        self.__values = [("USD", "02-04-2025 11:10", "90"),
                         ("EUR", "02-04-2025 11:11", "91"),
                         ("GBP", '02-04-2025 11:37', '100')]

    @property
    def values(self):
        return self.__values


c_r = CurrencyRatesMock()
c_r_controller = CurrencyRatesCRUD(c_r)
c_r_controller._create()
c_r_controller._read()

if __name__ == "__main__":
    print('server is running')

    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()
