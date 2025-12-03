import time
start = time.process_time()

BossHealth, BossDamage = 71,10
PlayerHealth, PlayerMana = 50,500
spellsCost = {
    'magic missile': 53,
    'drain': 73,
    'sheild': 113,
    'recharge': 229,
    'poison': 173
}
def bfs(BossH, PlayerH, Mana, Sheild, Poison, Recharge,playerTurn,manaUsed):
    movesList = list(spellsCost.keys())
    poison,sheild,recharge = Poison,Sheild,Recharge
    bossh,mana,bossDam = BossH,Mana,BossDamage
    if Poison>0:
        bossh += -3
        poison += -1
        if poison > 0:
            movesList.remove('poison')
    if Recharge > 0:
        mana += 101
        recharge += -1
        if recharge > 0:
            movesList.remove('recharge')
    if Sheild>0:
        bossDam += -7
        sheild += -1
        if sheild > 0:
            movesList.remove('sheild')
    if PlayerH <= 0 or mana <= 0:
        return [-1]
    if BossH <= 0 or bossh <= 0:
        return [manaUsed]
    recurs = []
    if playerTurn:
        if movesList.count('magic missile')>0:
            recurs += bfs(bossh-4, PlayerH, mana-spellsCost['magic missile'], sheild, poison, recharge, False, manaUsed+spellsCost['magic missile'])
        if movesList.count('drain')>0:
            recurs += bfs(bossh-2, PlayerH+2, mana-spellsCost['drain'], sheild, poison, recharge, False, manaUsed+spellsCost['drain'])
        if movesList.count('sheild')>0:
            recurs += bfs(bossh, PlayerH, mana-spellsCost['sheild'], 6, poison, recharge, False, manaUsed+spellsCost['sheild'])
        if movesList.count('recharge')>0:
            recurs += bfs(bossh, PlayerH, mana-spellsCost['recharge'], sheild, poison, 5, False, manaUsed+spellsCost['recharge'])
        if movesList.count('poison')>0:
            recurs += bfs(bossh, PlayerH, mana-spellsCost['poison'], sheild, 6, recharge, False, manaUsed+spellsCost['poison'])
    else:
        recurs += bfs(bossh, PlayerH-bossDam, mana, sheild, poison, recharge, True, manaUsed)
    if recurs.count(-1) != len(recurs):
        return [min([i for i in recurs if i>-1])]
    return [-1]

print(bfs(BossHealth, PlayerHealth, PlayerMana, 0,0,0,True,0))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[42] = '2015|Day 22|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()