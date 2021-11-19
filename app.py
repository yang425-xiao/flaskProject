#导入包
from flask import Flask,render_template,request
import datetime
#引入Flask并定义一个变量，实例化
app = Flask(__name__)

#路由解析：通过用户访问的路径，匹配相应的函数
# @app.route('/')
# def index():
#返回给用户渲染后的网页文件
#     return render_template('index.html')

#向页面传递一个变量
# @app.route('/')
def index2():
    time=datetime.date.today()     #普通变量
    name=['a','b','c']      #列表变量
    task={"任务":"打扫卫生",'时间':'3小时'}
    return render_template('index.html',var=time,list=name,task=task)


#表单提交
@app.route('/test/register')
#定义函数，规范化下和路径名称一致
def register():
    return render_template('test/register.html')
#接收表单提交的路由，需要指定methods为post，不写的话默认为get请求
#定义接口访问路径及访问方式
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result=request.form
        return render_template('test/result.html',result=result)

#通过访问路径，获取用户的字符串参数
# @app.route("/user/<name>")
# def welcom(name):
#     return '你好，%s'%name

#通过访问路径，获取用户的数据类型参数      此外，还有浮点数<float:age>
# @app.route("/user/<int：id>")
# def welcom(id):
#     return '你好，%d 号会员'%id

#debug模式开启
#路由路径不能重复，用户通过唯一路径访问特定的函数



if __name__ == '__main__':
    app.run()
