import subprocess
def main():
    vbsfile= input('バッチファイル名（拡張子除く）>> ')  
    path=r'C:\\Users\\user\\git\\windows_macro\\vvvvv.bat'
    with open(path, encoding='utf-8') as f:
        s=f.read()
    s=s.replace('vvvvv', vbsfile)
    path_w=r'C:\\Users\\user\\git\\windows_macro\\runvbs_'+vbsfile+r'.bat'
    with open(path_w, mode='w') as f:
        f.write(s)
if __name__ == "__main__":
    main()