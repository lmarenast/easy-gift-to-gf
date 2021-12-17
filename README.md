# easy-gift-to-gf

What better gift than a drawing for your girlfriend or boyfriend? In this project we use AnimeGANv2 to create a drawing from a photograph.

We will show an example of how to use it

We need to create a virtual environment with python 3.6, for this we use the following command
    
    python -m venv env-py36

Then we need to activate the virtual environment

    env-py36\Scriptts\activate

We clone this repository and install the dependencies with the following command

    pip install -r requirements.txt

Now, we go to the code folder and execute the script

    cd code
    python inference.py

After doing this, the windows explorer opens to select the photo

<img src="samples\1.png">

Then, the result will be displayed

<img src="samples\2.png">

In addition the resulting image will be automatically saved in D: \ easy_gif_to_gf \ output.jpg

<img src="samples\3.png">

Model taken from: [AnimeGANv2](https://github.com/TachibanaYoshino/AnimeGANv2)


