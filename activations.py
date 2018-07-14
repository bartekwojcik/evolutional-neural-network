import numpy as np

#https://theclevermachine.wordpress.com/2014/09/06/derivation-error-backpropagation-gradient-descent-for-neural-networks/
class Null_activation(object):

    def forward(self,x):
        return np.zeros_like(x)

    def deltah(self,hidden,deltao,prev_weights):
        gprime = 0
        deltah = gprime * (np.dot(deltao, np.transpose(prev_weights)))
        return deltah

class Sigmoid_activation(object):

    def forward(self, x):
        x -= np.max(x)
        hidden = 1.0 / (1.0 + np.exp(- x))
        return hidden

    def deltah(self,hidden,deltao,prev_weights):
        deltah = hidden * (1.0 - hidden) * (np.dot(deltao, np.transpose(prev_weights)))
        return deltah

class Tanh_activation(object):
    def forward(self,x):
        hidden = np.tanh(x)
        return hidden

    def deltah(self,hidden,deltao,prev_weights):
        deltah = 1.0 - np.square(np.tanh(hidden)) * (np.dot(deltao, np.transpose(prev_weights)))
        return deltah

class Cos_activation(object):
    def forward(self,x):
        hidden = np.cos(x)
        return hidden

    def deltah(self,hidden,deltao,prev_weights):
        deltah = - np.sin(hidden) * (np.dot(deltao, np.transpose(prev_weights)))
        return deltah

class Exp_activation(object):
    def forward(self, x):
        hidden = np.exp((- np.square(x))/2)
        return hidden

    def deltah(self, hidden, deltao, prev_weights):
        gprime = - hidden * np.exp((- np.square(hidden))/2)
        deltah = gprime * (np.dot(deltao, np.transpose(prev_weights)))
        return deltah