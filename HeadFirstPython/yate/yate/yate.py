#从标准库的string模块导入Template类，它支持简单的字符串替换模板
from string import Template
#resp缺省值 这个函数需要一个（可选的）字符串作为参数，用它来创建一个CGI（command gateway interface）"context-type："行
#缺省参数text/html
def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')
#include_header 需要一个字符换作为参数，用在HTML页面最前面的标题中。页面本身存储在一个单独的文件"templates/header.html中"
#可以根据条件替换标题
def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))
#与header相似决定一个尾部，尾部用来动态的创建一组HTML链接标记，
#从这些标记的使用来看标记应当是一个字典
def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))
#这个函数返回表单最前面的html，允许调用者指定表单数据传递的目标URL
#还可以指定所需要使用的方法
def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')
#这个函数返回表单末尾的HTML标记，同时还允许调用者定制表单的
#subimit 按钮文本
def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')
#给定一个单选钮名或值，创建一个HTML单选钮（通常包括在一个HTML表单中
# ）两个参数是必须的
def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')
#一个简单的FOR 循环 实现 给定一个列表项，这个函数会把该列表转换为一个HTML无序列表
#每次迭代会向ul元素增加一个li元素
def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)
#创建并返回一个HTML标题标记（H1 H2）默认
#H2 header_text参数是必要的j
def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')
#用HTML段落标记包围一个文本框（一个字符串）
def para(para_text):
    return('<p>' + para_text + '</p>') 

start_response()