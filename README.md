# HenKanKunPO_py
Fix Red Hat (Japanese style guide issues)  for PO pre-filled content.

Dependencies
python modules
  polib
  jaconv


It converts Zenkaku alphabet characters, special characters, and numbers to hankaku ones.
Also it adds space between Zenkaku and Hankaku characters.

Before:
Red Hat Linuxは、すっごいオペレーティングシステムです。

After:
Red Hat Linux は、すっごいオペレーティングシステム。


Also, HenKanKunPO converts terminology without Cho-on expressions.

Before:
お使いのコンピュータで、/User/hiroshi/Desktopのディレクトリに移動してください。

After:
お使いのコンピューターで、/User/hiroshi/Desktop のディレクトリーに移動してださい。

Very cool!

How to use:
Type po file name as first argument. 
Put yogo file name as second argument.

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
