#!/bin/sh

BASE_DIR=$(dirname $0)
. $BASE_DIR/env/bin/activate

GUNICORN_CMD="./env/bin/gunicorn"
CELERY_CMD="./env/bin/python"

GUNICORN_PID="tmp/gunicorn.pid"
CELERY_PID="tmp/celery.pid"

GUNICORN_ARGS="wsgi:application -c gunicorn_conf.py --daemon --pid=$GUNICORN_PID"
CELERY_ARGS="manage.py celery worker --pidfile=$CELERY_PID --beat --detach"

start () {
    start-stop-daemon --start --pidfile $BASE_DIR/$1 --chdir $BASE_DIR --exec $2 -- $3
    return
}

stop () {
    start-stop-daemon --stop --pidfile $BASE_DIR/$1
}

usage(){
    echo "Usage: $N {start|stop|restart} {gunicorn|celery}" >&2
    exit 1
}

case "$2" in
    gunicorn)
        CMD=$GUNICORN_CMD
        PID=$GUNICORN_PID
        ARGS="$GUNICORN_ARGS"
        ;;
    celery)
        CMD=$CELERY_CMD
        PID=$CELERY_PID
        ARGS="$CELERY_ARGS"
        ;;
    *)
        usage
        ;;
esac


case "$1" in
    start)
        echo "Starting $2"
        start $PID $CMD "$ARGS"
        ;;
    stop)
        echo "Stopping $2"
        stop $PID
        ;;
    restart)
        echo "Restarting $2"
        stop $PID
        sleep 1
        start $PID $CMD "$ARGS"
        ;;
    *)
        usage
        ;;
esac

exit 0
