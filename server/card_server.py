from concurrent import futures
import logging


import grpc
import card_pb2
import card_pb2_grpc
import card_resources as card_resources


def get_card(card_db, point):
    for card in card_db:
        if card.id == 1:
            return card
    return None


class CardServicer(card_pb2_grpc.CardService):

    def __init__(self):
        self.db = card_resources.read_card_database()

    def GetCard(self, request, context):
        card = get_card(self.db, request)
        if card is None:
            return card_pb2.card(id=0, name="request")
        else:
            return card


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    card_pb2_grpc.add_CardServiceServicer_to_server(
        CardServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
