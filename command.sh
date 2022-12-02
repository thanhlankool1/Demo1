build_docker_imgase (){
    echo "Start Build"
    docker build -t demo_app_lanlt23 .
    echo "End Build"
}

start(){
    echo "start app"
    docker-compose -f docker-compose/docker-compose-app.yml up -d
    echo "finish"
}

stop(){
    echo "start app"
    docker-compose -f docker-compose/docker-compose-app.yml down
    echo "finish"
}

start_redis_mongo(){
    echo "start app"
    docker-compose -f docker-compose/docker-compose.yml up -d
    echo "finish"
}


case $1 in
    build)
        build_docker_imgase
        ;;
    start)
        start
        ;;
    stop)
        stop
        ;;
    start_redis_mongo)
        start_redis_mongo
        ;;
    *)
        echo "Input: build or start_app"
esac