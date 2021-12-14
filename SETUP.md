# Развертывание приложения с помощью AWS EC2, NGINX, GUNICORN

## Запускаем EC2 экземпляр на AWS, для этого войдите в консоль aws.
    * Выберите EC2 из всех сервисов
    * Выберите запуск New instance и выберите Ubuntu из списка.
    * Выберите любой из экземпляров, каждый из них имеет различные конфигурации.
    * Теперь настройте группы безопасности и откройте порты 8000 и 9000. Просмотрите и запустите ваш экземпляр.

## Подключение к Экземпляру
### Мы можем подключиться к экземпляру, используя опцию 'connect' в консоли (или с помощью putty или любого другого подобного инструмента ). После подключения запустите следующие команды
    * sudo apt-get update
### Установливаем python , pip и django
    * sudo apt install python
    * sudo apt install python3-pip
    * pip3 install django
### Теперь, когда мы установили наши зависимости, мы можем создать папку, в которую мы скопируем наше приложение django.
    * cd  /home/ubuntu/
    * mkdir Project
    * cd Project
    * mkdir ProjectName
    * cd ProjectName
### Теперь мы поместим наш код по следующему пути.
    * Перейдите в только что созданную папку ( /home/ubuntu/Project/ProjectName/ )
    * git clone <repository-url>
### Это клонирует репозиторий в папку, и в следующий раз мы сможем просто вытащить изменения с помощью git pull.
### Мы должны внести некоторые изменения в settings.py в нашем проекте.
    * Вставьте свои секретные ключи и пароли в переменные окружения
    * Установить Debug = False
    * Добавте Ваш домейн в ALLOWED_HOSTS
    * BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    * STATIC_ROOT = os.path.join(BASE_DIR, “static”)
### Выполните следующие действия, чтобы миграция модели произошла и все статические файлы были собраны в общую папку (путь указан в STATIC_ROOT).
    * manage.py makemigrations
    * manage.py migrate
    * manage.py collectstatic
## Установка Nginx
### Для установки Nginx выполните команду
 * sudo apt install nginx
### Есть конфигурационный файл с именем по умолчанию в /etc/nginx/sites-enabled/, который имеет базовую настройку для NGINX, отредактируйте этот файл.
    * sudo vi default
### Добавим proxy_pass http://0.0.0.0:9000 и укажем путь к нашей статической папке, добавив путь внутри каталога /static/. Убедитесь, что вы собрали все статические файлы в общую папку, запустив команду
    * manage.py collectstatic
### Теперь запустите сервер nginx
    * sudo service nginx start
## Установка Gunicorn
    * pip install gunicorn
### Убедитесь, что Вы находитесь в папке проекта, например: /home/ubuntu/Project, и запустите следующую команду, чтобы запустить gunicorn
    * gunicorn ProjectName.wsgi:application- -bind 0.0.0.0:9000
### Теперь, когда мы установили и настроили nginx и gunicorn, к нашему приложению можно получить доступ через DNS экземпляра ec2.