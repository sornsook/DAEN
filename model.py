from tensorflow import keras
from tensorflow.keras import layers

# Slave network
def slave_net(input_size = (480,640,3)):
    
    factor = 3
    
    inputs 	= layers.Input(shape = input_size)
    conv_11 = layers.Conv2D(8*factor, (3, 3), activation='relu', padding='same',trainable = True)(inputs)
    conv_12 = layers.Conv2D(8*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_11)
    conv_13 = layers.Conv2D(8*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_12)
    pool_1	= layers.MaxPooling2D(pool_size = (2,2))(conv_13)
    
    conv_21 = layers.Conv2D(16*factor, (3, 3), activation='relu', padding='same',trainable = True)(pool_1)
    conv_22 = layers.Conv2D(16*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_21)
    pool_2	= layers.MaxPooling2D(pool_size = (2,2))(conv_22)
    conv_31 = layers.Conv2D(32*factor, (3, 3), activation='relu', padding='same',trainable = True)(pool_2)
    conv_32 = layers.Conv2D(32*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_31)
	# conv_33 = Conv2D(32*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_32)
    pool_3 	= layers.MaxPooling2D(pool_size=(2,2))(conv_32)

    conv_41 = layers.Conv2D(64*factor, (3, 3), activation='relu', padding='same',trainable = True)(pool_3)
    conv_42 = layers.Conv2D(64*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_41)
    # conv_43 = Conv2D(64*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_42)
    
    up_5   	= layers.UpSampling2D(size = (2,2))(conv_42)
    conv_51 = layers.Conv2D(32*factor, (3, 3), activation='relu', padding='same',trainable = True)(up_5)
    conv_52 = layers.Conv2D(32*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_51)
    
    up_6   	= layers.UpSampling2D(size = (2,2))(conv_52)
    conv_61 = layers.Conv2D(16*factor, (3, 3), activation='relu', padding='same',trainable = True)(up_6)
    conv_62 = layers.Conv2D(16*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_61)
    	# conv_63 = Conv2D(32*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_62)
    
    up_7   	= layers.UpSampling2D(size = (2,2))(conv_62)
    conv_71 = layers.Conv2D(8*factor, (3, 3), activation='relu', padding='same',trainable = True)(up_7)
    conv_72 = layers.Conv2D(8*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_71)
    conv_73 = layers.Conv2D(8*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_72)
    	# conv_74 = Conv2D(32*factor, (3, 3), activation='relu', padding='same',trainable = True)(conv_73)	
    
    layer_final = layers.Conv2D(1, (1, 1), activation='linear')(conv_73)
    
    model = keras.Model(inputs,layer_final)
    model.compile(optimizer=keras.optimizers.Adam(lr=1e-4), loss='mse', metrics=['mae'])
    model.summary()
    
    return model
