import json
from urllib.parse import urlencode
from urllib.request import urlopen


class Solution:
    def run(self, film, character):
        url = f"https://challenges.hackajob.co/swapi/api/films/?{urlencode(dict(search=film))}"
        with urlopen(url) as conn:
            resp = json.loads(conn.read())
            if "results" in resp and len(resp["results"]) > 0:
                film_d = resp["results"][0]
            else:
                film_d = None

        if film_d is not None:
            film_response = []
            for ch_url in film_d["characters"]:
                with urlopen(ch_url) as conn:
                    ch = json.loads(conn.read())
                    film_response.append(ch["name"])
            film_response.sort()
            film_response = ", ".join(film_response)
            film_response = f"{film}: {film_response}"
        else:
            film_response = f"{film}: none"

        url = f"https://challenges.hackajob.co/swapi/api/people/?{urlencode(dict(search=character))}"
        with urlopen(url) as conn:
            resp = json.loads(conn.read())
            if "results" in resp and len(resp["results"]) > 0:
                star_d = resp["results"][0]
            else:
                star_d = None

        if star_d is not None:
            star_response = []
            for f_url in star_d["films"]:
                with urlopen(f_url) as conn:
                    f = json.loads(conn.read())
                    star_response.append(f["title"])
            star_response.sort()
            star_response = ", ".join(star_response)
            star_response = f"{character}: {star_response}"
        else:
            star_response = f"{character}: none"

        filmsAndCharacters = f"{film_response}; {star_response}"
        return filmsAndCharacters
