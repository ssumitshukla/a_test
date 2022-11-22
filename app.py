
from flask import *
import gspread
import datetime

gc = gspread.service_account(filename = "creds.json")
sh = gc.open_by_key("1hVdLNn_VLxhBv7jKTpctiJIFNmGfLdNVJ5RafwUD3_c")
worksheet = sh.sheet1
current_time = datetime.datetime.now()
app = Flask(__name__, static_url_path='/static')

cost = {"1":35, "2":40, "3":45, "4":8, "5":50, "6":20} 

@app.route('/')
def Home():
    return render_template('index.html')
	
@app.route("/success", methods = ['POST'])
def predict():
	if request.method == 'POST':
		name = request.form['fn']
		pnum = int(request.form['pnum'])
		email = request.form['email']
		item = request.form['order']
		q = int(request.form['q'])

		total = (cost[item]*q)*1.18
		out = "Your Order Has Been Placed, Please Pay {} Rupees".format(total)
		worksheet.append_row([str(current_time),name,pnum,email,item,q,total])
		return render_template('index.html', results = out)
	else:
		return render_template('index.html')
		
		

if __name__ == "__main__":
	app.run(debug = True)