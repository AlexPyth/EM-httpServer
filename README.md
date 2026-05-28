# Инструкция запуска проекта на ОС семейства Debian:
### 1. Устанавливаем uidmap, dbus-user-session, curl, git:
	apt install uidmap dbus-user-session curl git
### 2. Добавляем возможность маршрутизировать трафик и биндить порт 80 пользователем:
	echo -e "\nnet.ipv4.ip_forward=1\nnet.ipv4.ip_unprivileged_port_start=80" | tee -a /etc/sysctl.conf
	sysctl --system
### 3. Устанавливаем Docker с помощью официального скрипта от разработчика:
	curl -fsSL https://get.docker.com/ | sh
### 4. Создаём пользователя, который будет запускать проект, и присваиваем ему пароль:
	useradd -m -s /bin/bash em-docker-user
	passwd em-docker-user
### 5. Для запуска проекта после перезагрузки хоста включ lingering для пользователя:
	loginctl enable-linger em-docker-user
### 6. Открываем CLI от пользователя "em-docker-user", все дальнейшие действия выполняем под ним;

### 7. Устанавливаем Docker для пользователя в режиме rootless:
	dockerd-rootless-setuptool.sh install
### 8. Клонируем репозиторий:
	git clone https://github.com/AlexPyth/EM-httpServer.git
### 9. Заходим в директорию с проектом и запускаем контейнеры:
	cd ~/EM-httpServer && docker compose up -d --build


# Проверка работы:
Отправить "GET /" запрос на IP хоста (например, командой ```curl http://localhost``` на хосте).

**Результат**: в ответе будет текст "**Hello from Effective Mobile!**".


# Схема взаимодействия:
1. Порт **80** хоста слушает TCP трафик и перенаправляет пакеты на порт **80** контейнера **nginx**;
2. Nginx проксирует http-запросы к "/" на порт **8080** контейнера **backend**. На ресурсы, отличные от "/", отдаёт ошибку **HTTP 404**. На методы, отличные от "GET", отдаёт ошибку **HTTP 405**;
3. В контейнере **backend** запущен **http.server**, который слушает HTTP/TCP трафик на порту **8080**, и при запросе "GET /" отдаёт текст "Hello from Effective Mobile!".


# Используемые технологии:
1. ОС Linux;
2. Docker, Docker Compose;
3. Python, http.server;
4. Nginx.
