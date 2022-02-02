import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org/?format=json').json()
    return ip_address['ip']


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=10)
    return results


def play_on_yt(video):
    kit.playonyt(video)


def search_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+254{number}", message)


EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')


def send_email(receiver_address, subject, message):

    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.sendmail(email)
        s.close()
        return True

    except Exception:
        print(Exception)
        return False


TMDB_API_KEY = config("TMDB_API_KEY")


def trending_movies():
    trending_movies = []
    res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]