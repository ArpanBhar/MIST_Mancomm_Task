# Hill Cipher: Encryption and Decryption
## Explanation
The hill cipher is a substitution based encryption method where a matrix key is given and we use multiplication module 26 to generate a new character then replace that character in the original string
## Code:
```python
KEY = np.array([[9,4],[5,7]])
def hill_cipher(x):
    x = x.lower()
    if(len(x)%2!=0):
        x+='x'
    x = np.array([ord(i)-ord('a') for i in x])
    arr = []
    for i in range(0,len(x),2):
        temp = np.array([x[i],x[i+1]])
        temp = KEY @ temp  % 26
        x[i],x[i+1] = temp[0],temp[1]
    return "".join([chr(i+ord('a')) for i in x])
```
## Decryption using brute force:
If we know that the string must contain a certain string (`arpan` taken for example) we can list out all the strings containing that string and get the flag
```python
def hill_cipher_decrypter(y):
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    x = np.array([ord(i)-ord('a') for i in y])
                    temp_key = np.array([[i,j],[k,l]])
                    for m in range(0,len(x),2):
                        temp = np.array([x[m],x[m+1]])
                        temp = temp_key @ temp  % 26
                        x[m],x[m+1] = temp[0],temp[1]
                        temp_string = "".join([chr(i+ord('a')) for i in x])
                        if "arpan" in temp_string:
                            print(temp_string)
```
## Example Output:
```bash
Enter plaintext: arpanhereistheflag
Ciphertext: qpfxpkajqyepbllyyq
Decrypting the ciphertext using brute force...
Decrypted strings:
arpanhajqyepbllyyq
arpanherqyepbllyyq
arpanhereiepbllyyq
arpanhereistbllyyq
arpanhereisthelyyq
arpanhereistheflyq
arpanhereistheflag
narpanajqyepbllyyq
narpanveqyepbllyyq
narpanveieepbllyyq
narpanveiexsbllyyq
narpanveiexsbhlyyq
narpanveiexsbhkfyq
narpanveiexsbhkfaa
```
Here `arpanhereistheflag` is the required flag