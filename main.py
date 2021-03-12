from tkinter import *
from tkinter import filedialog
from tkinter import ttk

current_dir = './'

# フォルダを指定して開く (デフォルトはカレント)
def open_dir():
    print('フォルダを開きます...')
    open_dir = filedialog.askdirectory(initialdir=current_dir)
    return open_dir  # 開いたフォルダのパスを返す


if __name__ == '__main__':
    
    # rootの初期化
    root = Tk()
    root.title('Photo Neat')
    root.geometry('800x400')

    main_frame = ttk.Frame(root, padding=4)
    
    path_entry = ttk.Entry(main_frame, width=30)
    path_entry.insert(END, 'フォルダを開くかパスを指定して下さい')
    
    open_dir_button = ttk.Button(main_frame, text='フォルダを開く', command=open_dir)

    files_label = ttk.Scrollbar

    info_label = ttk.Label(main_frame, text='情報:\nフォルダが選択されていません')



    

    # ウィジェットの色
    root.configure(background='gray')


    # ウィジェットの配置
    main_frame.pack()
    path_entry.pack(side=LEFT)
    open_dir_button.pack(side=LEFT)
    info_label.pack(side=BOTTOM)


    root.mainloop()
