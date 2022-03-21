from multiprocessing import Process
import time

def acquire_data(arg):
	for i in range(5):
		print('acquiring data: {}'.format(arg))
		time.sleep(1.1)

def capture_video():
	for i in range(5):
		print('capture video')
		time.sleep(1)
		
if __name__ == '__main__':
	p_data = Process(target=acquire_data, args('foo',))
	p_video = Process(target = capture_video)
	
	p_data.start()
	p_video.start()
	
	p_data.join()
	p_video.join()
