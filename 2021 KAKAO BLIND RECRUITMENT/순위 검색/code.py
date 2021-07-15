def solution(info, query):
    answer = []
    mp = {}
    SZ = 100000
    for language in ['java', 'python', 'cpp', 'all']:
        mp[language] = {}
        for work in ['backend', 'frontend', 'all']:
            mp[language][work] = {}
            for year in ['junior', 'senior', 'all']:
                mp[language][work][year] = {}
                for favorite in ['pizza', 'chicken', 'all']:
                    mp[language][work][year][favorite] = [0] * (SZ + 1)
    for atom in info:
        atom = atom.split(' ')
        for language in [atom[0], 'all']:
            for work in [atom[1], 'all']:
                for year in [atom[2], 'all']:
                    for favorite in [atom[3], 'all']:
                        mp[language][work][year][favorite][int(atom[4])] += 1
    for language in ['java', 'python', 'cpp', 'all']:
        for work in ['backend', 'frontend', 'all']:
            for year in ['junior', 'senior', 'all']:
                for favorite in ['pizza', 'chicken', 'all']:
                    for i in range(1, SZ + 1):
                        mp[language][work][year][favorite][i] += mp[language][work][year][favorite][i - 1]
    for q in query:
        q = q.split(' ')
        language = q[0] if q[0] != '-' else 'all'
        work = q[2] if q[2] != '-' else 'all'
        year = q[4] if q[4] != '-' else 'all'
        favorite = q[6] if q[6] != '-' else 'all'
        num = int(q[7])
        answer.append(mp[language][work][year][favorite][SZ] - mp[language][work][year][favorite][num - 1])
    return answer
