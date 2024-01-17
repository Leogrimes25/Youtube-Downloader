from pytube import YouTube
import customtkinter
import tkinter

app = customtkinter.CTk()
app.geometry('720x600')
app.title('Youtube Videos Downloader')


def download_start():
    try:
        link = entrada_link.get()
        ytObject = YouTube(link)
        download = ytObject.streams.get_highest_resolution()
        download.download()

    except ConnectionError:
        print("An Error has Occurred")
    print("Download Completed")


def download_start_audio():
    try:
        link = entrada_link.get()
        ytObject = YouTube(link)
        streams = ytObject.streams.all()
        download = next((s for s in streams if "video/mp4" in s.mime_type), None)

        if download:
            download.download()
            print("Download Completed")
        else:
            print("Não foi possível encontrar a stream de áudio.")

    except ConnectionError:
        print("An Error has Occurred")


url_link = tkinter.StringVar()

label_link = customtkinter.CTkLabel(app, text='Insira a URL :', height=10, width=10)
label_link.pack(padx=40, pady=40)

entrada_link = customtkinter.CTkEntry(app, height=50, width=500, textvariable=url_link)
entrada_link.pack()

botao_download = customtkinter.CTkButton(app, text='Download em Alta Resolução', width=50, height=50,
                                         command=download_start)
botao_download.place(x=120, y=250)

botao_download_2 = customtkinter.CTkButton(app, text='Baixar Apenas Áudio', width=50, height=50,
                                           command=download_start_audio)
botao_download_2.place(x=400, y=250)

app.mainloop()
