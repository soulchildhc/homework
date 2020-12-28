from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')



# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    interest_receive = request.form['interest_give']
    why_receive = request.form['why_give']
    phone_number_receive = request.form['phone_number_give']

    orders = {
        'name' : name_receive,
        'interest' : interest_receive,
        'why' : why_receive,
        'phone_number' : phone_number_receive
    }

    db.cosults.insert_one(orders)

    return jsonify({'result': 'success', 'msg' : '상담신청이 완료되었습니다!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    order_list = list(db.cosults.find({}, {'_id' : False}))
    return jsonify({'result': 'success', 'orders': order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)