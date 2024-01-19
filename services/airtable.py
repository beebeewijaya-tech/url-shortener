from pyairtable import Api


# // deprecated


class Airtable:
    api = None
    table = None

    def __init__(self, settings):
        self.api = Api(settings.airtable_key)
        self.table = self.api.table(settings.airtable_base_id, "url_shorten")

    def all(self):
        return self.table.all()

    def all_by_session(self, session_id):
        return self.table.all(formula=f"session='{session_id}'")

    def get_by_short_url(self, short):
        return self.table.first(formula=f"short_url='{short}'")

    def create(self, url_shorten):
        return self.table.create(url_shorten)

    def delete(self, id):
        return self.table.delete(id)
