import tensorflow as tf

class Dense:
    #   {
    #     "dna": [
    #       input layer eg 4,
    #       hidden layers eg [3, 2],
    #       output layer eg 4
    #     ], eg [4, [3, 2], 4]
    #   }
    def __init__(self, nn_config):
        self.dna = []
        self.session = tf.Session()

        # Input layer
        self.__input_layer = tf.placeholder(tf.float32, [1, nn_config["dna"][0]])

        # Hidden layers
        self.__hidden_layers = []
        prev_layer = self.__input_layer
        for i in nn_config["dna"][1]:
            self.__hidden_layers.append(
                    tf.layers.dense(
                        inputs=prev_layer,
                        units=i,
                        activation=tf.nn.relu)
                    )

        # Output layer
        dense_layer = tf.layers.dense(
                inputs=prev_layer,
                units=nn_config["dna"][2])
        self.__output_layer = tf.argmax(input=dense_layer, axis=1)

        # generate and store dna
        i_dna = {"units": nn_config["dna"][0]}
        h_dna = []
        for i in nn_config["dna"][1]:
            h_dna.append({"units": i})
        o_dna = {"units": nn_config["dna"][2]}
        self.dna = [i_dna, h_dna, o_dna]

    def assess(self):
        inputs = self.__observe()
        self.session.run(tf.global_variables_initializer())
        return self.session.run(self.__output_layer, {self.__input_layer: [inputs]})

    # PRIVATE
    def __observe(self):
        return [1,2,3,4]


