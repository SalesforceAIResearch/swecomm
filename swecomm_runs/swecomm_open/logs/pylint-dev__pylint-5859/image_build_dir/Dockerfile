FROM --platform=linux/x86_64 sweb.env.x86_64.e5bb89bf78258a7d14c34b:latest

COPY ./setup_repo.sh /root/
RUN /bin/bash /root/setup_repo.sh

WORKDIR /testbed/
