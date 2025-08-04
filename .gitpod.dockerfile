FROM gitpod/workspace-base

RUN echo "CI version from base"

### NodeJS ###
USER gitpod
ENV NODE_VERSION=20.10.0
ENV TRIGGER_REBUILD=1

RUN curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | PROFILE=/dev/null bash \
    && bash -c ". .nvm/nvm.sh \
        && nvm install $NODE_VERSION \
        && nvm use $NODE_VERSION \
        && nvm alias default $NODE_VERSION \
        && npm install -g typescript yarn node-gyp" \
    && echo ". ~/.nvm/nvm.sh" >> /home/gitpod/.bashrc.d/50-node

ENV PATH=$PATH:/home/gitpod/.nvm/versions/node/v${NODE_VERSION}/bin

### Python ###
USER root
RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.12 python3.12-venv python3-pip

USER gitpod
RUN python3.12 -m pip install --no-cache-dir --upgrade pip && \
    python3.12 -m pip install --no-cache-dir --upgrade \
        setuptools wheel virtualenv pipenv pylint rope flake8 \
        mypy autopep8 pep8 pylama pydocstyle bandit notebook twine

ENV PYTHONUSERBASE=/workspace/.pip-modules \
    PIP_USER=yes
ENV PATH=$PYTHONUSERBASE/bin:$PATH

### Heroku CLI ###
RUN curl https://cli-assets.heroku.com/install.sh | sh

### MongoDB (6.0) ###
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb && \
    sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb && \
    sudo apt-get install -y gnupg links && \
    curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | \
    sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor && \
    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | \
    sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list && \
    sudo apt-get update -y && \
    sudo apt-get install -y mongodb-mongosh && \
    sudo apt-get clean -y && \
    sudo rm -rf /var/cache/apt/* /var/lib/apt/lists/* /tmp/* /home/gitpod/*.deb && \
    sudo chown -R gitpod:gitpod /home/gitpod/.cache/heroku/

### PostgreSQL ###
RUN sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && \
    sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 && \
    sudo apt-get update -y && \
    sudo apt-get install -y postgresql-12

ENV PGDATA="/workspace/.pgsql/data"
RUN mkdir -p ~/.pg_ctl/bin ~/.pg_ctl/sockets && \
    echo '#!/bin/bash\n[ ! -d $PGDATA ] && mkdir -p $PGDATA && initdb --auth=trust -D $PGDATA\npg_ctl -D $PGDATA -l ~/.pg_ctl/log -o "-k ~/.pg_ctl/sockets" start' > ~/.pg_ctl/bin/pg_start && \
    echo '#!/bin/bash\npg_ctl -D $PGDATA -l ~/.pg_ctl/log -o "-k ~/.pg_ctl/sockets" stop' > ~/.pg_ctl/bin/pg_stop && \
    chmod +x ~/.pg_ctl/bin/*

ENV PGDATABASE="postgres"
ENV PATH="/usr/lib/postgresql/12/bin:/home/gitpod/.nvm/versions/node/v${NODE_VERSION}/bin:$HOME/.pg_ctl/bin:$PATH"

### Bash Aliases ###
RUN echo 'alias run="python3 $GITPOD_REPO_ROOT/manage.py runserver 0.0.0.0:8000"' >> ~/.bashrc && \
    echo 'alias heroku_config=". $GITPOD_REPO_ROOT/.vscode/heroku_config.sh"' >> ~/.bashrc && \
    echo 'alias python=python3' >> ~/.bashrc && \
    echo 'alias pip=pip3' >> ~/.bashrc && \
    echo 'alias arctictern="python3 $GITPOD_REPO_ROOT/.vscode/arctictern.py"' >> ~/.bashrc && \
    echo 'alias font_fix="python3 $GITPOD_REPO_ROOT/.vscode/font_fix.py"' >> ~/.bashrc && \
    echo 'alias set_pg="export PGHOSTADDR=127.0.0.1"' >> ~/.bashrc && \
    echo 'alias mongo=mongosh' >> ~/.bashrc && \
    echo 'alias make_url="python3 $GITPOD_REPO_ROOT/.vscode/make_url.py "' >> ~/.bashrc

### Local Environment ###
ENV PORT="8080"
ENV IP="0.0.0.0"
ENV DANGEROUSLY_DISABLE_HOST_CHECK=true

