import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import input_data



mnist  = input_data.read_data_sets('D:\workplace\TensorflowLearning\MNIST_data',one_hot=True)

def add_layer(inputs,in_size,out_size,activation_function=None):
	with tf.name_scope('layer'):
		with tf.name_scope('weights'):
			Weights = tf.Variable(tf.random_normal([in_size,out_size],name='W'))
		with tf.name_scope('baises'):
			biases = tf.Variable(tf.zeros([1,out_size])+0.1,name='b')
		Wx_plus_b=tf.matmul(inputs,Weights)+biases
		if activation_function is None:
			outputs = Wx_plus_b
		else:
			outputs = activation_function(Wx_plus_b)
		return outputs

def compute_accuracy(v_xs,v_ys):
	global prediction1
	global prediction2
	y_pre = sess.run(prediction2,feed_dict={xs:v_xs})
	correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
	accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
	result = sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})
	return result

xs = tf.placeholder(tf.float32,[None,784]) #28x28
ys = tf.placeholder(tf.float32,[None,10])

prediction1 = add_layer(xs,784,10,activation_function=tf.nn.softmax)
prediction2 = add_layer(prediction1,10,10,activation_function=tf.nn.softmax)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction2),
										reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)


sess = tf.Session()

sess.run(tf.initialize_all_variables())

for i in range(50000):
	batch_xs,batch_ys = mnist.train.next_batch(100)
	sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys})
	if i%5000==0:
		print(compute_accuracy(
			mnist.test.images,mnist.test.labels))

#一个教训
#双层网络虽然一定程度上增加了正确率
#但是同时也需要耗费更加多的时间去训练
#
#单层网络更加优秀你个傻逼