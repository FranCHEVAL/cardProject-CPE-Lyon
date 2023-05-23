from __future__ import print_function

import logging

import grpc
import card_pb2
import card_pb2_grpc
import card_resources as card_resources

def guide_get_one_feature(stub, user):
    card = stub.GetCard(user)
    if not card.name:
        print("Server returned incomplete feature")
        return

    if card.name:
        print("Feature called %s" % card.name)
    else:
        print("Found no feature at %s" % card.name)


def guide_get_feature(stub):
    guide_get_one_feature(
        stub, card_pb2.User(id=1))


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = card_pb2_grpc.CardServiceStub(channel)
        print("-------------- GetCard --------------")
        guide_get_feature(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
