FROM dokken/ubuntu-20.04
RUN apt-get update && sudo apt-get install -y gnupg software-properties-common
RUN wget -O- https://apt.releases.hashicorp.com/gpg | \
    gpg --dearmor | \
    sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
RUN apt-get update
RUN apt-get install gnupg
RUN apt-get install software-properties-common
RUN apt-get install curl
RUN echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
    https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
    sudo tee /etc/apt/sources.list.d/hashicorp.list
# RUN curl -fsSL https://get.docker.com | sh
RUN apt-get update
RUN apt-get install -y terraform
RUN apt-get install -y awscli
