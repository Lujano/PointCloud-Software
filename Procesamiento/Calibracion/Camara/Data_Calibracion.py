import numpy as np



Sensor_Data = np.array([[2, 50, 370], [4, 135, 340], [6, 180, 313], [8, 210, 300], [10, 232, 295], [12, 245, 290],
                        [14, 255, 285], [16, 265, 280], [18, 272, 272], [ 20, 283, 269], [22, 287, 265], [24, 295, 265] ])
np.savetxt('Sensor_Data_Fix.out', Sensor_Data, fmt='%1.6e')