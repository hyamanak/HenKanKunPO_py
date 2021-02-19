# HenKanKunPO_py
### Fixies Red Hat Japanese style guide misalignment for PO pre-filled contents.

### Dependencies
## python modules
polib  
jaconv


It converts Zenkaku alphabet characters, special characters, and numbers to hankaku ones.  
Also it adds space between Zenkaku and Hankaku characters.

Before:  
Ｒｅｄ　Ｈａｔ　Ｅｎｔｅｒｐｒｉｓｅ　Ｌｉｎｕｘ ８（ＲＨＥＬ ８）は、すっごいオペレーティングシステムです。

After:  
Red Hat Enterprise Linux 8 (RHEL 8) は、すっごいオペレーティングシステムです。


Also, HenKanKunPO converts terminology without Cho-on expressions.

Before:  
お使いのコンピュータで、/User/hiroshi/Desktopのディレクトリに移動してください。

After:  
お使いのコンピューターで、/User/hiroshi/Desktop のディレクトリーに移動してださい。

Very cool!

How to use:  
Type po file name as a first argument. 
Put yogo file name as a second argument.

$python3 HenkanKunPO.py XXX.po yogo.txt

About Yogo.txt

Put Japanese terms that needs to be Cho-on expression such as コンピュータ, レジストリ, バイナリ separating them by 
breaking each line. 



-- sample Yogo.txt --  
コンピュータ  
バイナリ  
レジストリ  


Those terms will have "ー" added, therefore, they will look in output.po file:
コンピューター
バイナリー
レジストリー
