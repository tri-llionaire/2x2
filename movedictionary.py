def or_L(current):
    new = list(current)
    new[2] = current[20]
    new[3] = current[17]
    new[10] = current[2]
    new[11] = current[3]
    new[17] = current[23]
    new[20] = current[22]
    new[22] = current[10]
    new[23] = current[11]
    new[5] = current[6]
    new[6] = current[7]
    new[7] = current[8]
    new[8] = current[5]
    return new
def or_Lp(current):
    new = list(current)
    new[2] = current[10]
    new[3] = current[11]
    new[10] = current[22]
    new[11] = current[23]
    new[17] = current[3]
    new[20] = current[2]
    new[22] = current[20]
    new[23] = current[17]
    new[5] = current[8]
    new[6] = current[5]
    new[7] = current[6]
    new[8] = current[7]
    return new
def or_Ld(current):
    new = list(current)
    new[2] = current[22]
    new[3] = current[23]
    new[10] = current[20]
    new[11] = current[17]
    new[17] = current[11]
    new[20] = current[10]
    new[22] = current[2]
    new[23] = current[3]
    new[5] = current[7]
    new[6] = current[8]
    new[7] = current[5]
    new[8] = current[6]
    return new
def or_D(current):
    new = list(current)
    new[7] = current[19]
    new[8] = current[20]
    new[11] = current[7]
    new[12] = current[8]
    new[15] = current[11]
    new[16] = current[12]
    new[19] = current[15]
    new[20] = current[16]
    new[21] = current[22]
    new[22] = current[23]
    new[23] = current[24]
    new[24] = current[21]
    return new
def or_Dp(current):
    new = list(current)
    new[7] = current[11]
    new[8] = current[12]
    new[11] = current[15]
    new[12] = current[16]
    new[15] = current[19]
    new[16] = current[20]
    new[19] = current[7]
    new[20] = current[8]
    new[21] = current[24]
    new[22] = current[21]
    new[23] = current[22]
    new[24] = current[23]
    return new
def or_Dd(current):
    new = list(current)
    new[7] = current[15]
    new[8] = current[16]
    new[11] = current[19]
    new[12] = current[20]
    new[15] = current[7]
    new[16] = current[8]
    new[19] = current[11]
    new[20] = current[12]
    new[21] = current[23]
    new[22] = current[24]
    new[23] = current[21]
    new[24] = current[22]
    return new
def or_B(current):
    new = list(current)
    new[1] = current[16]
    new[2] = current[13]
    new[6] = current[1]
    new[7] = current[2]
    new[13] = current[24]
    new[16] = current[23]
    new[23] = current[6]
    new[24] = current[7]
    new[17] = current[18]
    new[18] = current[19]
    new[19] = current[20]
    new[20] = current[17]
    return new
def or_Bp(current):
    new = list(current)
    new[1] = current[6]
    new[2] = current[7]
    new[6] = current[24]
    new[7] = current[23]
    new[13] = current[2]
    new[16] = current[1]
    new[23] = current[16]
    new[24] = current[13]
    new[17] = current[20]
    new[18] = current[17]
    new[19] = current[18]
    new[20] = current[19]
    return new
def or_Bd(current):
    new = list(current)
    new = list(current)
    new[1] = current[23]
    new[2] = current[24]
    new[6] = current[16]
    new[7] = current[13]
    new[13] = current[7]
    new[16] = current[6]
    new[23] = current[1]
    new[24] = current[2]
    new[17] = current[19]
    new[18] = current[20]
    new[19] = current[17]
    new[20] = current[18]
    return new
def move_R(current):
    new = list(current)
    new[1] = current[9]
    new[4] = current[12]
    new[9] = current[21]
    new[12] = current[24]
    new[18] = current[4]
    new[19] = current[1]
    new[21] = current[19]
    new[24] = current[18]
    new[13] = current[14]
    new[14] = current[15]
    new[15] = current[16]
    new[16] = current[13]
    return new
def move_Rp(current):
    new = list(current)
    new[1] = current[19]
    new[4] = current[18]
    new[9] = current[1]
    new[12] = current[4]
    new[18] = current[24]
    new[19] = current[21]
    new[21] = current[9]
    new[24] = current[12]
    new[13] = current[16]
    new[14] = current[13]
    new[15] = current[14]
    new[16] = current[15]
    return new
def move_Rd(current):
    new = list(current)
    new[1] = current[21]
    new[4] = current[24]
    new[9] = current[19]
    new[12] = current[18]
    new[18] = current[12]
    new[19] = current[9]
    new[21] = current[1]
    new[24] = current[4]
    new[13] = current[15]
    new[14] = current[16]
    new[15] = current[13]
    new[16] = current[14]
    return new
def move_U(current):
    new = list(current)
    new[5] = current[9]
    new[6] = current[10]
    new[9] = current[13]
    new[10] = current[14]
    new[13] = current[17]
    new[14] = current[18]
    new[17] = current[5]
    new[18] = current[6]
    new[1] = current[2]
    new[2] = current[3]
    new[3] = current[4]
    new[4] = current[1]
    return new
def move_Up(current):
    new = list(current)
    new[5] = current[17]
    new[6] = current[18]
    new[9] = current[5]
    new[10] = current[6]
    new[13] = current[9]
    new[14] = current[10]
    new[17] = current[13]
    new[18] = current[14]
    new[1] = current[4]
    new[2] = current[1]
    new[3] = current[2]
    new[4] = current[3]
    return new
def move_Ud(current):
    new = list(current)
    new[5] = current[13]
    new[6] = current[14]
    new[9] = current[17]
    new[10] = current[18]
    new[13] = current[5]
    new[14] = current[6]
    new[17] = current[9]
    new[18] = current[10]
    new[1] = current[3]
    new[2] = current[4]
    new[3] = current[1]
    new[4] = current[2]
    return new
def move_F(current):
    new = list(current)
    new[3] = current[8]
    new[4] = current[5]
    new[5] = current[22]
    new[8] = current[21]
    new[14] = current[3]
    new[15] = current[4]
    new[21] = current[14]
    new[22] = current[15]
    new[9] = current[10]
    new[10] = current[11]
    new[11] = current[12]
    new[12] = current[9]
    return new
def move_Fp(current):
    new = list(current)
    new[3] = current[14]
    new[4] = current[15]
    new[5] = current[4]
    new[8] = current[3]
    new[14] = current[21]
    new[15] = current[22]
    new[21] = current[8]
    new[22] = current[5]
    new[9] = current[12]
    new[10] = current[9]
    new[11] = current[10]
    new[12] = current[11]
    return new
def move_Fd(current):
    new = list(current)
    new[3] = current[21]
    new[4] = current[22]
    new[5] = current[15]
    new[8] = current[14]
    new[14] = current[8]
    new[15] = current[5]
    new[21] = current[3]
    new[22] = current[4]
    new[9] = current[11]
    new[10] = current[12]
    new[11] = current[9]
    new[12] = current[10]
    return new
