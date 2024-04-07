# 参考文档：https://blog.csdn.net/weixin_41888503/article/details/79802443
# 生成excel
def output_excel(name, head, lists):
    output = open(name + '.xls', 'w', encoding='gbk')
    output.write(head)
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            output.write(str(lists[i][j]))  # write函数不能写int类型的参数，所以使用str()转化
            output.write('\t')  # 相当于Tab一下，换一个单元格
        output.write('\n')  # 写完一行立马换行
    output.close()
