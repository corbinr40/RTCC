// C++ program for face detection

/*#include "/usr/local/include/opencv4/opencv2/objdetect.hpp"
#include "/usr/local/include/opencv4/opencv2/highgui.hpp"
#include "/usr/local/include/opencv4/opencv2/imgproc.hpp"
#include <iostream>*/

/*#include "opencv4/opencv2/objdetect.hpp"
#include "opencv4/opencv2/highgui.hpp"
#include "opencv4/opencv2/imgproc.hpp"
#include <iostream>*/

#include "opencv2/objdetect.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include <iostream>
//#include <raspicam/raspicam.h> //Raspberry Pi Camera Module

using namespace std;
using namespace cv;

//Function for Face Detection
void detectAndDraw(Mat&img, CascadeClassifier&cascade, double scale);
string cascadeName;

int main(int argc, const char** argv)
{
	// VideoCapture class for playing video for which faces to be detected
	VideoCapture capture;
	//raspicam::RaspiCam capture; //Pi Camera Object
	Mat frame, image;

	// PreDefined Trained XML classifiers
	CascadeClassifier cascade;
	double scale = 1;

	// Load Classifer model
	cascade.load("/cascade.xml");

	//Start Video feed
	capture.open(0);
	if(capture.isOpened() )
	{
		//Capture frames from video and detect faces
		cout << "Face Detection Started.... " << endl;
		while(1)
		{
			capture >> frame;
			if(frame.empty() )
				break;
			Mat frame1 = frame.clone();
			detectAndDraw(frame1, cascade, scale);
			char c = (char)waitKey(10);
			
			// Press q to exit from window
			if(c == 27 || c == 'q' || c == 'Q')
				break;
		}
	}
	else
		cout<<"Could not Open Camera";
		return 0;
}

void detectAndDraw(Mat& img, CascadeClassifier& cascade, double scale)
{
	vector<Rect> faces, faces2;
	Mat gray, smallImg;
	
	cvtColor(img, gray, COLOR_BGR2GRAY);
	double fx = 1 / scale;
	
	//Resize the Grayscale Image
	resize(gray, smallImg, Size(), fx, fx, INTER_LINEAR);
	equalizeHist(smallImg, smallImg);
	
	//Detect faces of different sizes using cascade classifier
	//cascade.detectMultiScale(smallImg, faces, 1.1, 2, 0|CASCADE_SCALE_IMAGE, Size(30,30));
	
	//Draw circles around the faces
	for (size_t i = 0; i < faces.size(); i++)
	{
		Rect r = faces[i];
		Mat smallImgROI;
		vector<Rect> nestedObjects;
		Point center;
		Scalar color = Scalar(255, 0, 0); //Colour for drawing tool
		int radius;
		
		double aspect_ratio = (double)r.width/r.height;
		if( 0.75 < aspect_ratio && aspect_ratio < 1.3)
		{
			center.x = cvRound((r.x + r.width*0.5)*scale);
            center.y = cvRound((r.y + r.height*0.5)*scale);
            radius = cvRound((r.width + r.height)*0.25*scale);
            circle( img, center, radius, color, 3, 8, 0 );
		}
		else
            rectangle( img, cv::Point(cvRound(r.x*scale), cvRound(r.y*scale)),
                    cv::Point(cvRound((r.x + r.width-1)*scale), 
                    cvRound((r.y + r.height-1)*scale)), color, 3, 8, 0);
        smallImgROI = smallImg( r );
    }
  
    // Show Processed Image with detected faces
    imshow( "Face Detection", img ); 
	}
	
