from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast(
    "bildirim  başlığı",
    "bildirim içeriği",
    #"aw",
    duration=3,
    icon_path="alert.ico"
)