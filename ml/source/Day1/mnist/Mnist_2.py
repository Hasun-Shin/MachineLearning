import numpy
import scipy.special
import matplotlib.pyplot as plt

class NerualNetwork:
    # 신경망 초기화
    def __init__(self, inputnodes, hiddennodes, outputdones, learnrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputdones

        # 가중치 행렬 wih(input 과 hidden 사이), who(hidden 과 output 사이 )
        #random 수를 가지고 만저 가중치 시작. 정규분포를 따름. 
        #pow ~ : 노드를 들어오는 연결 노드의 개수, 루트를 씌우고 역수를 취한 표준편차. 

        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), 
                                        (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), 
                                        (self.onodes, self.hnodes))                                        

        self.lr = learnrate

        # 활성화 함수 지정 -> sigmoid 
        # self.activation_function = lambda x: scipy.special.expit(x)
        pass

    # 신경망 학습
    def train(self, inputs_list, targets_list):
        # 입력 리스트를 2차원로 행렬로 변환
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # 은닉계층으로 들어오는 값 계산
        # Xhidden = W iput_hidden * I
        hidden_inputs = numpy.dot(self.wih, inputs)
        
        # 은닉계층으로 나가는 값 계산 :Ohidden
        #hidden_outputs = self.activation_function(hidden_inputs)
        hidden_outputs = self.sigmoid(hidden_inputs)

        # 최종계층으로 들어오는 값 계산
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 최종계층으로 나가는 값 계산
        #final_outputs = self.activation_function(final_inputs)
        final_outputs = self.sigmoid(final_inputs)

        # 오차는 (실제 값 - 계산 값)
        output_errors = targets - final_outputs

        # 은닉계층의 오차는 가중치에 의해 나뉜 출력 계층의
        # 오차들의 재조합 
        # errorhidden = WT(전치한것)input_hidden * erroroutput
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # 은닉계층과 출력계층 간 가중치 업데이트
        self.who += self.lr * numpy.dot(
                    (output_errors * final_outputs * (1.0 - final_outputs)),
                    numpy.transpose(hidden_outputs))
        
        # 입력계층과 은닉계층 간 가중치 업데이트
        self.wih += self.lr * numpy.dot(
                    (hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                    numpy.transpose(inputs))

        pass

    # 신경망 테스트(질의)
    def query(self, inputs_list):
        # 입력 리스트를 2차원 행렬로 변환
        inputs = numpy.array(inputs_list, ndmin=2).T

        # 은닉계층으로 들어오는 값 계산
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 은닉계층으로 나가는 값 계산
        #hidden_outputs = self.activation_function(hidden_inputs)
        hidden_outputs = self.sigmoid(hidden_inputs)
        # 최종 출력 계층으로 들어오는 값 계산
        final_inptus = numpy.dot(self.who, hidden_outputs)
        # 최종 출력 계층으로 나가는 값 계산
        #final_outputs = self.activation_function(final_inptus)
        final_outputs = self.sigmoid(final_inptus)

        return final_outputs

    def sigmoid(self, x):
        return 1 / (1 + numpy.exp(-x))

input_nodes = 784
hidden_nodes =100 #숫자 아무렇게 더 높여도 됨. 
output_nodes = 10 #답이 10개 이기 때문. 
learning_rate = 0.5

n = NerualNetwork(input_nodes, hidden_nodes, 
                    output_nodes, learning_rate)
# print(n.query([1.0, 0.5, -1.5]))

traning_data_file = open("../dataset/mnist_train.csv", "r") #60000 개 파일 
traning_data_list = traning_data_file.readlines()
traning_data_file.close()

for record in traning_data_list:
    all_values = record.split(',')
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    targets = numpy.zeros(output_nodes) + 0.01
    targets[int(all_values[0])] = 0.99
    n.train(inputs, targets)
    pass

test_data_file = open("../dataset/mnist_test.csv", "r") #10000 개 파일 
test_data_list = test_data_file.readlines()
test_data_file.close()

# all_values = test_data_list[0].split(',')
# image_array = numpy.asfarray(all_values[1:]).reshape((28,28))
# plt.imshow(image_array, cmap='Greys', interpolation='None')
# plt.show()
# print(n.query((numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01))

scorecard = []
for record in test_data_list:
    all_values = record.split(',')
    correct_label = int(all_values[0])
    print(correct_label, " correct label")
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    outputs = n.query(inputs)
    label = numpy.argmax(outputs)
    print(label, "network's answer") #가설에 의해 나온 값 
    if (label == correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)
        pass
    pass 

scorecard_array = numpy.asarray(scorecard)
print ("performance=", scorecard_array.sum() / scorecard_array.size)


#LR = 0.3 일때 정확률 94 나옴.
#LR = 0.1 일때 정확률 94 나옴. 
#LR = 0.5 일때 정확률 92 나옴.   
