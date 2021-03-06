###### HenKanKunPO_py
##### Fixies Red Hat Japanese style guide misalignment for PO pre-filled contents.

### Dependencies
## python modules
polib  
jaconv


It converts Zenkaku alphabet characters, special characters, and numbers to hankaku ones.  
Also it adds space between Zenkaku and Hankaku characters.


Here are before and after examples  

Before:  
Ｒｅｄ　Ｈａｔ　Ｅｎｔｅｒｐｒｉｓｅ　Ｌｉｎｕｘ ８（ＲＨＥＬ ８）は、すっごいオペレーティングシステムです。

After:  
Red Hat Enterprise Linux 8 (RHEL 8) は、すっごいオペレーティングシステムです。


Also, HenKanKunPO converts terminologies (needs to be defined) without Cho-on expressions.

Before:  
お使いのコンピュータで、/User/hiroshi/Desktopのディレクトリに移動してください。


After:  
お使いのコンピューターで、/User/hiroshi/Desktop のディレクトリーに移動してください。


How to use:  
Specify a po file name as a first argument, yogo file name as a second argument, output file name as a third argument::
HenKanKunPO.py input-file-name.po yogo-file-name.txt ouptput-file-name.po

Example:  
$python3 HenkanKunPO.py XXX.po yogo.txt output.po

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
