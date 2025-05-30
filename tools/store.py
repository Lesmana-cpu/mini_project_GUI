import main
import library

def mulai():
    while True:
        
    
        print('warung gacor')
        play_again = input ('apakah ingin kembali ke menu sebelumnya [y/n]')
        
        
        if play_again == 'y':
            main.menu()
        else:
            library.exit_program
    
if __name__ == '__main__':
    mulai()