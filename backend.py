from flask import Flask, render_template, request, redirect, url_for, make_response
app = Flask(__name__)
app.secret_key = "AN!@#J#Y"

@app.route('/')
def homepage():
    return make_response(render_template("home1.html"))

@app.route('/aboutus')
def aboutus():
    return make_response(render_template("Aboutus.html"))

@app.route('/services')
def services():
    return make_response(render_template("services.html"))

@app.route('/sustainability')
def sustainability():
    return make_response(render_template("sustainability.html"))


@app.route('/form_entry', methods=["POST", "GET"])
def form_entry():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        company = request.form.get("company")
        location = request.form.get("location")
        message = request.form.get("message")
        msg = "Halo Alpha One Energi,%20saya" + name + "\n" + "Email : " + email + "\n" + "Perusahaan: " + company + "\n" + "Lokasi: " + location + "\n" + message
        msg = msg.replace(" ", "%20")
        return redirect(f"https://api.whatsapp.com/send?phone=6285171650250&text={msg}")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True, threaded=False)

