from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
	{
		"Contact": "998764456",
		"Name": "Raju",
		"done": False,
		"id": 1
	},
	{
		"Contact": 	"9876543222",
		"Name": "Rahul",
		"done": False,
		"id": 2
	}
]

@app.route("/add-data", methods=["POST"])
def add_task():
	if not request.json:
		return jsonify({
			"status": "error",
			"message": "Please provide the data!"
			}, 400)

	contact = {
			'id': contacts[-1]['id'] + 1,
			'Name': request.json['Name'],
			'Contact': request.json['Contact', ""],
			'done': False
	}
	contact.append(tasks)
	return jsonify({
			"status": "success",
			"message": "Task added successfully!"
		})

if (__name__ == '__main__'):
	app.run(debug=True)