from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

toaster.show_toast('Beli BBCA woi!', 'WOIII! harga murah!!! beli cuk', threaded=True, icon_path=None, duration=5)

import time
while toaster.notification_active():
    time.sleep(.1)