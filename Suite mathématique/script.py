import requests
from bs4 import BeautifulSoup

def get_html(session, url):
    try:
        # here you can extract data with any method you want I found this easy sooo ;))
        r = session.get(url)
        data = BeautifulSoup(r.content,'html5lib')
        text = data.get_text(separator=' ', strip=True)
        table_of_elements = text.split(" ")
        print(table_of_elements)
        n=int(table_of_elements[23])
        U0=int(table_of_elements[18])
        x=int(table_of_elements[4])
        y=int(table_of_elements[13])
        op1 = table_of_elements[5]
        op2 = table_of_elements[9]
        part1 = U0 + n * x
        part2 = y * (n * (n - 1)) // 2
        result = part1 - part2

        return result

    except Exception as e:
        print("Parsing error:", e)
        return None


def main():
    # we used sessions to maintain the same cookies
    session = requests.Session()

    base_url = "http://challenge01.root-me.org/programmation/ch1/"
    result = get_html(session, base_url)

    if result is None:
        print("Failed to compute result.")
        return

    submit_url = f"http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result={result}"
    r = session.get(submit_url)

    if "Time out!" in r.text:
        print("Time out!")
    else:
        print(r.text)


main()
