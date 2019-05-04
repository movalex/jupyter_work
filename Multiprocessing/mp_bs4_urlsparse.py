from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string


def random_starting_url():
    starting = "".join(
        random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3)
    )
    url = "".join(["http://", starting, ".com"])
    return url


def handle_local_links(url, link):
    if link.startswith("/"):
        return "".join([url, link])
    return link


def get_links(url):
    try:
        resp = requests.get(url, timeout=1)
        soup = bs.BeautifulSoup(resp.text, "html.parser")
        body = soup.body

        links = [link.get("href") for link in body.find_all("a")]
        links = [handle_local_links(url, link) for link in links]
        links = [str(link) for link in links]

        return links

    except TypeError as e:
        print(e)
        print("Got a TypeError, probably got a None that we tried to iterate over")
        return []
    except IndexError as e:
        print(e)
        print("We probably did not find anu useful return on empty list")
        return []
    except AttributeError as e:
        print(e)
        print("likely got None for links, throwing this")
        return []
    except Exception as e:
        # raise
        print("unknown exception")
        return []


def main():
    how_many = 20
    p = Pool(processes=how_many)
    parse_us = [random_starting_url() for _ in range(how_many*2)]
    data = p.map(get_links, [link for link in parse_us])
    data = [url for url in data]
    print(data)
    p.close()

    with open("urls.txt", "w") as f:
        for elem in data:
            for url in elem:
                f.write(str(url))
                f.write('\n')


if __name__ == "__main__":
    main()

