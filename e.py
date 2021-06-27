from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [
    {
        "id": 1,
        "title": "buy stuff",
        "description": "cheese, plants, cottage cheese",
        "done": False
    },
    {
        "id": 2,
        "title": "learn python",
        "description": "google stuff and send it off as your on",
        "done": False
    }
]
@app.route('/add-data', methods=["POST"])

def addtask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        }, 30000)
    
    task = {
        "id": tasks[-1]["id"]+1, 
        "title": request.json("title"),
        "description": request.json.get("description", ""),
        "done": False
    }

    tasks.append(task)

    return jsonify({
        "status": "sucess",
        "message": "task added succesfully"
    })

@app.route("/get-data")

def gt():
    return jsonify({
        "data": tasks
    })

if __name__ == "__main__":
    app.run()