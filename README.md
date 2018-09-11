# FindLine

I've created an implementation that uses a Keras Neural Network model to do the requested task. 
From the results I got, I do not think I will have good approximate results. On the trainig i got:

Epoch 1/2
100000/100000 [==============================] - 340s 3ms/step - loss: 1907.3751 - acc: 0.9479
Epoch 2/2
100000/100000 [==============================] - 346s 3ms/step - loss: 1621.4495 - acc: 0.9522

I got a good 'Accuracy' but a large 'Loss'
I have some ideas of why:
-Maybe I could normalize the set of points at the entrance
-Use other activating / optimizing functions that fits best in this case
-Or it was an implementation error that I did not see.

Please, if you can, tell me where I went wrong and where I could optimize my code. I am open to criticism and a fast learner to improve my implementation.
