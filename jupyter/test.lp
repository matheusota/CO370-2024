\ Model flights
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  f_s0,f0^0 + f_s1,f1^1 + f_s2,f1^2
Subject To
 R0: - f_s1,f1^0 = 0
 R1: f_f2,t1^0 = 0
 R2: - f_s2,f1^0 = 0
 R3: f_f3,t2^0 = 0
 R4: - f_f0,f1^0 - f_f0,f2^0 + f_s0,f0^0 = 0
 R5: f_f0,f1^0 - f_f1,f2^0 - f_f1,f3^0 + f_s1,f1^0 + f_s2,f1^0 = 0
 R6: f_f0,f2^0 + f_f1,f2^0 - f_f2,f3^0 - f_f2,t1^0 = 0
 R7: f_f1,f3^0 + f_f2,f3^0 - f_f3,t2^0 - f_f3,t0^0 = 0
 R8: - f_s0,f0^1 = 0
 R9: f_f3,t0^1 = 0
 R10: - f_s2,f1^1 = 0
 R11: f_f3,t2^1 = 0
 R12: - f_f0,f1^1 - f_f0,f2^1 + f_s0,f0^1 = 0
 R13: f_f0,f1^1 - f_f1,f2^1 - f_f1,f3^1 + f_s1,f1^1 + f_s2,f1^1 = 0
 R14: f_f0,f2^1 + f_f1,f2^1 - f_f2,f3^1 - f_f2,t1^1 = 0
 R15: f_f1,f3^1 + f_f2,f3^1 - f_f3,t2^1 - f_f3,t0^1 = 0
 R16: - f_s0,f0^2 = 0
 R17: f_f3,t0^2 = 0
 R18: - f_s1,f1^2 = 0
 R19: f_f2,t1^2 = 0
 R20: - f_f0,f1^2 - f_f0,f2^2 + f_s0,f0^2 = 0
 R21: f_f0,f1^2 - f_f1,f2^2 - f_f1,f3^2 + f_s1,f1^2 + f_s2,f1^2 = 0
 R22: f_f0,f2^2 + f_f1,f2^2 - f_f2,f3^2 - f_f2,t1^2 = 0
 R23: f_f1,f3^2 + f_f2,f3^2 - f_f3,t2^2 - f_f3,t0^2 = 0
 R24: f_s0,f0^0 + f_s0,f0^1 + f_s0,f0^2 <= 50
 R25: f_f0,f1^0 + f_f0,f1^1 + f_f0,f1^2 + f_s1,f1^0 + f_s1,f1^1 + f_s1,f1^2
   + f_s2,f1^0 + f_s2,f1^1 + f_s2,f1^2 <= 20
 R26: f_f0,f2^0 + f_f0,f2^1 + f_f0,f2^2 + f_f1,f2^0 + f_f1,f2^1 + f_f1,f2^2
   <= 25
 R27: f_f1,f3^0 + f_f1,f3^1 + f_f1,f3^2 + f_f2,f3^0 + f_f2,f3^1 + f_f2,f3^2
   <= 40
Bounds
 f_f0,f1^0 <= 30
 f_f0,f1^1 <= 12
 f_f0,f1^2 <= 25
 f_f0,f2^0 <= 30
 f_f0,f2^1 <= 12
 f_f0,f2^2 <= 25
 f_f1,f2^0 <= 30
 f_f1,f2^1 <= 12
 f_f1,f2^2 <= 25
 f_f1,f3^0 <= 30
 f_f1,f3^1 <= 12
 f_f1,f3^2 <= 25
 f_f2,f3^0 <= 30
 f_f2,f3^1 <= 12
 f_f2,f3^2 <= 25
 f_s0,f0^0 <= 30
 f_s0,f0^1 <= 12
 f_s0,f0^2 <= 25
 f_s1,f1^0 <= 30
 f_s1,f1^1 <= 12
 f_s1,f1^2 <= 25
 f_s2,f1^0 <= 30
 f_s2,f1^1 <= 12
 f_s2,f1^2 <= 25
 f_f2,t1^0 <= 30
 f_f2,t1^1 <= 12
 f_f2,t1^2 <= 25
 f_f3,t2^0 <= 30
 f_f3,t2^1 <= 12
 f_f3,t2^2 <= 25
 f_f3,t0^0 <= 30
 f_f3,t0^1 <= 12
 f_f3,t0^2 <= 25
Generals
 f_f0,f1^0 f_f0,f1^1 f_f0,f1^2 f_f0,f2^0 f_f0,f2^1 f_f0,f2^2 f_f1,f2^0
 f_f1,f2^1 f_f1,f2^2 f_f1,f3^0 f_f1,f3^1 f_f1,f3^2 f_f2,f3^0 f_f2,f3^1
 f_f2,f3^2 f_s0,f0^0 f_s0,f0^1 f_s0,f0^2 f_s1,f1^0 f_s1,f1^1 f_s1,f1^2
 f_s2,f1^0 f_s2,f1^1 f_s2,f1^2 f_f2,t1^0 f_f2,t1^1 f_f2,t1^2 f_f3,t2^0
 f_f3,t2^1 f_f3,t2^2 f_f3,t0^0 f_f3,t0^1 f_f3,t0^2
End
