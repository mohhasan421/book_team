from flask import Flask, render_template, request

app = Flask(name)


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        booking_date = request.form.get("booking_date")
        booking_time = request.form.get("booking_time")

        if booking_date and booking_time:
            message = (
                f"تم استلام طلب الحجز بنجاح: "
                f"{booking_date} الساعة {booking_time}"
            )
        else:
            message = "يرجى إدخال التاريخ والوقت."

    return render_template("index.html", message=message)


if name == "main":
    app.run(debug=True)