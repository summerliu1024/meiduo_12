from fdfs_client.client import Fdfs_client

"""from fdfs_client.client import Fdfs_client


client = Fdfs_client('meiudo_mall_12/utils/fastdfs/client.conf')

client.upload_by_filename('/Users/summer/Desktop/1.png')
"""


def main():
    client = Fdfs_client('client.conf')

    client.upload_by_filename('/Users/summer/Desktop/1.png')


if __name__ == '__main__':
    main()
