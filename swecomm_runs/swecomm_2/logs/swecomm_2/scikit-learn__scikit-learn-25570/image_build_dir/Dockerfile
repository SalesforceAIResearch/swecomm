FROM --platform=linux/x86_64 sweb.env.x86_64.27dd9791e13f5c857a09f9:latest

COPY ./setup_repo.sh /root/
RUN /bin/bash /root/setup_repo.sh

WORKDIR /testbed/
