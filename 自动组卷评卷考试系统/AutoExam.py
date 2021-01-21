import random
def readQuestionBank():
# 读入题库文件
# 题库文件的结构是：一行题目，一行答案。
# 每种题型末尾有一行标记文字，标识计数停止的位置，不要改动标识文字的内容。
# 如果要新增题目，应将题目按照一行题目一行答案的格式，写在对应题型标记文字之前。
    questionBankFile=open(r'D:\AutoExam.txt','r')
    questionBankList=questionBankFile.readlines()
# 统计各题型题目总数
    index=0
    questionBankTuple=([],[],[])
# 统计题库中包含选择题的总数，便于之后确定出题的数量
    while True:
        if questionBankList[index]!='End of Multiple Choice\n':
            questionBankTuple[0].append((questionBankList[index].strip(),questionBankList[index+1].strip()))
            index+=2
        else:
            break
    index+=1 # 跳过不表示题目的标记行
# 统计题库中包含选择题的总数，便于之后确定出题的数量
    while True:
        if questionBankList[index]!='End of Filling Blanks\n':
            questionBankTuple[1].append((questionBankList[index].strip(),questionBankList[index+1].strip()))
            index+=2
        else:
            break
    index+=1 # 跳过不表示题目的标记行
# 统计题库中包含选择题的总数，便于之后确定出题的数量
    while True:
        if questionBankList[index]!='End of True or False':
            questionBankTuple[2].append((questionBankList[index].strip(),questionBankList[index+1].strip()))
            index+=2
        else:
            break
    print('本题库共包含单项选择题{}道，填空题{}道，判断题{}道。'.format(len(questionBankTuple[0]),len(questionBankTuple[1]),len(questionBankTuple[2])))
    return questionBankTuple
def examMaker(questionBankTuple):
    # 从全部题目中抽取的题目数。选择题抽取5的倍数道，填空题抽取4的倍数道，判断题抽取3的倍数道。
    countOfMultipleChoice=(len(questionBankTuple[0])//5)*5
    countOfFillingBlanks=(len(questionBankTuple[2])//4)*4
    countOfTrueOrFalse=(len(questionBankTuple[2])//3)*3
    # 将题库元组的三个分量：选择题列表、填空题列表和判断题列表拆分出来，并打乱
    multipleChoiceList=questionBankTuple[0]
    fillingBlanksList=questionBankTuple[1]
    trueOrFalseList=questionBankTuple[2]
    random.shuffle(multipleChoiceList)
    random.shuffle(fillingBlanksList)
    random.shuffle(trueOrFalseList)
    # 读取题目
    examQuestionBank=(multipleChoiceList[:countOfMultipleChoice],fillingBlanksList[:countOfFillingBlanks],trueOrFalseList[:countOfTrueOrFalse])
    # 拼接得到的 examQuestionBank 元组，0 号分量是选择题列表，1 号分量是填空题列表，2 号分量是判断题列表。
    # 每个列表的成员是 (题目, 答案) 元组。
    return examQuestionBank
def doTheExam(examQuestionBank):
    totalOfQuestions=len(examQuestionBank[0])+len(examQuestionBank[1])+len(examQuestionBank[2])
    # 答题开始时的用户友好界面
    print('欢迎使用自动组卷评卷系统！')
    print('本次考试共有{}题，其中{}道单项选择题，{}道填空题，{}道判断题。'.format(totalOfQuestions,len(examQuestionBank[0]),len(examQuestionBank[1]),len(examQuestionBank[2])))
    print('各题型在总分中的占比：单项选择题50%，填空题20%，判断题30%')
    print('请认真作答，诚信考试！')
    # 计数变量，用于统计各题型答对的题目数
    correctMultipleChoice=0
    correctFillingBlanks=0
    correctTrueOrFalse=0
    # 以下是答题循环
    for i in range(len(examQuestionBank[0])):
        print('选择题第{}题：'.format(i+1))
        # examQuestionBank 元组，0 号分量是选择题列表，1 号分量是填空题列表，2 号分量是判断题列表。
        # 每个列表的成员是 (题目, 答案) 元组。
        # 因此 examQuestionBank[0][i][0] 表示第 (i+1) 道选择题的题目，
        # examQuestionBank[0][i][1] 表示第 (i+1) 道选择题的答案。
        print(examQuestionBank[0][i][0])
        answer=input('请作答：')
        if answer.upper()==examQuestionBank[0][i][1]:  # 使用upper()方法，使得选择题作答不区分大小写
            correctMultipleChoice+=1
    for i in range(len(examQuestionBank[1])):
        print('填空题第{}题：'.format(i+1))
        print(examQuestionBank[1][i][0])
        answer=input('请作答：')
        if answer==examQuestionBank[1][i][1]:
            correctFillingBlanks+=1
    for i in range(len(examQuestionBank[2])):
        print('判断题第{}题：'.format(i+1))
        print(examQuestionBank[2][i][0])
        answer=input('请输入T或F作答，T表示对，F表示错：')
        if answer.upper()==examQuestionBank[2][i][1]: # 使用upper()方法，使得判断题作答不区分大小写
            correctTrueOrFalse+=1
    result=(correctMultipleChoice/len(examQuestionBank[0]),correctFillingBlanks/len(examQuestionBank[1]),correctTrueOrFalse/len(examQuestionBank[2]))
    score=50*result[0]+20*result[1]+30*result[2]
    print('考试结束')
    print('您的得分：{}'.format(score))
    print('单项选择题共{}道，您对了{}道'.format(len(examQuestionBank[0]),correctMultipleChoice))
    print('填空题共{}道，您对了{}道'.format(len(examQuestionBank[1]),correctFillingBlanks))
    print('判断题共{}道，您对了{}道'.format(len(examQuestionBank[2]),correctTrueOrFalse))    
def main():
    questionBankTuple=readQuestionBank()
    examQuestionBank=examMaker(questionBankTuple)
    doTheExam(examQuestionBank)
main()
input('请按回车键退出...')
