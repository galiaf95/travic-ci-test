import MySQLdb as mdb
from string import ascii_letters as ai
from random import choice
import unittest

class Test(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_db(self):
      con = mdb.connect(host='127.0.0.1', user='travis', passwd='')
      crsr = con.cursor(mdb.cursors.DictCursor)
      db_name = ''.join(choice(ai) for i in xrange(10))
      print db_name
      crsr.execute('create database {}'.format(db_name))
      crsr.execute('show databases;')
      dbs = crsr.fetchall()
      created_db_found = False
      for db in dbs:
          print db['Database']
          if db['Database'].lower() == db_name.lower():
              created_db_found = True
      self.assertTrue(created_db_found)

if __name__ == '__main__':
    unittest.main()
