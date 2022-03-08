# easy-gift-to-gf

What better gift than a drawing for your girlfriend or boyfriend? In this project we use AnimeGANv2 to create a drawing from a photograph.

We will show an example of how to use it

We need to create a virtual environment
    
    python -m venv myvenv

Then we need to activate the virtual environment

    myvenv\Scripts\activate

We clone this repository and install the dependencies with the following command

    pip install -r requirements.txt
   
In addition, we need to install the dlib library, for this we execute the following, from [dlib](https://pypi.org/simple/dlib/)

    python -m install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf

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


