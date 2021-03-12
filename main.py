# tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

# other imports
import os

current_dir = './'
flist = []


# フォルダを指定して開く (デフォルトはカレント)
def open_dir():
    print('フォルダを開きます...')
    open_dir = filedialog.askdirectory(initialdir=current_dir)
    update_flist(open_dir)
    return open_dir  # 開いたフォルダのパスを返す


# 画面に表示されているファイルを更新
def update_flist(dir):
    for f in os.listdir(dir):
        flist.append(f)
        lbox.insert(END, f)
        print(f, 'was added')
    info_label['text'] = '場所:{}'.format(dir)


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

    lbox = Listbox(main_frame, listvariable=StringVar(value=flist), height=20, selectmode=MULTIPLE)


    

    # ウィジェットの色
    root.configure(background='gray')


    # ウィジェットの配置
    main_frame.pack()
    path_entry.pack(side=LEFT)
    open_dir_button.pack(side=LEFT)
    info_label.pack(side=BOTTOM)
    lbox.pack(side=TOP)


    root.mainloop()
