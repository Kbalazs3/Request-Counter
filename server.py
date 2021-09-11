from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def read_stored_data():
    with open("request_counts.txt", "r") as data:
        request_data = {}
        for line in data:
            (key, value) = line.split(": ")
            request_data[key] = int(value)
    return request_data


def write_stored_data(request_data):
    with open("request_counts.txt", "w") as s_data:
        stored_data_to_str = ""
        for key, value in request_data.items():
            new_line = str(key + ": ") + str(value) + "\n"
            stored_data_to_str += new_line
        s_data.write(stored_data_to_str)


@app.route("/")
def main_page():
    requested_data = read_stored_data()
    return render_template("index.html", data=requested_data)


@app.route("/request_counter", methods=['GET', 'POST'])
def req_count_sub():
    request_data = read_stored_data()
    if request.method == 'GET':
        request_name = "GET"
    elif request.method == 'POST':
        request_name = "POST"
    elif request.method == 'DELETE':
        request_name = "DELETE"
    elif request.method == 'PUT':
        request_name = "PUT"
    if not request_data:
        request_data[request_name] = 1
    elif request_data:
        request_data[request_name] += 1
    write_stored_data(request_data)
    return redirect("/")


@app.route("/statistics")
def statistics():
    return render_template("statistics.html", data=read_stored_data())


if __name__=="__main__":
    app.run(
        debug=True
    )




