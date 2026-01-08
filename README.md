W ramach projektu zaimplementowano kompletną aplikację webową o nazwie FlaskWall, służącą jako środowisko demonstracyjne dla bezpiecznego cyklu wytwarzania oprogramowania. 

System wytworzono w oparciu o język Python 3.9 oraz framework Flask. Wybór tej technologii podyktowany był koniecznością pełnej kontroli nad nagłówkami HTTP 
oraz łatwością integracji z narzędziami audytującymi kod. 

Warstwę dostępu do danych zrealizowano przy użyciu SQLAlchemy, co pozwoliło na uniezależnienie kodu aplikacji od silnika bazy danych (SQLite w środowisku testowym CI/CD, PostgreSQL w środowisku produkcyjnym).
