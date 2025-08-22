import segno
from colorama import Fore

def generateQr(data):
    '''
        This function takes the data entered by the user, 
        generates a QR code and saves it as a SVG image.
        '''
    # generate qr
    data_to_qr = segno.make(data, error='q')
    # define image name and path
    file_name = data.replace('/', '.')
    file_path = 'qr_files/' + file_name + '.svg'
    # save qr image
    data_to_qr.save(file_path, scale=10, dark='black', light=None)
    # print success message
    print(Fore.GREEN + f'QR code generated successfully and saved in the "qr_files" folder.')

if __name__ == "__main__":
    # program starts
    program_active = True
    while program_active == True:
        print(Fore.YELLOW + '-------------QR SVG GENERATOR-------------' +  Fore.RESET)
        # user input to generate qr code
        data_input = input('Insert text or link to generate QR code: ')
        # generate qr
        generateQr(data_input)
        # ask if the user wants to generate another qr
        program_continue = input(Fore.YELLOW + 'Generate another QR? (y/n): ' + Fore.RESET)
        if program_continue != 'y':
            print(Fore.YELLOW + '------------------------------------------' +  Fore.RESET)
            # program ends
            program_active = False


