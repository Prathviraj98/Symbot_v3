import requests

from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_download = "https://lottie.host/413401ba-89ff-4d5c-a19d-a648352578e8/eD3PrZXQ6g.json"
lottie_download = load_lottieurl(lottie_url_download)



with st_lottie_spinner(lottie_download, key="download"):
    time.sleep(5)

