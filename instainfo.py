import instaloader
from pyfiglet import Figlet
from colorama import Fore, Style

def profil_bilgilerini_al(kullanici_adi):
    L = instaloader.Instaloader()
    try:
        profil = instaloader.Profile.from_username(L.context, kullanici_adi)
        print("Kullanıcı Adı:", profil.username)
        print("Tam Adı:", profil.full_name)
        print("Biyografi:", profil.biography)
        print("Profil Resmi URL'si:", profil.profile_pic_url)
        print("Dış Bağlantı URL'si:", profil.external_url)
        print("Gönderi Sayısı:", profil.mediacount)
        print("Takipçi Sayısı:", profil.followers)
        print("Takip Edilen Sayısı:", profil.followees)
        print("Gizli hesap mı:", profil.is_private)
        print("Doğrulanmış hesap mı:", profil.is_verified)
        print("İş hesabı mı:", profil.is_business_account)
        print("IGTV video sayısı:", profil.igtvcount)
    except instaloader.ProfileNotExistsException:
        print(f"{kullanici_adi} Instagram'da kayıtlı değil.")

def figlet_yazisi_yaz(yazi):
    figlet = Figlet(font='slant')
    return figlet.renderText(yazi)

# Kullanıcıdan Instagram kullanıcı adını al
print(Fore.BLUE +"-"*70)
kullanici_adi = input(Fore.BLUE +"Lütfen bilgilerini almak istediğiniz Instagram kullanıcı adını girin: ")

figlet_metni = figlet_yazisi_yaz("MKA CHECKER")
print(Fore.GREEN + figlet_metni + Style.RESET_ALL)
profil_bilgilerini_al(kullanici_adi)