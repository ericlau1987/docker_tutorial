FROM continuumio/miniconda3

LABEL maintainer=@continuumio 

RUN conda update conda && \
    conda install --quiet --yes ipython && \
    conda install jupyter -y 

# RUN useradd hopefulhopper --create-home --shell /bin/bash \
#   && echo hopefulhopper:hopefulhopper | chpasswd \
#   && usermod -a -G staff hopefulhopper

# WORKDIR /home/yifuliu

# USER ericlau1987

# RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
#   && echo "conda activate base" >> ~/.bashrc

# CMD [ "jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser" ]
CMD ["ipython"]