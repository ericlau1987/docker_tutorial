FROM jupyter/scipy-notebook

USER root

# RUN conda install --yes --name root \
# pymongo

USER jovyan

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]