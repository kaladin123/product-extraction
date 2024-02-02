FROM amazonlinux:2

# Install system dependencies
RUN yum install -y <your-system-dependencies> && yum clean all

# Install AWS Lambda Runtime Interface Client (RIC)
RUN curl -Lo aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie \
    && chmod +x aws-lambda-rie \
    && mv aws-lambda-rie /usr/local/bin/

# Optional: Install additional tools or libraries
RUN pip install --no-cache-dir <your-python-libraries>

# Set up working directory
WORKDIR /var/task
