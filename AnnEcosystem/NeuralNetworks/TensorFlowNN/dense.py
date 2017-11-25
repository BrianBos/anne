import tensorflow as tf

class Dense:
  # config template
  # {
  #   "input": {"units": 4},
  #   "hidden": [{"units": 3},{"units": 2}],
  #   "output": {"units": 4}
  # }
  def __init__(self, config):
    self.config = config
    self.session = tf.Session()

    # Input layer
    self.__input_layer = tf.placeholder(tf.float32, [1, self.config["input"]["units"]])

    # Hidden layers
    self.__hidden_layers = []
    prev_layer = self.__input_layer
    for i in self.config["hidden"]:
      self.__hidden_layers.append(
          tf.layers.dense(
            inputs=prev_layer,
            units=i["units"],
            activation=tf.nn.relu)
          )

    # Output layer
    dense_layer = tf.layers.dense(
        inputs=prev_layer,
        units=self.config["output"]["units"])
    self.__output_layer = tf.argmax(input=dense_layer, axis=1)

  def assess(self):
    inputs = self.__observe()
    self.session.run(tf.global_variables_initializer())
    return self.session.run(self.__output_layer, {self.__input_layer: [inputs]})

  # PRIVATE
  def __observe(self):
    return [1,2,3,4]


