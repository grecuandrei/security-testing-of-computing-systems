import subprocess as sub

ORIGINAL_MSG = b'FIRE_NUKES_MELA!'
MODIFIED_MSG = b'SEND_NUDES_MELA!'
IV = '7ec00bc6fd663984c1b6c6fd95ceeef1'

def get_new_iv():
    old_iv = bytes.fromhex(IV)
    new_iv = b''.join([bytes([old_iv[i] ^ ORIGINAL_MSG[i] ^ MODIFIED_MSG[i] for i in range(len(old_iv))])])
    return new_iv

def main():
	new_iv = get_new_iv().hex()
	print(new_iv)
	process = sub.Popen(['./oracle', new_iv])

if __name__ == '__main__':
	main()