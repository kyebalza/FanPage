from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.0lc3ei6.mongodb.net/?Cluster0=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
##    sample_receive = request.form['sample_give']
    print('서버연결완료')
    Nick_Name = request.form['nickName_give']
    Cheering_Comment = request.form['cheeringComment_give']
    passwd = request.form['passwd_give']
    comment_num = request.form['comment_num_give']
    print(Nick_Name, Cheering_Comment, passwd, comment_num)


    doc = {
        'nickName': Nick_Name,
        'cheeringComment': Cheering_Comment,
        'passwd': passwd,
        'comment_num' : comment_num
    }

    db.penPage.insert_one(doc)

    return jsonify({'msg':'응원 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():

    all_penPage = list(db.penPage.find({}, {'_id': False}))

    return jsonify({'penPage':all_penPage})


@app.route("/reviewDelete", methods=["POST"])
def homework_delete():
    passwd = request.form['passwd_receive']
    nickname = request.form['nickName_receive']
    cheeringComment = request.form['cheeringComment_receive']
    comment_num = request.form['comment_num_receive']
    print(passwd,nickname)
    db.penPage.delete_one({'passwd': passwd})
    return jsonify({'msg':comment_num+'번 글 삭제성공'})

@app.route("/reviewUpdate", methods=["POST"])
def homework_update():
    passwd = request.form['passwd_receive']
    nickname = request.form['nickName_receive']
    cheeringComment = request.form['cheeringComment_receive']
    comment_num = request.form['comment_num_receive']
    print(passwd,nickname)
    db.penPage.update_one({'comment_num': comment_num},{'$set':{'cheeringComment':cheeringComment}})
    return jsonify({'msg':comment_num+'번 글 수정성공'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)