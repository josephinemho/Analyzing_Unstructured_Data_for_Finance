tmux new -s notebook3
docker run -it -p 8888:8888 -v `pwd`:/home/jovyan/work --name jup generalassembly/scipy-notebook
sudo apt-get updates
sudo apt-get update
sudo apt-get install docker.io
docker run -it -p 8888:8888 -v `pwd`:/home/jovyan/work --name jup generalassembly/scipy-notebook
sudo reboot
docker ps
sudo usermod -aG docker ubuntu
sudo reboot
docker stats
tmux new -s notebook3
docker ps -a
docker run -it -p 8888:8888 -v `pwd`:/home/jovyan/work --name jup generalassembly/scipy-notebook
