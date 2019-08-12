from app import flaskAppInstance
import logging as logger

if __name__ == '__main__':
    logger.debug("starting application")
    flaskAppInstance.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)


