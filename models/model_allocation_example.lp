\ Model AllocationTeamMineraGitPo
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  4 allocate[0,0] + 3 allocate[0,1] + 4 allocate[0,2] + 56 allocate[1,0]
   + 7 allocate[1,1] + 78 allocate[1,2] + 5 allocate[2,0]
   + 34 allocate[2,1] + 3 allocate[2,2] + 3 allocate[3,0]
   + 88 allocate[3,1] + 3 allocate[3,2] + 4 allocate[4,0]
   + 56 allocate[4,1] + 4 allocate[4,2] + 9 allocate[5,0] + 5 allocate[5,1]
   + 6 allocate[5,2] + 5 allocate[6,0] + 9 allocate[6,1] + 4 allocate[6,2]
   + 6 allocate[7,0] + 7 allocate[7,1] + 5 allocate[7,2] + 7 allocate[8,0]
   + 10 allocate[8,1] + 5 allocate[8,2] + 34 allocate[9,0]
   + 3 allocate[9,1] + allocate[9,2]
Subject To
 totalidade[0]: allocate[0,0] + allocate[0,1] + allocate[0,2] <= 1
 totalidade[1]: allocate[1,0] + allocate[1,1] + allocate[1,2] <= 1
 totalidade[2]: allocate[2,0] + allocate[2,1] + allocate[2,2] <= 1
 totalidade[3]: allocate[3,0] + allocate[3,1] + allocate[3,2] <= 1
 totalidade[4]: allocate[4,0] + allocate[4,1] + allocate[4,2] <= 1
 totalidade[5]: allocate[5,0] + allocate[5,1] + allocate[5,2] <= 1
 totalidade[6]: allocate[6,0] + allocate[6,1] + allocate[6,2] <= 1
 totalidade[7]: allocate[7,0] + allocate[7,1] + allocate[7,2] <= 1
 totalidade[8]: allocate[8,0] + allocate[8,1] + allocate[8,2] <= 1
 totalidade[9]: allocate[9,0] + allocate[9,1] + allocate[9,2] <= 1
 cardinalidade_min[0]: allocate[0,0] + allocate[1,0] + allocate[2,0]
   + allocate[3,0] + allocate[4,0] + allocate[5,0] + allocate[6,0]
   + allocate[7,0] + allocate[8,0] + allocate[9,0] >= 1
 cardinalidade_min[1]: allocate[0,1] + allocate[1,1] + allocate[2,1]
   + allocate[3,1] + allocate[4,1] + allocate[5,1] + allocate[6,1]
   + allocate[7,1] + allocate[8,1] + allocate[9,1] >= 1
 cardinalidade_min[2]: allocate[0,2] + allocate[1,2] + allocate[2,2]
   + allocate[3,2] + allocate[4,2] + allocate[5,2] + allocate[6,2]
   + allocate[7,2] + allocate[8,2] + allocate[9,2] >= 1
 cardinalidade_max[0]: allocate[0,0] + allocate[1,0] + allocate[2,0]
   + allocate[3,0] + allocate[4,0] + allocate[5,0] + allocate[6,0]
   + allocate[7,0] + allocate[8,0] + allocate[9,0] <= 2
 cardinalidade_max[1]: allocate[0,1] + allocate[1,1] + allocate[2,1]
   + allocate[3,1] + allocate[4,1] + allocate[5,1] + allocate[6,1]
   + allocate[7,1] + allocate[8,1] + allocate[9,1] <= 3
 cardinalidade_max[2]: allocate[0,2] + allocate[1,2] + allocate[2,2]
   + allocate[3,2] + allocate[4,2] + allocate[5,2] + allocate[6,2]
   + allocate[7,2] + allocate[8,2] + allocate[9,2] <= 1
 conhecimento_min[0]: >= 0
 conhecimento_min[1]: allocate[0,1] + allocate[8,1] + allocate[9,1] >= 0
 conhecimento_min[2]: allocate[9,2] >= 0
 conhecimento_max[0]: allocate[5,0] >= 1
 conhecimento_max[1]: allocate[1,1] + allocate[3,1] + allocate[6,1]
   + allocate[7,1] >= 0
 conhecimento_max[2]: allocate[1,2] >= 0
Bounds
Binaries
 allocate[0,0] allocate[0,1] allocate[0,2] allocate[1,0] allocate[1,1]
 allocate[1,2] allocate[2,0] allocate[2,1] allocate[2,2] allocate[3,0]
 allocate[3,1] allocate[3,2] allocate[4,0] allocate[4,1] allocate[4,2]
 allocate[5,0] allocate[5,1] allocate[5,2] allocate[6,0] allocate[6,1]
 allocate[6,2] allocate[7,0] allocate[7,1] allocate[7,2] allocate[8,0]
 allocate[8,1] allocate[8,2] allocate[9,0] allocate[9,1] allocate[9,2]
End
