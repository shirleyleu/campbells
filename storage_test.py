import unittest
from storage import ComicManagerAlchemy


class TestCharacters(unittest.TestCase):
    def setUp(self):
        self.cm = ComicManagerAlchemy('sqlite:///foxtrot.db')

    def test_characters_from_date(self):
        self.assertEqual(self.cm.characters_from_date("1988-08-03"), ['Jason', 'punishment', 'Roger'])

    def test_dates_from_character(self):
        self.assertEqual(self.cm.dates_from_character("Marcus"),
                         ['1988-05-30', '1988-08-09', '1989-03-15', '1989-06-21', '1991-06-11', '1992-03-11',
                          '1992-08-06', '1992-10-06', '1992-10-07', '1992-10-10', '1994-03-03', '1996-01-20',
                          '1996-02-07', '1996-02-15', '1996-03-20', '1996-05-13', '1996-05-18', '1996-07-22',
                          '1996-07-23', '1996-07-24', '1996-07-25', '1996-07-26', '1996-08-03', '1996-09-22',
                          '1996-10-21', '1996-10-30', '1996-11-01', '1996-11-29', '1996-12-24', '1997-01-10',
                          '1997-01-24', '1997-02-13', '1997-03-04', '1997-03-16', '1997-04-06', '1997-04-27',
                          '1997-05-04', '1997-05-12', '1997-05-17', '1997-06-01', '1997-06-15', '1997-06-24',
                          '1997-06-25', '1997-06-26', '1997-06-27', '1997-06-28', '1997-06-29', '1997-07-01',
                          '1997-07-02', '1997-07-03', '1997-07-04', '1997-07-05', '1997-07-06', '1997-07-07',
                          '1997-07-08', '1997-07-09', '1997-07-10', '1997-07-11', '1997-07-12', '1997-07-13',
                          '1997-07-14', '1997-07-15', '1997-07-16', '1997-07-17', '1997-07-18', '1997-07-19',
                          '1997-07-20', '1997-07-21', '1997-07-22', '1997-07-23', '1997-07-24', '1997-07-25',
                          '1997-07-26', '1997-07-28', '1997-07-29', '1997-07-30', '1997-08-01', '1997-08-02',
                          '1997-08-06', '1997-08-09', '1997-09-09', '1997-09-10', '1997-09-11', '1997-09-12',
                          '1997-09-28', '1997-10-10', '1997-10-13', '1997-10-17', '1997-10-19', '1997-11-20',
                          '1997-12-06', '1997-12-30', '1998-01-11', '1998-01-30', '1998-02-13', '1998-02-16',
                          '1998-03-01', '1998-03-17', '1998-04-02', '1998-04-03', '1998-04-19', '1998-05-02',
                          '1998-05-05', '1998-05-07', '1998-05-08', '1998-05-09', '1998-05-17', '1998-05-31',
                          '1998-06-18', '1998-06-19', '1998-06-28', '1998-07-06', '1998-07-08', '1998-07-16',
                          '1998-08-04', '1998-08-16', '1998-09-13', '1998-09-27', '1998-10-14', '1998-11-01',
                          '1998-11-20', '1998-12-04', '1998-12-07', '1998-12-08', '1998-12-09', '1998-12-27',
                          '1999-02-21', '1999-03-17', '1999-05-04', '1999-06-03', '1999-07-11', '1999-08-06',
                          '1999-08-07', '1999-08-15', '1999-08-16', '1999-08-23', '1999-08-24', '1999-08-25',
                          '1999-08-26', '1999-08-27', '1999-09-14', '1999-09-17', '1999-09-21', '1999-09-22',
                          '1999-09-23', '1999-09-24', '1999-09-25', '1999-09-26', '1999-10-27', '1999-10-31',
                          '1999-11-06', '1999-12-12', '1999-12-26', '1999-12-28', '1999-12-29', '2000-01-03',
                          '2000-01-16', '2000-02-09', '2000-02-10', '2000-02-25', '2000-03-16', '2000-03-18',
                          '2000-04-08', '2000-04-09', '2000-04-19', '2000-04-20', '2000-04-21', '2000-04-27',
                          '2000-05-19', '2000-06-05', '2000-06-06', '2000-06-07', '2000-06-08', '2000-06-09',
                          '2000-06-10', '2000-06-11', '2000-06-12', '2000-06-13', '2000-06-14', '2000-06-15',
                          '2000-06-16', '2000-06-17', '2000-06-19', '2000-06-20', '2000-06-21', '2000-06-22',
                          '2000-06-23', '2000-06-24', '2000-06-25', '2000-06-26', '2000-06-27', '2000-06-28',
                          '2000-06-29', '2000-06-30', '2000-07-01', '2000-07-03', '2000-07-04', '2000-07-05',
                          '2000-07-06', '2000-07-07', '2000-07-08', '2000-07-09', '2000-07-10', '2000-07-11',
                          '2000-07-12', '2000-07-13', '2000-07-14', '2000-07-15', '2000-07-17', '2000-07-21',
                          '2000-07-22', '2000-08-04', '2000-08-25', '2000-09-05', '2000-09-06', '2000-09-07',
                          '2000-09-08', '2000-09-10', '2000-09-24', '2000-10-12', '2000-10-22', '2000-10-29',
                          '2000-11-12', '2000-11-19', '2000-11-25', '2000-12-31', '2001-01-11', '2001-01-13',
                          '2001-01-14', '2001-01-28', '2001-03-04', '2001-04-16', '2001-04-20', '2001-04-23',
                          '2001-04-27', '2001-06-07', '2001-06-08', '2001-06-10', '2001-06-19', '2001-06-24',
                          '2001-06-27', '2001-06-29', '2001-07-12', '2001-09-14', '2001-10-15', '2001-10-18',
                          '2001-10-22', '2001-10-25', '2001-10-26', '2001-10-28', '2001-11-03', '2001-12-30',
                          '2002-01-15', '2002-01-19', '2002-01-22', '2002-02-07', '2002-02-11', '2002-02-12',
                          '2002-02-13', '2002-02-15', '2002-02-16', '2002-03-08', '2002-03-15', '2002-04-16',
                          '2002-04-20', '2002-04-23', '2002-04-26', '2002-05-25', '2002-06-02', '2002-06-10',
                          '2002-06-11', '2002-06-12', '2002-06-13', '2002-06-14', '2002-06-15', '2002-06-28',
                          '2002-07-14', '2002-07-18', '2002-07-20', '2002-07-25', '2002-07-28', '2002-08-04',
                          '2002-08-27', '2002-09-08', '2002-09-18', '2002-10-20', '2002-10-31', '2002-11-05',
                          '2002-11-14', '2002-12-06', '2003-01-04', '2003-01-22', '2003-01-29', '2003-02-02',
                          '2003-02-12', '2003-03-02', '2003-03-23', '2003-03-24', '2003-03-25', '2003-03-26',
                          '2003-03-27', '2003-03-28', '2003-03-29', '2003-04-29', '2003-05-09', '2003-06-03',
                          '2003-06-04', '2003-06-05', '2003-06-06', '2003-07-13', '2003-07-16', '2003-07-17',
                          '2003-07-20', '2003-07-21', '2003-07-26', '2003-08-11', '2003-08-17', '2003-09-12',
                          '2003-09-18', '2003-09-21', '2003-09-29', '2003-10-12', '2003-11-11', '2003-11-12',
                          '2003-11-15', '2003-11-19', '2003-12-07', '2003-12-24', '2003-12-28', '2004-01-02',
                          '2004-01-06', '2004-01-09', '2004-01-13', '2004-01-18', '2004-01-25', '2004-02-26',
                          '2004-03-21', '2004-04-17', '2004-04-18', '2004-05-16', '2004-05-23', '2004-05-29',
                          '2004-06-06', '2004-06-17', '2004-06-20', '2004-06-22', '2004-06-24', '2004-06-27',
                          '2004-06-30', '2004-07-01', '2004-07-07', '2004-07-08', '2004-07-09', '2004-07-17',
                          '2004-08-08', '2004-08-11', '2004-09-07', '2004-09-13', '2004-09-19', '2004-09-26',
                          '2004-10-22', '2004-10-23', '2004-10-31', '2004-11-09', '2004-11-13', '2004-12-07',
                          '2004-12-08', '2004-12-15', '2004-12-28', '2004-12-30', '2005-01-02', '2005-01-31',
                          '2005-02-01', '2005-02-02', '2005-02-03', '2005-02-04', '2005-02-05', '2005-02-20',
                          '2005-03-04', '2005-04-05', '2005-04-08', '2005-04-17', '2005-04-26', '2005-04-27',
                          '2005-04-28', '2005-04-29', '2005-04-30', '2005-06-03', '2005-06-05', '2005-06-19',
                          '2005-06-27', '2005-06-29', '2005-07-01', '2005-07-02', '2005-07-15', '2005-08-13',
                          '2005-08-31', '2005-10-11', '2005-10-16', '2005-10-22', '2005-10-31', '2005-11-16',
                          '2005-12-07', '2005-12-30', '2006-01-17', '2006-02-09', '2006-02-12', '2006-02-26',
                          '2006-03-18', '2006-03-28', '2006-04-02', '2006-04-12', '2006-05-21', '2006-06-01',
                          '2006-06-03', '2006-06-25', '2006-07-23', '2006-08-03', '2006-10-08', '2006-10-25',
                          '2006-11-07', '2006-11-08', '2006-11-11', '2006-11-25', '2006-12-03', '2007-01-07',
                          '2007-02-11', '2007-06-10', '2007-10-21', '2008-02-17', '2008-04-27', '2008-05-25',
                          '2008-06-29', '2008-10-12', '2008-11-09', '2009-01-04', '2009-02-08', '2009-03-01',
                          '2009-03-22', '2009-05-03', '2009-06-14', '2009-06-28', '2009-07-19', '2009-10-04',
                          '2009-12-13', '2010-02-07', '2010-03-14', '2010-04-18', '2010-07-11', '2010-08-08',
                          '2010-09-19', '2010-11-14', '2011-01-16', '2011-01-23', '2011-02-27', '2011-03-06',
                          '2011-03-13', '2011-03-20', '2011-05-01', '2011-07-10', '2011-07-17', '2011-10-02',
                          '2011-10-30', '2012-01-29', '2012-05-06', '2012-05-27', '2012-07-29', '2012-08-05',
                          '2012-10-28', '2012-12-02', '2013-01-20', '2013-07-14', '2013-08-18', '2013-09-22',
                          '2013-10-06', '2013-11-03', '2013-11-17', '2014-01-05', '2014-01-26', '2014-02-16',
                          '2014-04-06', '2014-06-01', '2014-06-29', '2014-07-27', '2014-09-07', '2014-09-21',
                          '2014-10-05', '2014-10-19', '2014-10-26', '2015-01-04', '2015-01-18', '2015-02-01',
                          '2015-02-08', '2015-03-15', '2015-03-29', '2015-04-12', '2015-04-26', '2015-05-31',
                          '2015-06-07', '2015-08-02', '2015-08-23', '2015-11-01', '2015-12-13'])

    def test_search_transcripts(self):
        self.assertEqual(self.cm.search_transcripts("skeeter falls"),
                         ['1996-08-12', '1996-08-15', '1996-08-16', '1996-08-24'])

    def test_get_next_comic(self):
        self.assertEqual(self.cm.get_next_comic('1988-08-13'), '1988-08-15')

    def test_get_previous_comic(self):
        self.assertEqual(self.cm.get_previous_comic('1988-08-15'), '1988-08-13')
        self.assertEqual(self.cm.get_previous_comic('1992-03-31'), '1992-03-30')


if __name__ == '__main__':
    unittest.main()
