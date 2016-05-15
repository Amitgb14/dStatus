# -*- coding: utf-8 -*-

import os
import yaml
from subprocess import Popen, PIPE

from flask import Flask, jsonify, render_template, request

import config
import dServer

app = Flask(__name__)

_PORT = config.CLIENT_PORT
_host_file = 'dServer/hosts'


def check_node(node_ip):
    command = "ping {} -c 3 -W 5".format(node_ip)
    execute = Popen(command, stdout=PIPE,
                    stderr=PIPE, shell=True)
    status = execute.wait()
    (stdout, stderr) = execute.communicate()
    if status:
        return False
    return True


def read_host():
    if not os.path.exists(_host_file):
        return []

    hosts = []
    with open(_host_file) as fread:
        for host in fread:
            if host.startswith('#'):
                continue
            hosts.append(host.strip())
    return hosts


def get_alive_nodes():
    nodes = read_host()
    alive_nodes = {}
    for node in nodes:
        if check_node(node):
            alive_nodes[node] = "Success"
        else:
            alive_nodes[node] = "Failed"
    return alive_nodes


def scan_data(node):
    try:
        report = dServer.connect(node, _PORT)
        report = yaml.load(report)
        return report
    except Exception as e:
        print "Try to connect nodes", e.args


@app.route("/get")
def get_data():
    node = request.args.get('node', '', type=str)

    reports = scan_data(node)
    return jsonify(report=reports)


@app.route("/nodes")
def node():
    nodes = get_alive_nodes()
    return render_template("nodes.html", nodes=nodes)


@app.route("/")
def index():
    return render_template('index.html')


# ----------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
