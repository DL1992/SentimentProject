import os
import tarfile
from contextlib import closing
from urllib.request import urlopen

URL = ("http://www.cs.cornell.edu/people/pabo/"
       "movie-review-data/review_polarity.tar.gz")

ARCHIVE_NAME = URL.rsplit('/', 1)[1]
DATA_FOLDER = "Data"


def download_data_from_url():
    if not os.path.exists(DATA_FOLDER):

        if not os.path.exists(ARCHIVE_NAME):
            print("Downloading dataset from %s (3 MB)" % URL)
            opener = urlopen(URL)
            with open(ARCHIVE_NAME, 'wb') as archive:
                archive.write(opener.read())

        print("Decompressing %s" % ARCHIVE_NAME)
        with closing(tarfile.open(ARCHIVE_NAME, "r:gz")) as archive:
            archive.extractall(path='.')
        os.remove(ARCHIVE_NAME)


if __name__ == '__main__':
    download_data_from_url()
