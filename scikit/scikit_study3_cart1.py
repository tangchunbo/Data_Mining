from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

# 准备数据集
iris = load_iris()
# 获取特征集和分类表示
features = iris.data
labels = iris.target

# 随机抽取33% 的数据作为测试集,其余为训练集
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33,
                                                                            random_state=0)
# 创建 CART 分类树
# entropy: 基于信息熵, 也就是ID3, 实际结果与C4.5差别不大
# gini: 默认参数,CART算法
clf = DecisionTreeClassifier(criterion='gini')
# 拟合构造CART分类树
clf = clf.fit(train_features, train_labels)
test_predict = clf.predict(test_features)

# 预测结果和测试结果做对比
score = accuracy_score(test_labels, test_predict)
print("CART 分类树准确率 %.4lf" % score)

#