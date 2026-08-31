from flask import Flask, render_template_string
import requests

app = Flask(__name__)

html_file = open("public/index.html")
template = html_file.read()

@app.route("/")
def index():
    url = "http://todoAppApiVT26:4000/todos"
    
    try:
        response = requests.get(url).json()
    except requests.exceptions.Timeout:
        print("Fel: API-anropet tog för lång tid.")
        return render_template_string(template, todos=[])
    except requests.exceptions.HTTPError as e:
        print(f"Fel: HTTP-statusfel: {e}")
        return render_template_string(template, todos=[])
    except requests.exceptions.RequestException as e:
        print(f"Fel: Något gick fel vid anropet: {e}")
        return render_template_string(template, todos=[])


    return render_template_string(template, todos=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
