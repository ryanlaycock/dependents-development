import os
from redis import Redis
from neo4j import GraphDatabase

def get_redis():
    # if a custom IP for redis has been specified, use it, else default to localhost
    redis_ip = os.environ.get('REDIS_IP') 
    if (redis_ip == None):
        redis_ip = "localhost"

    # if a custom port for redis has been specified, use it, else default to localhost
    redis_port = os.environ.get('REDIS_PORT')
    if (redis_port == None):
        redis_port = "6379"

    redis_password = os.environ.get('REDIS_PASSWORD')
    if (redis_password == None):
        return Redis(redis_ip, redis_port)
    else:
        return Redis(redis_ip, redis_port, password=redis_password)

def get_neo4j():
    neo4j_ip = os.environ.get('NEO4J_IP') 
    if (neo4j_ip == None):
        neo4j_ip = "localhost"
    neo4j_ip = "bolt://" + neo4j_ip + ":7687"

    neo4j_user = os.environ.get('NEO4J_USER') 
    if (neo4j_user == None):
        raise ValueError('NEO4J_USER environment variable must be set.')

    neo4j_password = os.environ.get('NEO4J_PASS') 
    if (neo4j_password == None):
        raise ValueError('NEO4J_PASS environment variable must be set.')

    return GraphDatabase.driver(neo4j_ip, auth=(neo4j_user, neo4j_password),
                                encrypted=False)
