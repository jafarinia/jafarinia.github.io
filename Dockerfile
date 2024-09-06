#Version 1.0
#FROM nvcr.io/nvidia/pytorch:23.04-py3

#ENV DEBIAN_FRONTEND noninteractive

#Extra Requirements
#RUN apt-get update && DEBIAN_FRONTEND=noninteractive TZ=US
#RUN apt-get update && apt-get install -y openslide-tools
#RUN pip install --upgrade pip && pip install openslide-python && pip install staintools && pip install spams && pip install wandb -qU && pip install dill && pip install scikit-image pip install openpyxl && pip install lifelines && pip install scikit-survival && pip install cox && pip install timm && pip install transformers && pip install pytorch-lightning && pip && pip install einops && pip install webdataset && pip install h5py && pip install lightly && pip install shapely

#Versopm 1.1
FROM histo:1.0
RUN apt-get update && apt install -y tmux && apt-get install -y openssh-server
