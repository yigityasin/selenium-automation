docker network create grid

docker run -d -p 4444:4444 --net grid --name selenium-hub selenium/hub

docker run -d -p 5900:5900 --net grid --name chrome-debug -e HUB_HOST=selenium-hub selenium/node-chrome-debug

docker run -d -p 5901:5900 --net grid --name chrome-debug2 -e HUB_HOST=selenium-hub selenium/node-chrome-debug
