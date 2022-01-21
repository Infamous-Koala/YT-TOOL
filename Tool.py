import pytube
from pytube import YouTube

print("""
                                                                                                                                                                                             
                                                                                                                                                                                             
KKKKKKKKK    KKKKKKK                                lllllll                       YYYYYYY       YYYYYYY        tttt               TTTTTTTTTTTTTTTTTTTTTTT                            lllllll 
K:::::::K    K:::::K                                l:::::l                       Y:::::Y       Y:::::Y     ttt:::t               T:::::::::::::::::::::T                            l:::::l 
K:::::::K    K:::::K                                l:::::l                       Y:::::Y       Y:::::Y     t:::::t               T:::::::::::::::::::::T                            l:::::l 
K:::::::K   K::::::K                                l:::::l                       Y::::::Y     Y::::::Y     t:::::t               T:::::TT:::::::TT:::::T                            l:::::l 
KK::::::K  K:::::KKK  ooooooooooo    aaaaaaaaaaaaa   l::::l  aaaaaaaaaaaaa        YYY:::::Y   Y:::::YYttttttt:::::ttttttt         TTTTTT  T:::::T  TTTTTooooooooooo     ooooooooooo   l::::l 
  K:::::K K:::::K   oo:::::::::::oo  a::::::::::::a  l::::l  a::::::::::::a          Y:::::Y Y:::::Y  t:::::::::::::::::t                 T:::::T     oo:::::::::::oo oo:::::::::::oo l::::l 
  K::::::K:::::K   o:::::::::::::::o aaaaaaaaa:::::a l::::l  aaaaaaaaa:::::a          Y:::::Y:::::Y   t:::::::::::::::::t                 T:::::T    o:::::::::::::::o:::::::::::::::ol::::l 
  K:::::::::::K    o:::::ooooo:::::o          a::::a l::::l           a::::a           Y:::::::::Y    tttttt:::::::tttttt                 T:::::T    o:::::ooooo:::::o:::::ooooo:::::ol::::l 
  K:::::::::::K    o::::o     o::::o   aaaaaaa:::::a l::::l    aaaaaaa:::::a            Y:::::::Y           t:::::t                       T:::::T    o::::o     o::::o::::o     o::::ol::::l 
  K::::::K:::::K   o::::o     o::::o aa::::::::::::a l::::l  aa::::::::::::a             Y:::::Y            t:::::t                       T:::::T    o::::o     o::::o::::o     o::::ol::::l 
  K:::::K K:::::K  o::::o     o::::oa::::aaaa::::::a l::::l a::::aaaa::::::a             Y:::::Y            t:::::t                       T:::::T    o::::o     o::::o::::o     o::::ol::::l 
KK::::::K  K:::::KKo::::o     o::::a::::a    a:::::a l::::la::::a    a:::::a             Y:::::Y            t:::::t    tttttt             T:::::T    o::::o     o::::o::::o     o::::ol::::l 
K:::::::K   K::::::o:::::ooooo:::::a::::a    a:::::al::::::a::::a    a:::::a             Y:::::Y            t::::::tttt:::::t           TT:::::::TT  o:::::ooooo:::::o:::::ooooo:::::l::::::l
K:::::::K    K:::::o:::::::::::::::a:::::aaaa::::::al::::::a:::::aaaa::::::a          YYYY:::::YYYY         tt::::::::::::::t           T:::::::::T  o:::::::::::::::o:::::::::::::::l::::::l
K:::::::K    K:::::Koo:::::::::::oo a::::::::::aa:::l::::::la::::::::::aa:::a         Y:::::::::::Y           tt:::::::::::tt           T:::::::::T   oo:::::::::::oo oo:::::::::::ool::::::l
KKKKKKKKK    KKKKKKK  ooooooooooo    aaaaaaaaaa  aaallllllll aaaaaaaaaa  aaaa         YYYYYYYYYYYYY             ttttttttttt             TTTTTTTTTTT     ooooooooooo     ooooooooooo  llllllll
                                                                                                                                                                                             
                                                                                                                                                                                             
                                                                                                                                                                                             
                                                                                                                                                                                             
                                                                                                                                                                                             
                                                                                                                                                                                             
                                                                                                                                                                                             
""")
link = input("link ")
file_type = input("file type (mp3/mp4) ")
video_quality = input("video_quality ")


yt = YouTube(link)
yt.filter.stream(progressive=True, file_extension= file_type)
yt.download()
