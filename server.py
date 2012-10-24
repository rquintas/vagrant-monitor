from flask import Flask,render_template
from subprocess import check_output
import re

machine_folders = [{"folder":"/Users/rquintas/Coding/vagrant/postgres/","name":"default"}]

app = Flask(__name__)

def get_machines_info():
    
    machines = []
    
    for machine in machine_folders:
        out = check_output(["vagrant","status"],cwd=machine["folder"])
        machines.append({"title":machine["name"],"status":re.search(r''+machine["name"]+'\s(.*)\n',out).group(1)})
    
    return machines

@app.route("/")
def root():
    machines = get_machines_info()
    return render_template('show_machines.html',entries=machines)

if __name__ == "__main__":
    app.debug = True
    app.run()