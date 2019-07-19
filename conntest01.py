#https://www.programcreek.com/python/example/107948/ldap3.Connection

from ldap3 import Server, Connection, SUBTREE

LDAP_URL = 'ldap1-slave.rettorato.unito.it'
username=
password=

server = Server(host=LDAP_URL, port=636, use_ssl=True, get_info='ALL')

conn = Connection(server, user=username, password=password, auto_bind='NONE', version=3,
                            authentication='SIMPLE', client_strategy='SYNC', auto_referrals=False,
                            check_names=True, read_only=True, lazy=False, raise_exceptions=False)

if not conn.bind():
      self.logger.error("ldap_bind: Bind error occurred: {}".format(conn.result))

print(conn)

conn.search(search_base ='ou=utenti,o=unito,dc=unito,dc=it',search_filter='(uid=sbacciag)',attributes = ['sn'])
print(conn.result)
print(conn.response)



