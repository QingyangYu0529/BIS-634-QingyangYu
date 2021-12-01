import pandas as pd


cancer_data = pd.read_csv("cleaned_cancer_data.csv")

# save state name(lowercase) into a list state_name, for further use in Flask.
state_name = cancer_data['State'].tolist()
state_name = [item.lower() for item in state_name]

# save age-adjusted incidence rate into a list age_adjusted_IR, merge two lists into tuple state_IR.
FIPS_code = cancer_data['FIPS'].tolist()
Lower_CI = cancer_data['Lower 95% Confidence Interval'].tolist()
Upper_CI = cancer_data['Upper 95% Confidence Interval'].tolist()
average_annual_count = cancer_data['Average Annual Count'].tolist()
recent_trend = cancer_data['Recent Trend'].tolist()
age_adjusted_IR = cancer_data['Age-Adjusted Incidence Rate([rate note]) - cases per 100,000'].tolist()
state_info = list(tuple(zip(state_name, FIPS_code, age_adjusted_IR, Lower_CI, Upper_CI, average_annual_count, recent_trend)))


from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/state/<string:name>")
def get_info():
    import json
    dics = {}
    for item in state_name:
        dics[item] = age_adjusted_IR[state_name.index(item)]
    json_object = json.dumps(dics)
    return json_object


@app.route("/info", methods=["GET"])
def info():
    usertext = request.args.get("usertext")
    result = ""
    IR = 0
    FIPS = 0
    CI = ""
    AAC = 0
    rec_trend = ""
    if usertext.lower() in state_name:
        for item in state_info: 
            if usertext.lower() == item[0]:
                FIPS = item[1]
                IR = item[2]
                CI = "(" + str(item[3]) + "," + str(item[4]) + ")"
                AAC = int(item[5])
                rec_trend = item[6]
        result += f"The state name is {usertext}, the age-adjusted incidence rate(cases per 100k) is {IR}.\n" 
        return render_template("info.html", analysis = result, FIPS = FIPS, IR = IR, CI = CI, AAC = AAC, rec_trend = rec_trend, usertext = usertext)
    else:
        result += f"Error: the state name {usertext} is invalid.\n"
        return render_template("error.html", analysis = result, usertext = usertext)
    
@app.route("/map")
def map():
    return render_template("map.html")        

if __name__ == "__main__":
    app.run(debug = True)