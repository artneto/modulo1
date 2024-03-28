#Harry Potter and Ron Weasley are competing in a game of
#cards called Explosive Snap. Every time the match ends, they write it down
#who won or if it was a draw. Tell which of the two has won more times in
#last ten disputes, how many times he won and what was the first game in
#that there was a draw.

snapExplosivo = input().split(' ')
counterHarry = snapExplosivo.count('Harry')
counterRony = snapExplosivo.count('Rony')
i = 'empate'

if counterHarry > counterRony:
    print('Harry ganhou mais')
else:
    print('Rony ganhou mais')

print(f'{counterRony} vezes')

if i in snapExplosivo:
    print(f'A primeira partida com empate foi a {snapExplosivo.index('empate') +1}a')