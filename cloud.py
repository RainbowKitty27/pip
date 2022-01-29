import dropbox
class TransferData:
    def __init__(self, accessToken):
        self.accessToken=accessToken
    def upload_file(self, fileFrom, fileTo):
        dbx=dropbox.Dropbox(self.accessToken)
        with open(fileFrom,"rb") as f:
            dbx.files_upload(f.read(),fileTo)
def main():
    accessToken="sl.BA8hMDtkQnoLB7kw0BFtnynjPx8ZuWB1aaPNQBwNNJhFEfN9y2zxZQeKi2lAjGW-YmIEQSyArbJYUbuRgM0lhPSr6zpFToh6nIzfJ1htr1rIN1bhp6V38ZzYfozeW3Aryd8z0eECV1c"
    transferdata=TransferData(accessToken)
    fileFrom="random.txt"
    fileTo="/notafolder/randomjunior.txt"
    transferdata.upload_file(fileFrom,fileTo)
    print("file has been moved")
main()

            


