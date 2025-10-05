# split-piping stderr and stdout

Approach: take the stderr of /challenge/hack and redirect it to the imaginary file(stdin) of /challenge/the and pipe the stdout to /challenge/planet

```bash
hacker@piping~split-piping-stderr-and-stdout:~$ /challenge/hack 2> >(/challenge/the) | /challenge/planet
Congratulations, you have learned a redirection technique that even experts 
struggle with! Here is your flag:
pwn.college{EnUFsJdhOZ9zgSrDdcvh7r1iNQU.dFDNwYDL1ATN0czW}
```