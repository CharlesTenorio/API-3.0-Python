from .base import Base


class QueryRecorrency(Base):

    def __init__(self, merchant, environment):

        super(QueryRecorrency, self).__init__(merchant)

        self.environment = environment

    def execute(self, payment_id):

        uri = '%s1/RecurrentPayment/%s' % (self.environment.api_query, payment_id)

        return self.send_request("GET", uri)
