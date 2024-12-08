import numpy as np

def p10(klucz):
    klucz_p10 = np.array([klucz[2], klucz[4], klucz[1], klucz[6], klucz[3], klucz[9], klucz[0], klucz[8], klucz[7], klucz[5]])
    klucz_p10_lewy, klucz_p10_prawy = np.array_split(klucz_p10, 2)
    klucz_p10_lewy_shift = np.roll(klucz_p10_lewy, -1)
    klucz_p10_prawy_shift = np.roll(klucz_p10_prawy, -1)
    permutacja10 = np.concatenate((klucz_p10_lewy_shift, klucz_p10_prawy_shift))
    # print(f'Klucz po p10: {permutacja10}')
    return permutacja10

def p8(permutacja10):
    klucz_1 = np.array([permutacja10[5], permutacja10[2], permutacja10[6], permutacja10[3], permutacja10[7], permutacja10[4], permutacja10[9], permutacja10[8]])
    permutacja10_lewy, permutacja10_prawy = np.array_split(permutacja10, 2)
    permutacja10_lewy_shift = np.roll(permutacja10_lewy, -2)
    permutacja10_prawy_shift = np.roll(permutacja10_prawy, -2)
    shift_caly = np.concatenate((permutacja10_lewy_shift, permutacja10_prawy_shift))
    klucz_2 = np.array([shift_caly[5], shift_caly[2], shift_caly[6], shift_caly[3], shift_caly[7], shift_caly[4], shift_caly[9], shift_caly[8]])
    # print(f'Klucz 1: {klucz_1}, klucz 2: {klucz_2}')
    return klucz_1, klucz_2

def ip(tekst_jawny):
    p8_tekst = np.array([tekst_jawny[1], tekst_jawny[5], tekst_jawny[2], tekst_jawny[0], tekst_jawny[3], tekst_jawny[7], tekst_jawny[4], tekst_jawny[6]])
    p8_tekst_lewy, p8_tekst_prawy = np.array_split(p8_tekst, 2)
    return p8_tekst_lewy, p8_tekst_prawy

def fk(prawe_ip, lewe_ip, klucz):
    ep = np.array([prawe_ip[3], prawe_ip[0], prawe_ip[1], prawe_ip[2], prawe_ip[1], prawe_ip[2], prawe_ip[3], prawe_ip[0]])
    xorep = np.bitwise_xor(klucz, ep)
    xorep_lewy, xorep_prawy = np.array_split(xorep, 2)
    s0 = np.array([[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]])
    s1 = np.array([[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]])
    row_s0 = int(f"{xorep_lewy[0]}{xorep_lewy[3]}", 2)
    col_s0 = int(f"{xorep_lewy[1]}{xorep_lewy[2]}", 2)
    row_s1 = int(f"{xorep_prawy[0]}{xorep_prawy[3]}", 2)
    col_s1 = int(f"{xorep_prawy[1]}{xorep_prawy[2]}", 2)
    s0_value = s0[row_s0, col_s0]
    s1_value = s1[row_s1, col_s1]
    # print(f"S0[{row_s0}, {col_s0}] = {s0_value}, S1[{row_s1}, {col_s1}] = {s1_value}")
    s0_bin = [int(bit) for bit in f'{s0_value:02b}']
    s1_bin = [int(bit) for bit in f'{s1_value:02b}']
    s0_plus_s1 = np.concatenate((s0_bin, s1_bin))
    sp4 = np.array([s0_plus_s1[1], s0_plus_s1[3], s0_plus_s1[2], s0_plus_s1[0]])
    xorsl = np.bitwise_xor(sp4, lewe_ip)
    fk_obl = np.concatenate((xorsl, prawe_ip))
    # print(f'Fk po obliczeniu: {fk_obl}')
    return fk_obl

def sw(fk_pierwsze):
    fk_zamiana = np.roll(fk_pierwsze, -4)
    fk_zm_lewy, fk_zm_prawy = np.array_split(fk_zamiana,2)
    # print(f'Fk po zmianie lewy: {fk_zm_lewy} i prawy: {fk_zm_prawy}')
    return fk_zm_lewy, fk_zm_prawy

def ip_minus(fk_drugie):
    ip_minus1 = np.array([fk_drugie[3], fk_drugie[0], fk_drugie[2], fk_drugie[4], fk_drugie[6], fk_drugie[1], fk_drugie[7], fk_drugie[5]])
    return ip_minus1

def litery(wynik):
    value = int("".join(map(str, wynik)), 2)
    if value == 0:
        return '-'
    return chr(value - 1 + ord('A'))

def fun(tekst_jawny, klucz):
    klucz_10 = p10(klucz)
    klucz_jeden, klucz_dwa = p8(klucz_10)
    lewy_ip, prawy_ip = ip(tekst_jawny)
    fk_pierwsze = fk(prawy_ip, lewy_ip, klucz_jeden)
    sw_lewy, sw_prawy = sw(fk_pierwsze)
    fk_drugie = fk(sw_prawy, sw_lewy, klucz_dwa)
    wynik = ip_minus(fk_drugie)
    wynik_lewy, wynik_prawy = np.array_split(wynik, 2)
    wynik_tekst_1 = litery(wynik_lewy)
    wynik_tekst_2 = litery(wynik_prawy)
    print(f'Wynik operacji: {wynik}, {wynik_tekst_1}{wynik_tekst_2}')


tekst_jawny = [1, 0, 0, 1, 1, 0, 0, 1]
klucz = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
ntekst_jawny = [0, 1, 1, 0, 0, 1, 1, 0]
nklucz = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

jeden = fun(tekst_jawny, klucz)
dwa = fun(ntekst_jawny, klucz)
trzy = fun(ntekst_jawny, nklucz)



