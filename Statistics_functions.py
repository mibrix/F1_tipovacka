import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

def score_and_matrix(gp_id, conn):

    c = conn.cursor()

    player_names = ["Wonde", "Tome", "Hrici", "Kajlo", "Sasu", "OG"]
    matrix_of_ans = {}
    score = []
    percentage = []
    for i in range(len(player_names)):
        matrix_i = [None for _ in range(15)]
        # correct answers
        c.execute(f'''SELECT a.question_id FROM bets a JOIN ground_truth b
                     ON a.grand_prix_id = b.grand_prix_id
                     AND a.answer = b.correct_ans
                     AND a.question_id = b.question_id
                     WHERE a.player_id = {i + 1}
                     AND a.grand_prix_id = {gp_id}''')
        myresult = c.fetchall()
        correct_pts = len(myresult) * 2
        minus_pts = 0

        # matrix
        for q_id in myresult:
            matrix_i[q_id[0] - 1] = True

        # if DNF player was correct
        if (6,) in myresult:
            matrix_i[5] = True
        else:
            minus_pts += 1
            matrix_i[5] = False

        # incorrect answers
        c.execute(f'''SELECT a.question_id FROM bets a JOIN ground_truth b
                 ON a.grand_prix_id = b.grand_prix_id
                 AND a.answer <> b.correct_ans
                 AND a.question_id = b.question_id
                 WHERE a.player_id = {i + 1}
                 AND a.grand_prix_id = {gp_id}''')

        myresult1 = c.fetchall()
        for ans in myresult1:
            if ans[0] >= 1 and ans[0] <= 11 and ans[0] != 6:
                minus_pts += 1
            if ans[0] != 6:
                matrix_i[ans[0] - 1] = False

        matrix_of_ans[player_names[i]] = matrix_i + [None, None]
        score.append(max(correct_pts - minus_pts, -6))
        percentage.append(correct_pts / 2 / 15 * 100)

    return (score, matrix_of_ans, percentage)


def answers(gp_id, conn):
    c = conn.cursor()

    player_names = ["Wonde", "Tome", "Hrici", "Kajlo", "Sasu", "OG"]
    d = {"Wonde": [None for _ in range(15)], "Tome": [None for _ in range(15)], "Hrici": [None for _ in range(15)],
         "Kajlo": [None for _ in range(15)], "Sasu": [None for _ in range(15)], "OG": [None for _ in range(15)]}
    c.execute(f'''SELECT * FROM bets
                  WHERE grand_prix_id = {gp_id}''')

    myresult = c.fetchall()
    for ans in myresult:
        d[player_names[int(ans[1]) - 1]][ans[0] - 1] = ans[3]

    # add score
    for n, score in enumerate(score_and_matrix(gp_id, conn)[0]):
        d[player_names[n]].append(score)

    for n, per in enumerate(score_and_matrix(gp_id, conn)[2]):
        d[player_names[n]].append(per)

    df = pd.DataFrame(data=d)

    # add questions
    c.execute(f'''SELECT text FROM questions''')
    myresult1 = c.fetchall()
    questions = []
    for que in myresult1:
        questions.append(que[0])
    questions.append('Body')
    questions.append('Uspesnost %')
    df.index = questions

    # matrix of correctness
    df_bool = pd.DataFrame(score_and_matrix(gp_id, conn)[1])
    df_bool.index = questions


    def color_boolean(val):
        out = 'background-color: '
        if val == True:
            return out + "#e6ffe6"
        elif val == False:
            return out + "#ffe6e6"
        elif val == None:
            return out + "yellow"

    display(df.style.apply(lambda _: df_bool.applymap(color_boolean), axis=None))
    display(df.style.apply(lambda c: df_bool[c.name].apply(color_boolean)))


# https://stackoverflow.com/questions/72236704/highlight-element-based-on-boolean-pandas-df

def sum_pts(n_of_gp, conn):

    player_names = ["Wonde", "Tome", "Hrici", "Kajlo", "Sasu", "OG"]
    score = score_and_matrix(1, conn)[0]
    for i in range(2, n_of_gp + 1):
        for n, r in enumerate(score_and_matrix(i, conn)[0]):
            score[n] += r

    # plot
    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(player_names, score, width=0.4)

    plt.ylabel("Pocet bodov")
    plt.title("Celkovy pocet bodov")
    plt.show()

    print({player_names[i]: score[i] for i in range(len(player_names))})



def continuity(n_of_gp, conn):

    player_names = ["Wonde", "Tome", "Hrici", "Kajlo", "Sasu", "OG"]
    score = score_and_matrix(1, conn)[0]
    d = {player_names[i]: [score[i]] for i in range(len(player_names))}
    for i in range(2, n_of_gp + 1):
        for n, r in enumerate(score_and_matrix(i, conn)[0]):
            d[player_names[n]].append(d[player_names[n]][-1] + r)

    # plot
    for key, val in d.items():
        plt.plot(val, label=key)
    plt.legend(loc='lower center')
    plt.show()
    print(d)


