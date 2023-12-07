from flask import Flask, render_template, request, flash
from datetime import datetime
from .Queries import Query1, Query2, Query3, Query4, Query5, Query6, Query7, Query8


def output():
    print("hi")


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random stuff'

    @app.route('/')
    def home():
        return render_template("Base.html")

    @app.route('/test/', methods=['POST'])
    def testfunc():
        if request.method == 'POST':
            Query1()
            return render_template("Base.html")

    @app.route('/test2/', methods=['POST'])
    def testfunc2():
        if request.method == 'POST':
            flash(Query2(), category='success')
            return render_template("Base.html")

    @app.route('/test3/', methods=['POST'])
    def testfunc3():
        if request.method == 'POST':
            flash(Query3(), category='success')
            return render_template("Base.html")

    @app.route('/test4/', methods=['POST'])
    def testfunc4():
        if request.method == 'POST':
            flash(Query4(), category='success')
            return render_template("Base.html")

    @app.route('/test5/', methods=['POST'])
    def testfunc5():
        if request.method == 'POST':
            flash(Query5(), category='success')
            return render_template("Base.html")

    @app.route('/test6/', methods=['POST'])
    def testfunc6():
        if request.method == 'POST':
            flash(Query6(), category='success')
            return render_template("Base.html")

    @app.route('/test7/', methods=['POST'])
    def testfunc7():
        if request.method == 'POST':
            flash(Query7(), category='success')
            return render_template("Base.html")

    @app.route('/test8/', methods=['POST'])
    def testfunc8():
        if request.method == 'POST':
            flash(Query8(), category='success')
            return render_template("Base.html")

    return app



