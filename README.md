docker login 

docker build  -t test .


docker tag test microshak/ai_benchtest

docker push microshak/ai_benchtest