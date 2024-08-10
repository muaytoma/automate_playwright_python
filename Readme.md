## run test ##
pytest
pytest --junitxml=output/test-results.xml

## install docker jenkin ###

 docker build -t jenkins-python-playwright .


docker run --name jenkins-python-playwright \
  -u root \
  -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins-python-playwright

## jenkin ## 
1. Go to http://localhost:8080/login?from=%2F
2. Create credential at github then go to jenkin > manage jenkin > credential
3. Create pipeline, check script at Jenkinsfile
